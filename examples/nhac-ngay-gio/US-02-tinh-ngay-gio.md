# US-02 Xem ngày giỗ dương lịch của năm nay

**Là** thành viên nhà chung, **tôi muốn** thấy ngày giỗ năm nay đã đổi sang dương lịch, **để** sắp xếp về quê mà không phải tự tra lịch âm.

Ưu tiên: MUST · Màn liên quan: S-01, S-02 · Quy tắc: BR-01, BR-02, BR-03

## Acceptance criteria

### Happy path
- **Given** ông A mất ngày 15/3 âm lịch **When** mở danh sách ngày giỗ năm 2027 **Then** thấy "Giỗ ông A — 15/3 âm lịch — Thứ Tư, 21/04/2027"
- **Given** có 3 ngày giỗ trong năm **When** mở danh sách **Then** sắp xếp theo ngày dương lịch gần nhất trước, ngày đã qua của năm nay nằm cuối và mờ

### Input sai
- **Given** ngày mất trong gia phả là 31/2 âm lịch (dữ liệu nhập sai) **When** tính ngày giỗ **Then** không crash, hiện "Ngày mất chưa hợp lệ — Sửa" cho người có quyền sửa (VR-01)

### Không có quyền
- **Given** người dùng không phải thành viên nhà chung **When** mở link ngày giỗ được chia sẻ **Then** thấy màn "Bạn chưa thuộc gia đình này", không thấy tên người mất
- **Given** thành viên không phải trưởng tộc **When** xem chi tiết ngày giỗ **Then** không thấy nút sửa ngày mất

### Dữ liệu trống
- **Given** gia phả chưa có ai có ngày mất **When** mở danh sách **Then** hiện hướng dẫn "Thêm ngày mất trong gia phả để nhận nhắc giỗ" và nút đi tới gia phả
- **Given** người mất chỉ có năm mất, không có ngày tháng **When** mở danh sách **Then** người đó không xuất hiện, cuối danh sách ghi "2 người chưa có ngày mất đầy đủ"

### Giá trị biên
- **Given** ông B mất ngày 30 tháng Chạp **When** năm âm lịch đó tháng Chạp chỉ có 29 ngày **Then** giỗ vào 29 tháng Chạp, hiện ghi chú "Tháng Chạp năm nay thiếu, giỗ vào ngày 29" (BR-02)
- **Given** ngày giỗ năm nay đã qua **When** mở danh sách vào ngày hôm sau **Then** hiện ngày giỗ của năm sau ở mục "Sắp tới"
- **Given** ngày giỗ rơi vào 01/01 dương lịch **When** đang là 31/12 lúc 23:59 **Then** vẫn hiện "Ngày mai"

### Bổ sung: lỗi hệ thống và đồng thời
- **Given** mất mạng và chưa có cache **When** mở danh sách **Then** hiện lỗi kèm nút Thử lại; có cache thì hiện dữ liệu cũ kèm dòng "Cập nhật lúc …"

## Ghi chú

- Câu hỏi mở về tháng nhuận: Q-01 trong [ban-giao.md](ban-giao.md#12-câu-hỏi-mở).
- Dữ liệu mẫu: `fixtures/ngay-gio.json` có ca tháng thiếu, tháng nhuận, chỉ có năm mất.
