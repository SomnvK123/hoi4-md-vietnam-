"""Export captured 39-node baseline and current 24-node industry layout."""
import json
import xml.etree.ElementTree as ET
from industry_diagram import ROOT, draw, labels, xml_page, focus_map, positions, groups, value, values


def main():
    out = ROOT / '.claude/docs/industry/v31'
    snapshot = json.loads((out / 'before.json').read_text(encoding='utf-8'))
    before = {fid: dict(x=xy[0], y=xy[1], pre=snapshot['pre'][fid]) for fid, xy in snapshot['pos'].items()}
    for left, right in [('VIE_fdi_fast_track', 'VIE_fdi_technology_screening'), ('VIE_chip_design_packaging_priority', 'VIE_chip_pilot_fab_priority')]:
        before[left]['ex'] = [right]
        before[right]['ex'] = [left]
    manifest = json.loads((out / 'structure.json').read_text(encoding='utf-8'))
    focuses = focus_map((ROOT / 'common/national_focus/VIE_md_focus.txt').read_text(encoding='utf-8'))
    pos = positions(focuses)
    after = {n['id']: dict(x=pos[n['id']][0], y=pos[n['id']][1], pre=groups(focuses[n['id']]), ex=values(value(focuses[n['id']], 'mutually_exclusive', []), 'focus')) for n in manifest['focuses']}
    assert len(before) == 39 and len(after) == 24
    (out / 'after.json').write_text(json.dumps(after, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    mx = ET.Element('mxfile', {'host': 'app.diagrams.net', 'compressed': 'false'})
    for graph, names, title, stem in [(before, snapshot['titles'], 'Công nghiệp trước sửa: 39 focus', 'before'), (after, labels(), 'Công nghiệp v31: 24 focus — 3/6 ngành, năng suất và 32 điểm', 'after')]:
        draw(graph, names, title, out / (stem+'.png'))
        xml_page(mx, graph, names, title)
    ET.indent(mx)
    ET.ElementTree(mx).write(out / 'industry_v31.drawio', encoding='utf-8', xml_declaration=True)
    print('PASS: captured 39-node baseline / live 24-node manifest; PNG and editable drawio')


if __name__ == '__main__':
    main()
