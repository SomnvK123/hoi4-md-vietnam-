# Trung–Nhật — dữ liệu trích từ code

Chỉ kiểm cấu trúc; không mô phỏng HOI4.

| Mã | ID thật | Cost | Anchor | x/y tương đối | X/Y tuyệt đối | Prerequisite (AND giữa nhóm, OR trong nhóm) |
|---|---|---:|---|---|---|---|
| J01 | CHI_the_japan_question | 5 | CHI_Chinese_Diplomacy | (28,1) | (83,1) | (CHI_Chinese_Diplomacy) |
| J02 | CHI_the_historical_reckoning | 7 | J01 | (-3,1) | (80,2) | (J01) |
| J03 | CHI_the_nanjing_memorial_mandate | 3 | J02 | (-2,1) | (78,3) | (J02) |
| J04 | CHI_the_diaoyu_sovereignty_declaration | 5 | J02 | (0,1) | (80,3) | (J02) |
| J05 | CHI_the_rare_earth_lever | 3 | J02 | (2,1) | (82,3) | (J02) |
| J06 | CHI_the_yasukuni_protest_doctrine | 3 | J02 | (-2,2) | (78,4) | (J03) |
| J07 | CHI_the_maritime_militia_initiative | 3 | J02 | (0,2) | (80,4) | (J04) |
| J08 | CHI_anti_japanese_boycott_campaign | 5 | J02 | (2,2) | (82,4) | (J05) |
| J09 | CHI_the_senkaku_crisis | 7 | J02 | (0,3) | (80,5) | (J06) AND (J07) AND (J08) |
| J10 | CHI_the_fukuda_doctrine_revisited | 7 | J01 | (3,1) | (86,2) | (J01) |
| J11 | CHI_the_panda_diplomacy_renewal | 5 | J10 | (0,1) | (86,3) | (J10) |
| J12 | CHI_the_rcep_acceleration | 5 | J10 | (-2,1) | (84,3) | (J10) |
| J13 | CHI_assuage_japanese_concerns | 7 | J10 | (2,1) | (88,3) | (J10) |
| J14 | CHI_the_anime_generation_gambit | 3 | J10 | (0,2) | (86,4) | (J11) |
| J15 | CHI_the_china_plus_one_counteroffensive | 5 | J10 | (-2,2) | (84,4) | (J12) |
| J16 | CHI_the_quad_wedge_strategy | 5 | J10 | (2,3) | (88,5) | (J13) AND (J14) |
| J17 | CHI_the_tokyo_communique | 7 | J10 | (0,4) | (86,6) | (J14) AND (J15) AND (J16) |
| J18 | CHI_break_the_first_island_chain | 10 | J01 | (0,6) | (83,7) | (J17 OR J09) |

```mermaid
flowchart TD
    ROOT["Ngoại giao khu vực CHI"]
    J01["J01: the_japan_question"]
    J02["J02: the_historical_reckoning"]
    J03["J03: the_nanjing_memorial_mandate"]
    J04["J04: the_diaoyu_sovereignty_declaration"]
    J05["J05: the_rare_earth_lever"]
    J06["J06: the_yasukuni_protest_doctrine"]
    J07["J07: the_maritime_militia_initiative"]
    J08["J08: anti_japanese_boycott_campaign"]
    J09["J09: the_senkaku_crisis"]
    J10["J10: the_fukuda_doctrine_revisited"]
    J11["J11: the_panda_diplomacy_renewal"]
    J12["J12: the_rcep_acceleration"]
    J13["J13: assuage_japanese_concerns"]
    J14["J14: the_anime_generation_gambit"]
    J15["J15: the_china_plus_one_counteroffensive"]
    J16["J16: the_quad_wedge_strategy"]
    J17["J17: the_tokyo_communique"]
    J18["J18: break_the_first_island_chain"]
    ROOT -->|AND| J01
    J01 -->|AND| J02
    J02 -->|AND| J03
    J02 -->|AND| J04
    J02 -->|AND| J05
    J03 -->|AND| J06
    J04 -->|AND| J07
    J05 -->|AND| J08
    J06 -->|AND| J09
    J07 -->|AND| J09
    J08 -->|AND| J09
    J01 -->|AND| J10
    J10 -->|AND| J11
    J10 -->|AND| J12
    J10 -->|AND| J13
    J11 -->|AND| J14
    J12 -->|AND| J15
    J13 -->|AND| J16
    J14 -->|AND| J16
    J14 -->|AND| J17
    J15 -->|AND| J17
    J16 -->|AND| J17
    J17 -->|OR| J18
    J09 -->|OR| J18
    J10 -. mutex .- J02
```

Mermaid thể hiện quan hệ; vị trí vẽ tự động không là tọa độ engine. Tọa độ thật ở bảng/CSV.

## Kiểm hình học nguồn

Không áp tiêu chuẩn VIE ngược thành khẳng định nguồn MD đã đạt chuẩn.

- {"type": "anchor_not_direct_parent", "focus": "CHI_the_yasukuni_protest_doctrine", "anchor": "CHI_the_historical_reckoning"}
- {"type": "anchor_not_direct_parent", "focus": "CHI_the_maritime_militia_initiative", "anchor": "CHI_the_historical_reckoning"}
- {"type": "anchor_not_direct_parent", "focus": "CHI_anti_japanese_boycott_campaign", "anchor": "CHI_the_historical_reckoning"}
- {"type": "anchor_not_direct_parent", "focus": "CHI_the_senkaku_crisis", "anchor": "CHI_the_historical_reckoning"}
- {"type": "anchor_not_direct_parent", "focus": "CHI_the_anime_generation_gambit", "anchor": "CHI_the_fukuda_doctrine_revisited"}
- {"type": "anchor_not_direct_parent", "focus": "CHI_the_china_plus_one_counteroffensive", "anchor": "CHI_the_fukuda_doctrine_revisited"}
- {"type": "anchor_not_direct_parent", "focus": "CHI_the_quad_wedge_strategy", "anchor": "CHI_the_fukuda_doctrine_revisited"}
- {"type": "anchor_not_direct_parent", "focus": "CHI_the_tokyo_communique", "anchor": "CHI_the_fukuda_doctrine_revisited"}
- {"type": "anchor_not_direct_parent", "focus": "CHI_break_the_first_island_chain", "anchor": "CHI_the_japan_question"}
