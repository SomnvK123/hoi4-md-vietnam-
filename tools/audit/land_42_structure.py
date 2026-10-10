"""Validate the authored land-42 graph and preserve the unrelated baseline.

Reads live PDX through the repository parser. No engine or AI simulation.
Run from any directory; stdlib only. Never writes an audit artifact.
"""
import hashlib
import json
from industry import ROOT, focus_map, positions, groups, value, values, walk

DOCUMENT = ROOT / '.claude/docs/land_force/v39/structure.json'


def load():
    manifest = json.loads(DOCUMENT.read_text(encoding='utf-8'))
    focuses = focus_map((ROOT / 'common/national_focus/VIE_md_focus.txt').read_text(encoding='utf-8-sig'))
    records = {n['code']: n for n in manifest['focuses']}
    return manifest, focuses, records


def reachable(focuses, records, route, excluded=()):
    forbidden = {records[c]['id'] for c in excluded}
    selected = {n['id'] for c, n in records.items() if c[0] not in 'PMR' or c[0] == route}
    done = {'VIE_modernize_vpa'}
    while True:
        more = {f for f in selected - done - forbidden
                if all(any(p in done for p in g) for g in groups(focuses[f]))}
        if not more:
            return done
        done |= more


def main():
    manifest, focuses, records = load()
    ids = {c: n['id'] for c, n in records.items()} | {'ROOT': 'VIE_modernize_vpa'}
    owned = set(ids.values()) - {'VIE_modernize_vpa'}
    assert len(records) == len(owned) == 42
    assert {k for k in focuses if k.startswith('VIE_lf_')} == owned
    assert len(focuses) == manifest['baseline_count'] + 42
    assert not any(k.startswith('VIE_lf_sf_') for k in focuses)
    xy, order = positions(focuses), list(focuses)
    for code, n in records.items():
        b, fid = focuses[n['id']], n['id']
        assert groups(b) == [[ids[c] for c in g] for g in n['groups']], (code, 'gates')
        assert xy[fid] == tuple(n['xy']), (code, 'coordinates')
        assert int(value(b, 'cost')) == n['cost'], (code, 'cost')
        anchor = value(b, 'relative_position_id')
        assert anchor == ids[n['anchor']] and anchor in {p for g in groups(b) for p in g}
        assert order.index(anchor) < order.index(fid), (code, 'forward anchor')
        available = value(b, 'available', [])
        assert available == ([('date', '>', f'{n["year"] - 1}.12.31')] if n['year'] else [])
        assert not values(b, 'bypass'), (code, 'unexpected bypass')
        assert value(b, 'icon') == n['icon']
        reward = value(b, 'completion_reward')
        assert reward[0][0] == 'log'
        assert value(reward, f'VIE_lf_reward_{code.lower()}_effect') == 'yes'
        mutex = {p for g in values(b, 'mutually_exclusive') for p in values(g, 'focus')}
        expected = {ids[c] for c in ('P1', 'M1', 'R1') if c != code} if code in ('P1', 'M1', 'R1') else set()
        assert mutex == expected, (code, 'mutex')
        assert not any(k == 'has_active_mission' for k, _, _ in walk(value(b, 'ai_will_do'))), (code, 'free focus bankruptcy gate')

    # Detect collisions/gaps against the whole current tree, not only new nodes.
    assert len(set(xy.values())) == len(xy)
    for fid in owned:
        x, y = xy[fid]
        assert all(abs(x - ox) >= 2 for other, (ox, oy) in xy.items() if other != fid and oy == y)
    for route in 'PMR':
        done = reachable(focuses, records, route)
        assert len(done) - 1 == 30 and ids['F2'] in done
        no_industry = reachable(focuses, records, route, [f'I{i}' for i in range(1, 6)])
        assert len(no_industry) - 1 == 25 and ids['F2'] in no_industry
        no_d8 = reachable(focuses, records, route, ['D8'])
        assert ids['F1'] in no_d8 and ids['F2'] not in no_d8
        for missing in (route + '4', route + '5', 'B7', 'B6'):
            assert ids['F1'] not in reachable(focuses, records, route, [missing])

    for fid, digest in manifest['preserved_focuses'].items():
        actual = hashlib.sha256(json.dumps(focuses[fid], ensure_ascii=False).encode()).hexdigest()
        assert actual == digest, ('Unrelated focus changed', fid)
    for relative, digest in manifest['protected_files'].items():
        assert hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() == digest, ('Protected file changed', relative)
    print('PASS: 42 nodes, exact gates/costs/dates/anchors, symmetric mutex, 3 reachable routes, optional industry, 317 preserved focuses and protected files.')
    print('Static graph only: engine connectors, dates in-game and AI progression require runtime QA.')


if __name__ == '__main__':
    try:
        main()
    except (AssertionError, ValueError, KeyError) as exc:
        raise SystemExit('FAIL: ' + str(exc))
