"""Export a self-contained paper design; no mod or engine assets are included."""
import argparse
from pathlib import Path
import re
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    'VIETNAM_POLITICAL_FOCUS_DESIGN_VI.md',
    'VIETNAM_POLITICAL_REVIEW_L3_VI.md',
    'VIETNAM_POLITICAL_PARAMETERS_VI.json',
    'VIETNAM_POLITICAL_BALANCE_VI.py',
    'VIETNAM_POLITICAL_CROSSCHECK_VI.py',
    'VIETNAM_POLITICAL_CONSUMERS_VI.py',
    'VIETNAM_POLITICAL_BALANCE_VI.csv',
    'VIETNAM_POLITICAL_I5_EXCEPTIONS_VI.csv',
    'VIETNAM_POLITICAL_NODE_CHOICES_VI.csv',
    'VIE_political_v57_implementation.md',
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/'artifacts'/'vietnam-political-design.zip')
    args = parser.parse_args()
    for name in FILES:
        if not (ROOT/name).is_file():
            raise SystemExit(f'Missing package source: {name}')
        if name.endswith('.md'):
            content = (ROOT/name).read_text(encoding='utf-8')
            for link in re.findall(r'\]\(([^)]+)\)', content):
                if '://' not in link and not link.startswith('#') and link.split('#')[0] not in FILES:
                    raise SystemExit(f'Unpackaged link in {name}: {link}')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(args.output, 'w', ZIP_DEFLATED) as package:
        for name in FILES:
            package.write(ROOT/name, name)
        package.writestr('README.md',
            '# Thiết kế chính trị Việt Nam\n\n'
            'Giải nén cả gói vào cùng thư mục. Cần Python 3 (chỉ thư viện chuẩn); không cần HOI4.\n\n'
            'Đọc VIETNAM_POLITICAL_FOCUS_DESIGN_VI.md và VIETNAM_POLITICAL_REVIEW_L3_VI.md.\n'
            'Chạy: python VIETNAM_POLITICAL_BALANCE_VI.py --audit-l3\n'
            'Chi tiết probe: thêm --audit-json. Đồng bộ bảng: thêm --sync-approved.\n'
            'JSON tham số và cả hai script đi kèm. REVIEW_L1/L2 không phải phụ thuộc.\n'
            'CSV ngân sách chỉ có tổ hợp hợp lệ; E103 tự động, không có lựa chọn A/B/C. Ca khóa lịch ở CSV ngoại lệ I5 và probe audit.\n'
            'Đây là mô hình giấy; chưa triển khai/kiểm trong game.\n')
    with ZipFile(args.output) as package:
        if package.testzip() is not None:
            raise SystemExit('ZIP validation failed')
    print(f'{args.output}: {len(FILES)} sources + README; all local document links included')


if __name__ == '__main__':
    main()
