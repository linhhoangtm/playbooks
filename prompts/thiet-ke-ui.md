# Prompt: thiết kế UI/UX

Dùng được trong Claude chat, Claude Design hoặc Claude Code (khi làm UI bằng code). Chi tiết: [Dùng Claude làm prototype cho Designer, BA, PM](../guides/claude-lam-prototype.md).

## Design system

```
Tạo design system cho <tên sản phẩm> — <cảm giác: vd trang nhã, trẻ trung, dễ đọc cho người lớn tuổi>.
Gồm: bảng màu (primary, neutral, success / warning / error, cả dark mode), font hỗ trợ tiếng Việt đủ dấu,
thang cỡ chữ, spacing 4/8, bo góc, component: button, input, card, list item, tab bar, dialog, toast, empty state.
Contrast đạt WCAG AA, vùng chạm ≥ 44pt (iOS) / 48dp (Android). Theo repo / ảnh đính kèm nếu có.
```

## Wireframe

```
Từ danh sách màn S-01…S-xx và user flow (đính kèm), vẽ wireframe xám cho <mobile 390×844 / desktop 1440>:
chỉ bố cục, nội dung thật từ dữ liệu mẫu, không màu, không ảnh.
Mỗi màn ghi ID + story liên quan. Cho 2 phương án bố cục khác hẳn nhau cho màn <quan trọng nhất>.
```

## Mockup nhiều hướng

```
Áp design system vào wireframe đã chọn. Làm 3 hướng thị giác khác nhau cho màn <S-01>
(vd: tối giản / ấm áp / hiện đại nhiều màu). Mỗi hướng 1 dòng ưu / nhược.
Chưa làm các màn khác, chờ mình chọn.
```

## Prototype tương tác

```
Nối các màn thành prototype bấm được theo user flow:
- nhập liệu thật được, có validate và thông báo lỗi theo acceptance criteria
- mỗi màn có 4 trạng thái: loading, có dữ liệu, rỗng, lỗi (có nút nhỏ để chuyển trạng thái khi demo)
- quay lại, hủy, xác nhận hoạt động đúng
- dữ liệu lấy từ JSON mẫu, đổi JSON là màn đổi theo
Chỉ làm các màn phục vụ <giả định cần test>.
```

## Viết nội dung trên màn hình (UX writing)

```
Viết lại toàn bộ chữ trên màn <tên> (tiêu đề, nút, placeholder, thông báo lỗi, empty state) bằng tiếng Việt:
ngắn, xưng hô <bạn / anh chị / không xưng>, nút là động từ, lỗi nói rõ chuyện gì và làm gì tiếp.
Bảng: vị trí | chữ cũ | chữ mới | lý do.
```

## Tự rà UI/UX

```
Rà <ảnh chụp / prototype / file UI> theo: 10 heuristic của Nielsen, contrast, vùng chạm,
text tiếng Việt dài bị cắt, cỡ chữ phóng to 200%, màn nhỏ 360×640, dark mode, thao tác một tay, đủ 4 trạng thái.
Bảng: màn | vấn đề | mức (cao / vừa / thấp) | cách sửa. Nếu là file UI sửa được thì sửa luôn mục mức cao.
```

## Chọn giả định cần test bằng prototype

```
Từ mục "Giả định" trong PRD, chọn 3 giả định rủi ro nhất có thể kiểm bằng prototype.
Với mỗi cái: màn/flow cần làm, nhiệm vụ giao cho user khi test, dấu hiệu đạt / không đạt.
Màn nào không phục vụ 3 giả định này thì đừng làm trong prototype.
```

## Kịch bản test với user

```
Viết kịch bản usability test 20 phút cho prototype (3 giả định trong Project):
- 2 câu khởi động về thói quen hiện tại của họ
- 3 nhiệm vụ viết theo tình huống thật, KHÔNG chứa tên nút/menu (vd "Tháng sau là giỗ ông nội, bác muốn được nhắc trước")
- mỗi nhiệm vụ: dấu hiệu thành công, thời gian tối đa, câu hỏi sau nhiệm vụ
- 3 câu kết thúc, không hỏi "bác có thích không"
- lời dặn cho người dẫn: không gợi ý, không giải thích, hỏi "bác đang nghĩ gì?"
```

## Tổng hợp sau test với user

```
Đây là ghi chép 5 phiên test (đã bỏ tên thật): <dán ghi chép hoặc transcript>.
Gom thành bảng: vấn đề | màn | số người gặp (x/5) | mức (chặn / khó chịu / nhỏ) | trích dẫn ngắn | đề xuất sửa.
Sắp xếp theo mức rồi số người. Chỉ đưa vào điều thấy trong ghi chép, không suy diễn.
Kết luận từng giả định: đúng / sai / chưa rõ.
```

## Từ ảnh chụp ra code

```
Đây là ảnh màn hình thiết kế. Dựng lại bằng <Flutter / React Native / React + Tailwind>,
dùng component có sẵn trong repo (đọc thư mục <components>) trước khi tạo mới.
Đủ 4 trạng thái. Chữ lấy từ file i18n nếu repo có. Liệt kê chỗ ảnh không rõ thay vì tự đoán.
```
