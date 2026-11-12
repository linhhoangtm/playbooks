# <Tên dự án>

<!--
Mẫu CLAUDE.md cho Claude Code. Giữ ngắn (dưới ~150 dòng): Claude đọc file này mỗi phiên.
Chỉ ghi điều Claude KHÔNG tự đoán được từ code. Mỗi lần Claude làm sai, thêm 1 dòng quy tắc.
Xóa các comment này sau khi điền.
-->

<1–2 câu: sản phẩm là gì, cho ai.>

## Stack

- <Flutter 3.x / React Native (Expo) / Next.js / Go / FastAPI…>
- DB: <PostgreSQL / MySQL / SQL Server> · ORM / query: <…>
- State / DI: <…>
- Offline / cache: <…>

## Cấu trúc

- `<thư mục>` — <vai trò>
- `<thư mục>` — <vai trò>
- Tài liệu: `docs/` (PRD, ADR, `docs/features/<ten>.md` cho từng tính năng)

## Lệnh

- Chạy dev: `<lệnh>`
- Format: `<lệnh>`
- Lint / analyze: `<lệnh>`
- Typecheck: `<lệnh>`
- Test: `<lệnh>` · 1 file: `<lệnh> <đường dẫn>`
- E2E: `<lệnh>` (cần <emulator / dev server>)
- Migration: `<lệnh>` (chỉ local)

## Quy ước

- Đặt tên: <file, class, biến, API: snake_case / camelCase…>
- Chữ trên UI: tiếng Việt, lấy từ <file i18n>; không hardcode
- Mỗi màn có đủ 4 trạng thái: loading, có dữ liệu, rỗng, lỗi
- Lỗi API: <format>; luôn hiển thị thông báo người dùng hiểu được
- Test: <thư viện>; test mới đặt ở <thư mục>; mỗi bug sửa xong có 1 test tái hiện
- Mỗi tính năng xét đủ 5 nhóm test: happy path, input sai, không có quyền, dữ liệu trống, giá trị biên
- Test fail: báo nguyên nhân, không sửa code hay nới lỏng assert chỉ để pass
- Integration test dùng DB thật (vd Testcontainers), không mock database
- Kiểm quyền ở server cho mọi endpoint: đăng nhập + dữ liệu thuộc về user + role
- Token / secret trên máy lưu bằng secure storage, không ghi vào log

## Không được làm

- Không tự commit / push. Làm xong: báo file đã đổi + cách thử, chờ duyệt.
- Không thêm hoặc nâng dependency khi chưa hỏi.
- Không đọc / sửa: `.env*`, `<file khóa, keystore, cấu hình production>`.
- Không chạy migrate / seed vào DB không phải local.
- Không sửa code không liên quan đến task.
- Các điều cấm trên được chặn cứng thêm trong `.claude/settings.json`; bị chặn thì hỏi, không tìm cách vòng.

## Sau mỗi thay đổi

1. Format + lint + test liên quan, báo kết quả.
2. Đổi API dùng chung với app khác → chạy thêm `<lệnh regression>`.
3. Ghi quyết định lớn vào `docs/adr/`.

## Ghi chú / bẫy đã gặp

- <vd: hàm X trả về ngày theo UTC, hiển thị phải đổi sang giờ VN>
