# Release <phiên bản> — <dd/mm/yyyy>

<!-- Hai bản cùng một file. Bản người dùng dán vào "Có gì mới" trên App Store / Google Play (≤ 500 ký tự). -->

## Cho người dùng

- <Động từ + lợi ích, không thuật ngữ: "Nhắc ngày giỗ theo âm lịch, báo trước 7 ngày">
- <...>
- Sửa lỗi và cải thiện tốc độ.

## Cho team

**Tính năng:** <PR / issue>
**Sửa lỗi:** <PR / issue>
**Kỹ thuật:** <refactor, nâng thư viện, đổi hạ tầng>

**Cần làm khi deploy**

- Migration: <tên migration, có khóa bảng lâu không, cách rollback>
- Biến môi trường / cấu hình mới: <tên — giá trị ở production do ai đặt>
- Thứ tự deploy: <API trước, app sau / tương thích ngược với app bản cũ đến khi nào>

**Rủi ro và theo dõi:** <chỉ số / log cần xem trong 24 giờ đầu>

**Rollback:** <cách quay lại bản trước; dữ liệu đã migrate xử lý thế nào>
