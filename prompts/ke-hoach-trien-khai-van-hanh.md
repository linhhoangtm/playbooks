# Prompt: kế hoạch, triển khai và vận hành

Chi tiết: [Dùng Claude xây dựng sản phẩm từ ý tưởng](../guides/claude-tu-y-tuong-den-san-pham.md) (giai đoạn 5, 8, 9). Mẫu: [templates/ROADMAP.md](../templates/ROADMAP.md), [templates/release-note.md](../templates/release-note.md), [templates/postmortem.md](../templates/postmortem.md).

## Chia MVP thành roadmap

```
Từ PRD.md và ARCHITECTURE.md, chia MVP thành milestone M0–M5 và các task.
Mỗi task gồm: ID, mô tả 1 dòng, layer (Flutter/API/DB), task phụ thuộc, acceptance criteria,
ước lượng (S/M/L). Task nào lớn hơn L thì chia nhỏ tiếp.
Xuất ra docs/ROADMAP.md dạng checklist.
```

## CI/CD

```
Tạo GitHub Actions: PR thì chạy lint và test (Flutter + server).
Merge vào main thì build Docker image, push lên registry, deploy lên VPS qua SSH, chạy migration.
Secret lấy từ GitHub Secrets, không hard-code. Viết kèm docs/DEPLOY.md hướng dẫn rollback.
```

## Store listing

```
Viết store listing tiếng Việt và tiếng Anh cho app <...>: tên (tối đa 30 ký tự),
mô tả ngắn (tối đa 80 ký tự), mô tả dài, 5 caption cho ảnh chụp màn hình, từ khóa ASO.
Dựa trên IDEA_BRIEF.md, nhấn mạnh điểm khác biệt so với đối thủ.
```

## Privacy policy

```
Đọc source app và backend ở <đường dẫn>. Liệt kê mọi dữ liệu cá nhân app thu thập: trường nào, lấy ở màn nào,
lưu ở đâu, giữ bao lâu, gửi cho bên thứ ba nào (AI, analytics, crash report, thanh toán), ghi file:dòng.
Từ bảng đó viết nháp chính sách quyền riêng tư tiếng Việt: dữ liệu thu thập, mục đích, chia sẻ, thời gian lưu,
quyền của người dùng (xem, sửa, xóa, rút lại đồng ý), cách liên hệ, cách xóa tài khoản.
Đánh dấu [CẦN LUẬT SƯ XEM] ở chỗ phụ thuộc quy định pháp luật. Không bịa dữ liệu không có trong code.
```

## Gom phản hồi sau phát hành

```
Đây là <120> review và <30> crash log trong tháng: <dán vào>.
Phân nhóm theo vấn đề, đếm số lần xuất hiện, đánh giá mức ảnh hưởng.
Đề xuất 5 task ưu tiên cho sprint tới, đúng format của docs/ROADMAP.md.
```

## Phân tích query chậm

```
Đây là kết quả EXPLAIN (ANALYZE, BUFFERS) của query chậm: <dán query + kết quả>. Bảng có khoảng <số> dòng.
Giải thích vì sao chậm, đề xuất index hoặc cách viết lại query, ước lượng tác động khi ghi.
Đối chiếu với docs/ARCHITECTURE.md: đã đến ngưỡng cần cache / read replica / partition chưa.
```

## Viết postmortem

```
Đây là log, timeline trong chat và các commit liên quan đến sự cố ngày <...>: <dán>.
Viết postmortem theo templates/postmortem.md: diễn biến theo giờ, nguyên nhân gốc (hỏi "vì sao" đến tầng quy trình),
vì sao không phát hiện sớm hơn, việc cần làm có người + hạn. Không đổ lỗi cá nhân. Chỗ không có dữ liệu thì ghi "chưa rõ".
```
