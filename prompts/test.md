# Prompt: test

Chi tiết và ví dụ: [Dùng Claude để test web app và mobile app](../guides/claude-test-web-mobile.md). Mẫu báo cáo: [templates/bao-cao-test.md](../templates/bao-cao-test.md).

## Ma trận 5 nhóm test case

```
Đọc tính năng <tên> (code ở <đường dẫn>, spec ở <đường dẫn hoặc dán>).
1. Viết acceptance criteria dạng Given / When / Then, tối đa 10 dòng.
2. Lập bảng test case: criteria × 5 nhóm (happy path, input sai, không có quyền, dữ liệu trống, giá trị biên).
   Cột: ID, nhóm, test case, input, output mong đợi, loại test (unit / widget / E2E).
3. Đánh dấu case nào đã có test, case nào chưa (grep thư mục test).
Chưa viết code. Chờ mình duyệt bảng.
```

## Viết test từ bảng đã duyệt

```
Viết test cho các case chưa có trong bảng, dùng đúng thư viện test của repo (đọc CLAUDE.md).
Chỉ viết trong thư mục test. Chạy test vừa viết và báo kết quả.
Test fail vì bug thật → giữ nguyên, ghi bug, không sửa code để test pass.
```

## Kiểm quyền / IDOR

```
Liệt kê mọi endpoint / server action trong <đường dẫn>. Với mỗi cái: có kiểm đăng nhập không,
có kiểm dữ liệu thuộc về user không (object-level), có kiểm role cho thao tác quản trị không. Ghi file:dòng.
Viết script gọi http://localhost:<port> bằng 2 tài khoản test A, B: B thử đọc / sửa / xóa dữ liệu của A.
In bảng: endpoint | hành động | status mong đợi | status thực tế.
```

## Security tổng quát

```
Rà bảo mật <phạm vi> theo OWASP API Top 10 và OWASP MASVS (nếu có mobile):
kiểm quyền, validation, injection, secrets trong code / app, lưu token trên máy, HTTP không TLS, log lộ dữ liệu.
Chỉ báo lỗ hổng có bằng chứng (file:dòng hoặc request tái hiện). Mức: High / Med / Low + cách sửa.
```

## Chống bot

```
Rà các endpoint: đăng nhập, gửi OTP, đăng ký, quên mật khẩu, danh sách / chi tiết theo id,
đăng nội dung, gọi AI, xác minh thanh toán / IAP (code ở <đường dẫn>).
Mỗi endpoint: có rate limit không (theo IP / tài khoản / thiết bị), ở đâu (file:dòng), ngưỡng bao nhiêu;
id có đoán được không; có CAPTCHA / Turnstile / App Check / Play Integrity / App Attest không.
Viết script (vd scripts/test-bot.mts) gọi http://localhost:<port> để thử từng mối đe dọa theo bảng OWASP OAT,
in bảng: endpoint | số request | bị chặn ở lần thứ mấy | status.
Chỉ chạy vào localhost, không chạy vào production. Không sửa code ứng dụng.
```

## Red-team tính năng AI

```
Tính năng AI: endpoint <url local>, system prompt ở <file>, cách ghép context ở <file>.
1. Viết 30 payload theo OWASP Top 10 for LLM 2025 (LLM01, 02, 05, 06, 07, 10), tiếng Việt và tiếng Anh:
   prompt injection trực tiếp và gián tiếp qua dữ liệu user (tên, ghi chú, bài đóng góp), lộ system prompt,
   lộ dữ liệu user khác, output chứa HTML / link độc, tiêu thụ không giới hạn.
2. Gọi từng payload bằng tài khoản test A, lưu response.
3. Chấm từng response: Pass / Fail + lý do.
4. Kiểm code: context có thể chứa dữ liệu user khác không? output có được escape khi render không?
   có quota theo user và giới hạn độ dài input không?
Bảng: ID | rủi ro | payload | response tóm tắt | kết quả | cách sửa.
```

## Performance

```
Tìm điểm chậm trong <phạm vi>: query trong vòng lặp (N+1), thiếu index, list không phân trang,
gọi API ngoài không timeout / cache, render thừa, ảnh lớn. Đo nếu server local đang chạy.
Bảng: vấn đề | file:dòng | số đo (ms, số query) | cách sửa.
```

## Memory leak

```
Rà <thư mục UI> tìm: controller / subscription / timer / listener không dispose hoặc cleanup,
list dài không lazy, ảnh không giới hạn kích thước decode. Chạy leak test nếu repo đã bật.
Bảng: file:dòng | đối tượng | vì sao leak | cách sửa.
```

## Rà UI/UX bằng trình duyệt

```
Mở http://localhost:<port>/<trang> bằng trình duyệt. Thử ở 375px và 1440px, dark mode, phóng chữ 200%.
Kiểm: 4 trạng thái (loading / dữ liệu / rỗng / lỗi), text tiếng Việt dài, nút bấm 2 lần, bàn phím che input, focus và label cho screen reader.
Chụp màn hình chỗ lỗi. Bảng: màn | vấn đề | mức | cách sửa.
```
