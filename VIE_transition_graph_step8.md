# Bước 8: Đồ thị chuyển chế độ với ngưỡng cụ thể

> Tiếp theo STEP 1–7. Đây là bước chốt **con số**, thứ đã bị treo từ STEP 5. **Chưa** lên kế hoạch code (STEP 9).
>
> Nhãn: **[SỰ KIỆN]** · **[HỌC THUẬT]** · **[TIỀN ĐỀ KỊCH BẢN]**

---

## 0. Kết quả trong một đoạn

Chốt được thang chuẩn hóa, **vân tay của con đường lịch sử**, và **ngưỡng cho 11 cạnh chuyển chế độ**. Phép thử quan trọng nhất đã chạy: **một người chơi đi hết con đường lịch sử không tự động mở nhánh chế độ nào** ngoài nhánh Kiến tạo — và nhánh đó vẫn bị chặn thêm bởi hai điều kiện ngoài trục. Mọi nhánh khác đòi hỏi người chơi **cố ý lệch khỏi lịch sử**, và lệch bao nhiêu thì đo được.

---

## 1. Thang chuẩn hóa

**[TIỀN ĐỀ KỊCH BẢN]** Mỗi trục quy về **−10…+10**, chia theo phạm vi đạt được **khi chưa vào dải chế độ nào** — tức là những gì người chơi làm được bằng thân lịch sử cộng nhánh quân sự. Cách chia này có lý do: ngưỡng là để **mở cửa vào** dải, nên phải đo bằng thứ đạt được **trước khi** vào.

| Trục | Tối đa dương | Tối đa âm | SPAN dùng để chia |
|---|---|---|---|
| size quy mô bộ máy | +6 | −12 | 12 |
| merit chất lượng bộ máy | +59 | 0 | 59 |
| decent phân cấp | +24 | −15 | 24 |
| checks ràng buộc | +19 | −15 | 19 |
| market thị trường | +41 | −40 | 41 |
| civil quyền dân sự | +5 | −14 | 14 |
| integ hội nhập | +98 | −26 | 98 |
| mob huy động | +12 | 0 | 12 |
| west linkage phương Tây | +29 | −6 | 29 |

`giá trị hiển thị = round(10 × thô / SPAN)`, cắt ở ±10.

**[HỌC THUẬT]** Hai trục có phạm vi rất lệch — `merit` và `integ` chỉ đi một chiều, đúng như STEP 6 đã phát hiện. Điều đó không phải lỗi thang đo mà là đặc điểm thật của lịch sử Việt Nam 2000–2026.

---

## 2. Vân tay của con đường lịch sử

**[SỰ KIỆN]** Đi hết thân lịch sử và nhánh quân sự, không rẽ nhánh nào:

| merit | integ | west | civil | mob | decent | checks | size | market |
|---|---|---|---|---|---|---|---|---|
| **+10** | **+7** | **+8** | **−10** | +5 | +4 | +3 | −2 | 0 |

Đọc bằng lời: **bộ máy được làm sạch tới mức tối đa, hội nhập rất sâu và nghiêng phương Tây, quyền dân sự bị siết gần kịch trần, năng lực huy động quần chúng cao nhưng do nhà nước kiểm soát, phân cấp và ràng buộc quyền lực nhích lên một chút, nhà nước và thị trường cân bằng.**

**[HỌC THUẬT]** Đây là một mô tả trung thực về Việt Nam 2026, và nó rơi ra từ mô hình chứ không được đặt vào.

**Một lưu ý về `mob`:** giá trị +5 không có nghĩa là đường phố sôi sục. Nó đo **năng lực huy động có tổ chức** — Mặt trận, dân quân tự vệ, đoàn thanh niên, hội cựu chiến binh. Theo Linz, thứ nguy hiểm không phải huy động mà là **huy động ngoài tầm kiểm soát của nhà nước**. Vì vậy `mob` cao chỉ thành nguy hiểm khi đi kèm `checks` thấp và một sự kiện làm mất kiểm soát. Đó là điều kiện ghép, không cần thêm biến.

---

## 3. Đồ thị chuyển

**[TIỀN ĐỀ KỊCH BẢN]** Sửa lại bản nháp ở mục XIV của bạn theo kết quả STEP 3 và STEP 7:

```
                     ĐỔI MỚI TIẾP TỤC  (slot 19, closed autocracy)
                                │
                 ─── vùng cấu hình B1/B2 ───
            (tự chủ chiến lược + phát triển chủ nghĩa dân tộc;
                     KHÔNG đổi chế độ, vẫn slot 19)
                                │
      ┌──────────────┬──────────┼───────────┬──────────────┐
      │              │          │           │              │
  market thấp    merit cao   mob cao    civil rất thấp  market cao
  integ thấp     + tổn thương + checks    + checks thấp   + decent cao
      │          hệ thống      thấp          │              │
      ▼              ▼          ▼            ▼              ▼
  BẢO THỦ (4)   KIẾN TẠO (19)  DÂN TÚY(20)  AN NINH (7)  ĐẶC KHU (16)
                     │             │                          │
              merit≥7,civil≥−6     │                    merit không
              checks≥5             │                    theo kịp market
                     │      ┌──────┴──────┐                   │
                     ▼      ▼             ▼                   ▼
            ĐA ĐẢNG CÓ   JUNTA (22)   LẠC HỒNG (21)      TÀI PHIỆT (15)
            KIỂM SOÁT     mob≥9        mob≥9, checks≤−5        │
                     │    quân đội     + 2/3 điều kiện    merit tiếp tục
                     ▼    can thiệp      cấu trúc          sụp đổ
              DÂN CHỦ (1/2/14/18)  │           │                │
              — lối vào "thế mạnh" │           ▼                ▼
                                   │      thoái hóa thành  ┌─────────┐
                     ┌─────────────┘      độc đoán thường  │ SỤP ĐỔ  │
                     ▼                                     └────┬────┘
            HỘI ĐỒNG PHÁT TRIỂN (0)                             │
            west≥6, merit≥5, checks≤−4              ┌───────┬────┴───┬────────┐
                     │                              ▼       ▼        ▼        ▼
                     ▼ "khoảnh khắc 1987"        JUNTA  QUÂN CHỦ  DÂN CHỦ  ĐOÀN KẾT
              DÂN CHỦ — lối vào "thế mạnh"                       (lối vào
                                                                 "thay thế",
                                                                  bị phạt)
```

**Ba quy luật, đều rút từ literature:**

1. **Không có cạnh nào đi thẳng từ Đổi Mới tới Lạc Hồng.** Chỉ tới được qua Dân túy, và Dân túy đòi `mob ≥ 7` mà con đường lịch sử chỉ đạt +5.
2. **Vùng B1/B2 không phải một nút.** Tự chủ chiến lược và phát triển chủ nghĩa dân tộc **không đổi chế độ** — chúng là cấu hình. Đây là sửa lớn nhất so với bản nháp của bạn.
3. **Dân chủ có hai lối vào, hai hệ quả.** "Nhượng bộ từ thế mạnh" (Slater & Wong) đi qua Đa đảng có kiểm soát; "thay thế" (O'Donnell & Schmitter) đi qua Sụp đổ và **bị phạt**.

---

## 4. Ngưỡng cho từng cạnh

**[TIỀN ĐỀ KỊCH BẢN]** Điều kiện trục **cộng thêm** cửa event hiện có, không thay thế nó. Cờ vẫn là điều kiện cần; trục là điều kiện đủ.

| Cạnh | Điều kiện trục | Điều kiện ngoài trục | Cơ sở |
|---|---|---|---|
| → **Bảo thủ** (4) | `market ≤ −2` **và** `integ ≤ +3` | Cửa D1 Đại hội IX, BoP phía bảo thủ | Đóng cửa kinh tế là dấu hiệu nhận biết, không phải khẩu hiệu |
| → **Kiến tạo** (19) | `merit ≥ +4` | **Đe dọa bên ngoài** cao **và** ngân khố eo hẹp **và** cần chính danh quần chúng | Doner, Ritchie & Slater (2005): kiến tạo bị ép ra đời |
| → **Tự chủ** (19) | `integ ≤ +4` **và** `west ≤ +4` | Cửa D4 HD-981, phản ứng cứng rắn | Kuik (2008) |
| → **Dân túy** (20) | `mob ≥ +7` **và** `checks ≤ 0` | Cửa D4, để đường phố dẫn dắt | Mudde (2004); Levitsky & Loxton (2013) |
| → **An ninh** (7) | `civil ≤ −8` **và** `checks ≤ −2` | Cửa D3 khủng hoảng trật tự | Greitens (2016) |
| → **Đặc khu** (16) | `market ≥ +5` **và** `decent ≥ +3` | Cửa D6 Luật Đặc khu 2018 | — |
| → **Tài phiệt** (15) | `merit ≤ +2` **và** `market ≥ +3` | `corruption_level ≥ 07`, faction `oligarchs` đã có | Evans (1995): mất tự chủ; Winters (2011) |
| → **Đa đảng có kiểm soát → Dân chủ** | `merit ≥ +7` **và** `civil ≥ −6` **và** `checks ≥ +5` | Tăng trưởng tốt, đảng còn tự tin | **Slater & Wong (2013): nhượng bộ từ thế mạnh** |
| → **Junta** (22) | `mob ≥ +9` | Quân đội can thiệp (đã có `vie_alt.15.a`) | Geddes et al.: quân sự **giải huy động** |
| → **Lạc Hồng** (21) | `mob ≥ +9` **và** `checks ≤ −5` | **Ít nhất 2 trong 3:** khủng hoảng chính danh đang hoạt động · một bộ phận tinh hoa đã ly khai · độc quyền bạo lực đã rạn | Paxton giai đoạn 3; Mann (2004) |
| → **Hội đồng Phát triển** (0) | `west ≥ +6` **và** `merit ≥ +5` **và** `checks ≤ −4` | Đã ở Junta hoặc An ninh, hoặc đã `pivot_to_the_west` | Mô hình Park Chung-hee: kiến tạo **cộng** độc đoán |

**[HỌC THUẬT] Hai ngưỡng đáng giải thích:**

- **Tài phiệt đòi `merit ≤ +2`** trong khi lịch sử đạt `+10`. Nghĩa là người chơi phải **chủ động bỏ gần hết nội dung chống tham nhũng** trong suốt 25 năm. Đó đúng là điều kiện: đầu sỏ không phải thứ bạn chọn, nó là thứ xảy ra khi bạn không xây bộ máy.
- **Hội đồng Phát triển đòi `checks ≤ −4`.** Tôi thêm điều kiện này sau khi chạy thử: nếu chỉ đòi `west` và `merit` thì con đường lịch sử tự động mở nó, mà điều đó sai — Hội đồng Phát triển là chế độ **độc đoán** phát triển, nên phải phá kiểm soát ngang mới vào được.

---

## 5. Kiểm chứng: con đường lịch sử mở được gì

**[SỰ KIỆN]** Chạy vân tay lịch sử qua toàn bộ bảng ngưỡng:

| Nhánh | Kết quả | Vì sao |
|---|---|---|
| Bảo thủ | **đóng** | `integ +7` vượt xa ngưỡng ≤ +3 |
| **Kiến tạo** | **mở** | `merit +10 ≥ +4` — nhưng vẫn cần ba điều kiện tổn thương hệ thống |
| Tự chủ | **đóng** | `integ +7` và `west +8` đều quá cao |
| Dân túy | **đóng** | `mob +5 < +7`, và `checks +3 > 0` |
| An ninh | **đóng** | `civil −10` đủ, nhưng `checks +3 > −2` |
| Đặc khu | **đóng** | `market 0 < +5` |
| Tài phiệt | **đóng** | `merit +10` cách ngưỡng ≤ +2 rất xa |
| Dân chủ từ thế mạnh | **đóng** | `civil −10 < −6`: phải **cố ý nới kiểm soát** mới vào được |
| Lạc Hồng | **đóng** | thiếu cả `mob` lẫn `checks` |
| Junta | **đóng** | `mob +5 < +9` |
| Hội đồng Phát triển | **đóng** | `checks +3 > −4` |

**[HỌC THUẬT]** Kết quả này là thứ cần đạt: **10 trên 11 nhánh đóng**, và nhánh duy nhất mở là nhánh mà lịch sử thật cũng có xu hướng đi tới. Người chơi muốn nhánh khác phải trả giá bằng việc **bỏ bớt nội dung lịch sử** — và vì toàn bộ nội dung lịch sử đã chiếm trọn 45 năm của một ván 2000–2045, bỏ bớt là có thật, không phải tượng trưng.

Đáng chú ý: hàng **Dân chủ từ thế mạnh** đóng vì `civil`. Người chơi đã xây một bộ máy sạch và giàu, nhưng vẫn phải **chủ động nới kiểm soát** mới mở được cửa. Đó đúng là điều Przeworski và O'Donnell mô tả: tự do hóa là một quyết định riêng, không phải hệ quả tự động của phát triển.

---

## 6. Cạnh thất bại và đảo ngược

**[HỌC THUẬT]** STEP 3 đã chỉ ra literature nói kết cục **phổ biến nhất** của cả A lẫn C là "nửa chừng", không phải cực đoan. Bốn cạnh sau hiện **chưa có trong code**:

| Cạnh | Điều kiện | Cơ sở |
|---|---|---|
| **Lạc Hồng → độc đoán thường** | Sau N năm không chiến tranh lớn, `mob` tụt dưới ngưỡng | Paxton giai đoạn 5: mất năng lượng cách mạng, thành chế độ bảo thủ bình thường |
| **Dân chủ hóa dừng ở độc đoán cạnh tranh** | Vào được Đa đảng có kiểm soát nhưng `merit` hoặc `checks` không đạt ngưỡng | Levitsky & Way: đây là kết cục phổ biến nhất |
| **Kiến tạo → Tài phiệt** | `market` tăng nhanh hơn `merit`, khoảng cách vượt một ngưỡng | **Evans (1995): gắn kết cao mà tự chủ thấp thì bị bắt cóc.** Đây là cạnh quan trọng nhất còn thiếu |
| **Bất kỳ → Sụp đổ** | Stability dưới ngưỡng, ≥2 khủng hoảng, trục ở cực | Đã có trong plan v6, chưa nối vào trục |

**[TIỀN ĐỀ KỊCH BẢN]** Cạnh thứ ba đáng làm nhất. Nó biến toàn bộ luận điểm Evans thành một luật chơi: *nếu bạn mở thị trường nhanh hơn tốc độ xây bộ máy, bạn không được nhà nước kiến tạo, bạn được tài phiệt.* Và nó giải thích vì sao Đặc khu dẫn tới Tài phiệt — Đặc khu cho `market +26` mà không cho `merit` điểm nào.

---

## 7. Thay đổi so với code hiện tại

**[SỰ KIỆN]** Hiện nay 16 gốc dải mở bằng cờ do event đặt (`VIE_developmental_unlocked`, `VIE_oligarch_unlocked`…), không đọc gì khác.

**[TIỀN ĐỀ KỊCH BẢN]** Thay đổi là **thêm vào `available`**, không xóa cờ:

```
available = {
    has_country_flag = VIE_oligarch_unlocked      # giữ nguyên: cửa event
    check_variable = { VIE_ax_merit < 2 }         # thêm: điều kiện cấu hình
    check_variable = { VIE_ax_market > 3 }
    has_idea = corruption_level_07                # hoặc cao hơn
}
```

Nghĩa là: **cửa event mở cơ hội, cấu hình quyết định bạn có đi được hay không.** Không focus nào bị xóa, không ID nào đổi, không cờ nào mất tác dụng.

---

## 8. Còn thiếu

| Việc | Ghi chú |
|---|---|
| **Ngưỡng cho cạnh thất bại** | Bốn cạnh ở mục 6 mới có điều kiện định tính, chưa có số |
| **Ba điều kiện tổn thương hệ thống** | "Đe dọa bên ngoài", "ngân khố eo hẹp", "cần chính danh quần chúng" chưa quy ra biến game cụ thể |
| **Ba điều kiện cấu trúc của Lạc Hồng** | "Khủng hoảng chính danh", "tinh hoa ly khai", "rạn độc quyền bạo lực" chưa có cách đo |
| **Cái giá Geddes cho `merit`** | Thiết kế ở STEP 6, chưa vào file dữ liệu, nên `merit` vẫn quá dễ lên |
| **Thử đổi `bureau_law` bằng focus** | **Nợ từ STEP 5**, vẫn chặn phần quyết định lặp lại |
| **Quan hệ dân sự – quân sự Việt Nam** | **Nợ từ STEP 3**, cần cho ngưỡng Junta — hiện `mob ≥ 9` là suy ra, không có nguồn Việt Nam |

---

## Nguồn

Doner, Ritchie & Slater (2005) *International Organization* 59(2); Slater & Wong (2013) *Perspectives on Politics* 11(3); Evans (1995) *Embedded Autonomy*; Winters (2011) *Oligarchy*; Paxton (2004) *The Anatomy of Fascism*; Mann (2004) *Fascists*; Mudde (2004); Levitsky & Loxton (2013); Levitsky & Way (2010); Geddes, Wright & Frantz (2014); Greitens (2016); O'Donnell & Schmitter (1986); Przeworski (1991); Linz (2000); Kuik (2008).

Dữ liệu mod: `D:\HOI4Mods\_gen\axis_map.py`, `axis_map_mil_alt.py`. Vân tay lịch sử và bảng kiểm chứng ngưỡng đều tính từ hai file này.
