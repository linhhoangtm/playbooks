# Design system: <tên sản phẩm>

Cập nhật: <dd/mm/yyyy> · Nguồn: <link Claude Design / Figma> · Cảm giác: <vd trang nhã, dễ đọc cho người lớn tuổi>

<!-- Dev và Claude Code dùng file này để tạo theme và component dùng chung. Mọi màn chỉ dùng token, không hardcode màu / cỡ chữ. -->

## Màu

| Token | Light | Dark | Dùng cho |
| --- | --- | --- | --- |
| `primary` | <#...> | <#...> | Nút chính, link |
| `on-primary` | <#...> | <#...> | Chữ trên nền primary |
| `surface` | <#...> | <#...> | Nền màn |
| `on-surface` | <#...> | <#...> | Chữ chính |
| `muted` | <#...> | <#...> | Chữ phụ, viền |
| `success` / `warning` / `error` | <...> | <...> | Trạng thái |

Contrast chữ / nền đạt WCAG AA (≥ 4,5:1 chữ thường, ≥ 3:1 chữ lớn): <đã kiểm bằng công cụ ...>.

## Chữ

Font: <tên, hỗ trợ đủ dấu tiếng Việt> · Cỡ chữ theo thang, đổi theo cài đặt cỡ chữ hệ thống.

| Token | Cỡ / dòng | Đậm | Dùng cho |
| --- | --- | --- | --- |
| `display` | <32/40> | <600> | Tiêu đề lớn |
| `title` | <20/28> | <600> | Tiêu đề màn |
| `body` | <16/24> | <400> | Nội dung |
| `caption` | <13/18> | <400> | Chú thích |

## Khoảng cách, bo góc, đổ bóng

- Spacing: 4 · 8 · 12 · 16 · 24 · 32
- Bo góc: <sm 4 · md 8 · lg 16>
- Vùng chạm tối thiểu: 44pt (iOS) / 48dp (Android)

## Component

| Component | Biến thể | Trạng thái | Ghi chú |
| --- | --- | --- | --- |
| Button | primary, secondary, text, destructive | default, pressed, disabled, loading | Nhãn là động từ |
| Input | text, number, password, multiline | default, focus, error, disabled | Lỗi hiện dưới ô, không xóa dữ liệu đã nhập |
| Card, list item, tab bar, dialog, toast | <...> | <...> | <...> |
| Empty state | <minh họa + 1 câu + nút hành động> | | |
| Error view | <thông báo + nút Thử lại> | | |

## Nội dung và giọng văn

- Xưng hô: <bạn / anh chị / không xưng> · Nút: động từ ngắn ("Lưu", "Nhắc tôi")
- Thông báo lỗi: nói chuyện gì xảy ra + làm gì tiếp, không đổ lỗi cho người dùng
- Số tiền: `1.250.000 ₫` · Ngày: `dd/mm/yyyy` · Giờ: 24h

## Icon và hình ảnh

<Bộ icon, kích thước chuẩn, phong cách minh họa, ảnh có alt text.>
