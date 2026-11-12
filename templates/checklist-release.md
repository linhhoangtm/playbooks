# Checklist release — <phiên bản> — <dd/mm/yyyy>

## Code và test

- [ ] Lint, typecheck, unit / widget test xanh trong CI
- [ ] Regression và E2E chạy trên build release
- [ ] Tính năng mới đủ test 5 nhóm (happy path, input sai, không quyền, dữ liệu trống, giá trị biên)
- [ ] Đã review code; không còn TODO / log debug / màn "đang phát triển" hiện ra UI

## Bảo mật

- [ ] Mọi endpoint mới kiểm đăng nhập + dữ liệu thuộc về user + role
- [ ] Không có secret trong code / app; token lưu bằng secure storage
- [ ] Rate limit cho đăng nhập, OTP, đăng ký, gọi AI; quota AI theo user
- [ ] Xác minh thanh toán / receipt ở server; bấm 2 lần hoặc webhook gọi lại không trừ tiền / tạo đơn 2 lần
- [ ] Đã chạy security review, không còn mục High
- [ ] Red-team tính năng AI đã chạy với bản system prompt mới nhất

## Hiệu năng và ổn định

- [ ] Không có N+1 mới; truy vấn mới có index
- [ ] Không có leak mới (controller, subscription, listener)
- [ ] Web: Core Web Vitals đạt (LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1); app: mở lạnh < 3 giây trên máy tầm trung

## UI/UX

- [ ] Mọi màn đủ loading / có dữ liệu / rỗng / lỗi
- [ ] Text tiếng Việt dài, cỡ chữ 200%, màn nhỏ, dark mode không vỡ
- [ ] Test a11y tự động xanh (axe / Lighthouse cho web, `meetsGuideline` / label cho app)
- [ ] Đã thử trên ít nhất 1 iPhone và 1 Android thật

## Dữ liệu và vận hành

- [ ] Migration đã chạy thử trên bản sao dữ liệu; có cách rollback
- [ ] Cấu hình / biến môi trường mới đã thêm ở production
- [ ] Monitoring / alert cho tính năng mới
- [ ] Release note cho người dùng và cho team

## Quyền riêng tư và pháp lý

- [ ] Chính sách quyền riêng tư khớp dữ liệu app thực thu thập, có link trong app và trên store
- [ ] Xin đồng ý trước khi thu thập dữ liệu cá nhân không bắt buộc; rút lại đồng ý được
- [ ] Đã rà theo pháp luật bảo vệ dữ liệu cá nhân hiện hành (Luật 91/2025/QH15 và văn bản hướng dẫn), nhất là dữ liệu gửi ra nước ngoài (AI, cloud, analytics)
- [ ] App / web có bán hàng hoặc đặt hàng: đã thông báo / đăng ký với Bộ Công Thương theo quy định thương mại điện tử hiện hành

## Store (nếu là app mobile)

- [ ] Xóa tài khoản trong app (và link web cho Google Play)
- [ ] Màn đồng ý trước khi gửi dữ liệu cho AI bên thứ ba
- [ ] Có đăng nhập Google / Facebook → có lựa chọn đăng nhập bảo vệ quyền riêng tư tương đương (vd Sign in with Apple, guideline 4.8)
- [ ] Nội dung user tạo có báo cáo, chặn, lọc
- [ ] Nội dung số trên iOS bán qua IAP, có Restore
- [ ] Permission khai báo đều dùng thật, mô tả rõ ràng
- [ ] Target API Android đạt yêu cầu hiện hành
- [ ] Data safety / App Privacy khớp dữ liệu app thực gửi (đối chiếu network log)
- [ ] Demo account dùng được, không cần OTP; Review Notes đã cập nhật
