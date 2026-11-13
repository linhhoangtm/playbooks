# <US-01> <Tên story ngắn>

**Là** <vai>, **tôi muốn** <việc>, **để** <lợi ích>.

Ưu tiên: <MUST / SHOULD / COULD> · Màn liên quan: <S-01, S-02> · Quy tắc: <BR-01>

## Acceptance criteria

<!-- Xét đủ 5 nhóm; nhóm nào không áp dụng ghi N/A kèm lý do. Quá 10 criteria thì tách story. -->

### Happy path

- **Given** <bối cảnh> **When** <hành động> **Then** <kết quả>

### Input sai

- **Given** <...> **When** <nhập sai: rỗng, sai format, quá dài, ký tự đặc biệt> **Then** <thông báo lỗi cụ thể, không mất dữ liệu đã nhập>

### Không có quyền

- **Given** <chưa đăng nhập / user khác / role thấp> **When** <...> **Then** <chuyển đăng nhập / 403 / không thấy nút>

### Dữ liệu trống

- **Given** <chưa có dữ liệu / API trả rỗng / offline> **When** <...> **Then** <empty state có hướng dẫn, không crash>

### Giá trị biên

- **Given** <0, max, max+1, ngày 29/02, cuối tháng, trang cuối…> **When** <...> **Then** <...>

### Bổ sung: lỗi hệ thống và đồng thời
<!-- Chỉ khi story có gọi mạng hoặc ghi dữ liệu; không áp dụng thì xóa mục này. -->
- **Given** <mất mạng / server lỗi / đang gửi> **When** <bấm Lưu, bấm 2 lần, người khác vừa sửa> **Then** <không mất dữ liệu, không tạo trùng, báo xung đột>

## Ghi chú

- <Câu hỏi mở, link thiết kế, dữ liệu mẫu>
