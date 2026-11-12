# Ví dụ: tính năng "Nhắc ngày giỗ"

Bộ tài liệu điền sẵn cho **một tính năng** đi từ PRD đến báo cáo test, để thấy các template trong [templates/](../../templates/) trông thế nào khi dùng thật và nối với nhau ra sao qua mã định danh.

> Ví dụ minh họa cho một app gia phả giả định (Flutter, backend Go, PostgreSQL). Không phải kế hoạch thật của sản phẩm nào; số liệu test user là giả định. Quy trình tạo ra bộ này: [Dùng Claude làm prototype cho Designer, BA, PM](../../guides/claude-lam-prototype.md#7-ví-dụ-tính-năng-nhắc-ngày-giỗ-cho-app-gia-phả).

| Thứ tự | File | Template gốc | Ai viết (cùng Claude) |
| --- | --- | --- | --- |
| 1 | [PRD.md](PRD.md) | [PRD.md](../../templates/PRD.md) | PM |
| 2 | [US-02-tinh-ngay-gio.md](US-02-tinh-ngay-gio.md) | [user-story.md](../../templates/user-story.md) | BA |
| 3 | [ban-giao.md](ban-giao.md) | [ban-giao-dev.md](../../templates/ban-giao-dev.md) | BA + Designer, sau 2 vòng test user |
| 4 | [bao-cao-test.md](bao-cao-test.md) | [bao-cao-test.md](../../templates/bao-cao-test.md) | Dev / QA, sau khi code |

Theo dõi hai sợi chỉ xuyên suốt qua mã định danh:

- **Tháng thiếu:** bước rà thiếu sót phát hiện ca "mất ngày 30" → acceptance criteria giá trị biên trong **US-02** → quy tắc **BR-02** trong tài liệu bàn giao → test case **TC-05** bị Fail trong báo cáo test, kèm `file:dòng` và cách sửa.
- **Giả định G1** (người lớn tuổi tự bật được nhắc) trong PRD → test user vòng 1 chỉ 2/5 làm được → nút "Nhắc tôi" đưa ra ngoài, ghi ở **Lịch sử thay đổi v2** của tài liệu bàn giao.
