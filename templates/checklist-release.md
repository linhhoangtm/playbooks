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

Chi tiết từng mục và cách test: [guide test, mục 11.2](../guides/claude-test-web-mobile.md#112-rủi-ro-bị-app-store--google-play-từ-chối).

**Tài khoản và quyền riêng tư**

- [ ] Phần không cần tài khoản dùng được khi chưa đăng nhập (Apple 5.1.1(v))
- [ ] Xóa tài khoản trong app (và link web cho Google Play)
- [ ] Privacy policy có link ở App Store Connect / Play Console **và** trong app
- [ ] Màn đồng ý trước khi gửi dữ liệu cho AI bên thứ ba; có tracking thì hiện App Tracking Transparency
- [ ] Có đăng nhập Google / Facebook → có lựa chọn đăng nhập bảo vệ quyền riêng tư tương đương (vd Sign in with Apple, guideline 4.8)
- [ ] Permission khai báo đều dùng thật, mô tả rõ ràng; từ chối quyền thì app vẫn dùng được phần còn lại
- [ ] Android: chọn ảnh bằng Photo Picker, không xin `READ_MEDIA_*` nếu không cần; foreground service khai báo đúng loại
- [ ] Data safety / App Privacy khớp dữ liệu app thực gửi (đối chiếu network log)

**Nội dung và tính năng**

- [ ] Nội dung user tạo, chatbot AI có lọc, báo cáo, chặn; có giới hạn độ tuổi nếu cần
- [ ] Có cách liên hệ trong app, Support URL mở được
- [ ] Không bắt bật thông báo mới cho dùng; push quảng cáo có công tắc riêng
- [ ] Không có tính năng ẩn; OTA chỉ dùng để sửa lỗi

**Thanh toán**

- [ ] Nội dung số trên iOS bán qua IAP, có Restore; hàng vật lý / dịch vụ ngoài app dùng cổng thanh toán thường
- [ ] Subscription ghi rõ giá, kỳ hạn, quyền lợi, cách hủy; nâng / hạ gói không tạo gói trùng
- [ ] Xin đánh giá qua API hệ thống, không popup tự làm

**Nộp bản**

- [ ] Ảnh chụp cho thấy app đang dùng, dữ liệu giả; age rating khai đúng; "Có gì mới" mô tả thay đổi thật
- [ ] Target API Android đạt yêu cầu hiện hành; bản đầu của tài khoản cá nhân mới đã qua closed test 12 người / 14 ngày
- [ ] Demo account dùng được, không cần OTP; gói IAP đã cấu hình; backend chạy suốt thời gian review
- [ ] Review Notes đã cập nhật; lỗi cũ trong `docs/store-review.md` không lặp lại
