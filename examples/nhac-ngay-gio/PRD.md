# PRD: Nhắc ngày giỗ

Phiên bản: v1.0 · Ngày: 03/11/2026 · Người viết: PM · Trạng thái: Đã duyệt

## 1. Bối cảnh và vấn đề

Con cháu ở xa quê hay quên ngày giỗ vì ngày giỗ tính theo âm lịch, mỗi năm rơi vào một ngày dương lịch khác. Hiện các gia đình nhắc nhau qua nhóm Zalo, người lớn tuổi phải gọi điện từng người. App gia phả đã có ngày mất của từng người nhưng chưa dùng dữ liệu này. [GIẢ ĐỊNH] Trong 20 gia đình được phỏng vấn, 14 nói từng có người quên giỗ trong 2 năm gần đây.

## 2. Mục tiêu và chỉ số

| Mục tiêu | Chỉ số | Hiện tại | Mục tiêu sau 3 tháng |
| --- | --- | --- | --- |
| Không ai quên giỗ | % nhà chung bật nhắc cho ít nhất 1 ngày giỗ | 0% | 60% |
| Gắn kết gia đình | % ngày giỗ có ≥ 3 người bấm "Tôi sẽ về" | 0% | 30% |

## 3. Người dùng (persona)

- **Bác Hòa, 62 tuổi, trưởng tộc** — dùng điện thoại Android cỡ chữ lớn, quen Zalo, không quen menu nhiều tầng. Cần nhắc cả nhà mà không phải gọi từng người.
- **Chị Mai, 34 tuổi, sống ở TP.HCM** — bận, quê ở Nam Định. Cần biết trước đủ sớm để xin nghỉ và đặt vé.

## 4. User journey chính

1. Mở app, vào nhà chung của gia đình.
2. Thấy danh sách ngày giỗ sắp tới, tính sẵn từ ngày mất trong gia phả.
3. Bấm "Nhắc tôi" ở một ngày giỗ.
4. Nhận thông báo trước 7 ngày và trước 1 ngày.
5. Bấm "Tôi sẽ về" để cả nhà biết.

## 5. Tính năng

| # | Tính năng | Ưu tiên | Ghi chú |
| --- | --- | --- | --- |
| 1 | Danh sách ngày giỗ tính từ ngày mất âm lịch trong gia phả | MUST | |
| 2 | Đổi ngày giỗ âm lịch sang dương lịch cho từng năm | MUST | Gồm tháng thiếu, tháng nhuận |
| 3 | Bật nhắc, thông báo trước 7 ngày và 1 ngày | MUST | |
| 4 | Báo "Tôi sẽ về" | SHOULD | |
| 5 | Ghi đóng góp tiền / lễ vật | COULD | |
| 6 | Livestream buổi giỗ | WON'T | Bản sau |

## 6. Ngoài phạm vi

- Thanh toán online cho đóng góp.
- Ngày giỗ của người không có trong gia phả.

## 7. Giả định cần kiểm chứng

| Giả định | Cách kiểm | Dấu hiệu đúng / sai |
| --- | --- | --- |
| G1: người lớn tuổi tự bật được nhắc cho một ngày giỗ trong 1 phút | Prototype, test 5 người 55–70 tuổi | Đúng nếu ≥ 4/5 tự làm xong ≤ 60 giây |
| G2: người ở xa muốn báo "Tôi sẽ về" | Hỏi sau nhiệm vụ trong buổi test | Đúng nếu ≥ 3/5 nói sẽ dùng |

## 8. Ràng buộc và yêu cầu phi chức năng

- Thời gian: 4 tuần, 1 dev Flutter + 1 dev backend · Nền tảng: iOS, Android
- Thông báo vẫn đến khi app không mở; giờ nhắc theo giờ Việt Nam
- Cỡ chữ lớn, vùng chạm ≥ 48dp vì nhiều người dùng lớn tuổi
- Dữ liệu ngày mất là dữ liệu cá nhân của người đã mất và gia đình; chỉ thành viên nhà chung xem được

## 9. Câu hỏi mở

| Câu hỏi | Ai trả lời | Hạn |
| --- | --- | --- |
| Người mất vào tháng nhuận thì giỗ tháng nhuận hay tháng thường? | PM hỏi 3 trưởng tộc | 10/11/2026 |
| Nhiều nhánh cùng giỗ một người thì hiện một hay nhiều mục? | PM | 10/11/2026 |
