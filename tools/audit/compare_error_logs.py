"""So sanh error.log MD va MD+VIE; chi doc file, khong dieu khien game."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re


def signatures(text):
    result = Counter()
    for line in text.splitlines():
        if not line.strip():
            continue
        # Bo gio va game-date; giu diagnostic/source. So dong script co the doi sau sua.
        line = re.sub(r'^\[[^\]]*\]\[[^\]]*\]', '', line).replace('\\', '/')
        line = re.sub(r'near line: \d+|line\s*:\s*\d+|(?<=\.txt):\d+', '<line>', line)
        result[line] += 1
    return result


def compare(baseline, candidate):
    old, new = signatures(baseline), signatures(candidate)
    rows = []
    for signature in sorted(old.keys() | new.keys()):
        before, after = old[signature], new[signature]
        status = 'shared' if before and after else 'candidate_only' if after else 'baseline_only'
        rows.append({'status': status, 'baseline_count': before, 'candidate_count': after,
                     'signature': signature})
    return rows


def self_test():
    old = '[10:00:00][no_game_date][trigger.cpp:700]: Bad in common/test.txt line : 12\n'
    new = '[11:00:00][2000.1.1][trigger.cpp:700]: Bad in common/test.txt line : 40\n'
    assert compare(old, new)[0]['status'] == 'shared'
    rows = compare(old, new * 2 + '[11:00:00][no_game_date][font.cpp:1]: missing\n')
    assert any(r['status']=='candidate_only' for r in rows)
    assert any(r['status']=='shared' and r['candidate_count']==2 for r in rows)
    assert compare(old, '')[0]['status'] == 'baseline_only'
    assert signatures('') == Counter()
    print('PASS: timestamps/dates/line numbers normalized; duplicates, additions and removals preserved')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('baseline', type=Path, nargs='?')
    parser.add_argument('candidate', type=Path, nargs='?')
    parser.add_argument('--self-test', action='store_true')
    parser.add_argument('--json', action='store_true', help='JSON to stdout; does not write files')
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if args.baseline is None or args.candidate is None:
        parser.error('baseline and candidate log paths are required')
    rows = compare(args.baseline.read_text(encoding='utf-8-sig', errors='replace'),
                   args.candidate.read_text(encoding='utf-8-sig', errors='replace'))
    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
    else:
        for row in rows:
            print(f"{row['status']} MD={row['baseline_count']} MD+VIE={row['candidate_count']} {row['signature']}")
        print('Shared diagnostics are observed in both sessions; candidate-only does not by itself prove VIE causation.')


if __name__ == '__main__':
    main()
