# Công cụ bố cục focus (chuẩn: VIE_focus_coding_standards.md mục 7.3)

Chạy từ gốc repo. Cần `matplotlib` cho hai script render (đặt `OPENBLAS_NUM_THREADS=1` nếu báo lỗi cấp phát bộ nhớ).

| Script | Việc |
|---|---|
| `reanchor.py` | Neo mọi focus vào một tiền đề của chính nó mà KHÔNG đổi vị trí tuyệt đối (có kiểm tra đồng nhất). |
| `relayout.py <out.json> <root_id>...` | Tính bố cục ngang mới cho các nhánh (làm phẳng chuỗi dọc từ 3 focus, xếp hàng theo tầng, dịch tới chỗ trống). Chế độ `RELAYOUT_MODE=bary` (mặc định) hoặc `keep`. Chỉ tính, chưa ghi file focus. |
| `tidy_layout.py <plan.json> [--skip-prefix P] [--start X]` | Bố cục kiểu chính trị cho mọi nhánh (xem docstring). Chỉ tính; ghi bằng `apply_plan.py`. |
| `metrics.py` | So sánh số hàng, bề ngang, số điểm giao đường nối và tổng độ dài đường nối trước và sau cho từng nhánh. Chỉ áp dụng khi chỉ số tốt hơn. |
| `apply_plan.py <plan.json>` | Ghi kế hoạch vào `VIE_md_focus.txt` (dừng nếu có ô trùng hoặc khoảng cách dưới 2). |
| `render_tree.py x0 x1 y0 y1 out.png` | Vẽ cây hiện tại. |
| `render_plan.py plan.json out.png` | Vẽ kế hoạch trước khi áp dụng. |

Sau mỗi lần áp dụng: `python tools/check_static.py` phải giữ nguyên 90 lỗi nền.
