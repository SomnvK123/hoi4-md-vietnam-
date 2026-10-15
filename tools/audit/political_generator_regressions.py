"""Kiem generator tren ban sao tam; khong ghi vao checkout."""
from pathlib import Path
import ast, re, shutil, subprocess, sys, tempfile

ROOT = Path(__file__).resolve().parents[2]
ns = {}
tree = ast.parse((ROOT/'tools/audit/audit.py').read_text(encoding='utf-8'))
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)
                             and n.name in ('tokenize','parse')],type_ignores=[]),'parser','exec'),ns)

def canonical(block):
    return [(k,op,canonical(v) if isinstance(v,list) else v) for k,op,v,line in block]

def parsed(path):
    text=path.read_text(encoding='utf-8-sig')
    text=re.sub(r'#[^\n]*|"(?:\\.|[^"\\])*"',lambda m:m[0] if m[0].startswith('"') else '',text)
    return ns['parse'](ns['tokenize'](text))

def layout(path):
    tree=next(v for k,op,v,line in parsed(path) if k=='focus_tree')
    keys={'id','icon','x','y','relative_position_id','prerequisite','mutually_exclusive','cost'}
    return [canonical([n for n in v if n[0] in keys]) for k,op,v,line in tree if k=='focus']

def files(root):
    return {p.relative_to(root):p.read_bytes() for folder in ('common','events','localisation')
            for p in (root/folder).rglob('*') if p.is_file() and p.suffix in ('.txt','.yml')}

def main():
    generator=ast.parse((ROOT/'tools/build_political_runtime.py').read_text(encoding='utf-8'))
    helpers={'re':re}
    exec(compile(ast.Module(body=[n for n in generator.body if isinstance(n,ast.FunctionDef)
                                 and n.name=='normalize_pp'],type_ignores=[]),'normalize','exec'),helpers)
    old='# political_power < 99\nlog = "political_power < 8"\nNOT = { political_power < 25 }\nadd_political_power = -25\nhas_political_power > 20'
    expected=old.replace('NOT = { political_power < 25 }','NOT = { has_political_power < 25 }')
    assert helpers['normalize_pp'](old)==expected,'Normalization changed comments, strings or effects'
    assert helpers['normalize_pp'](expected)==expected,'PP normalization is not idempotent'
    with tempfile.TemporaryDirectory(prefix='vie-generator-') as temporary:
        copy=Path(temporary)
        for folder in ('common','events','localisation'):
            shutil.copytree(ROOT/folder,copy/folder)
        (copy/'tools').mkdir()
        shutil.copy2(ROOT/'tools/build_political_runtime.py',copy/'tools/build_political_runtime.py')
        shutil.copy2(ROOT/'VIETNAM_POLITICAL_PARAMETERS_VI.json',copy/'VIETNAM_POLITICAL_PARAMETERS_VI.json')
        focus=Path('common/national_focus/VIE_md_focus.txt')
        before=files(copy); geometry=layout(copy/focus)
        # Tai hien input truoc ban sua; generator phai tu chuan hoa, khong chi output live.
        legacy_references=0
        legacy_paths={Path(p) for p in (
            'common/national_focus/VIE_md_focus.txt',
            'common/decisions/VIE_md_politics_runtime_decisions.txt',
            'common/scripted_triggers/VIE_md_triggers_politics_runtime.txt',
            'events/VIE_md_politics_events.txt', 'events/VIE_md_politics_runtime_events.txt')}
        for path,data in before.items():
            if path not in legacy_paths:continue
            text=data.decode('utf-8')
            text,count=re.subn(r'\bhas_political_power\b(?=\s*[<>=])','political_power',text)
            if count:
                legacy_references+=count
                (copy/path).write_text(text,encoding='utf-8')
        assert legacy_references>0,'No legacy PP input injected'
        for iteration in (1,2):
            result=subprocess.run([sys.executable,str(copy/'tools/build_political_runtime.py')],capture_output=True,text=True,encoding='utf-8')
            assert result.returncode==0,result.stdout+result.stderr
            after=files(copy)
            assert layout(copy/focus)==geometry,'Generator changed focus order/geometry/prerequisites'
            if iteration==1:
                changes=[]
                for path in before:
                    if before[path]!=after[path]:
                        changes.append(str(path))
                        # Doi whitespace duoc phep; script va loc phai giu nghia live.
                        if path.suffix=='.txt':
                            assert canonical(parsed(ROOT/path))==canonical(parsed(copy/path)),str(path)+' semantic drift'
                        else:
                            assert before[path].decode('utf-8-sig').splitlines()==after[path].decode('utf-8-sig').splitlines(),str(path)+' loc drift'
                print('First generation whitespace changes:',changes)
                first=after
            else:
                assert after==first,'Second generation is not byte-idempotent'
        print(f'PASS: {legacy_references} legacy PP inputs normalized; live semantics, all focus layout/order, second-run byte idempotence; checkout not modified')

if __name__=='__main__':main()
