# Prompt: ý tưởng và PRD

Chi tiết: [Dùng Claude xây dựng sản phẩm từ ý tưởng](../guides/claude-tu-y-tuong-den-san-pham.md), [Dùng Claude làm prototype cho Designer, BA, PM](../guides/claude-lam-prototype.md). Mẫu: [templates/PRD.md](../templates/PRD.md).

## Làm rõ ý tưởng

```
Mình có ý tưởng: <mô tả 1–3 câu>.
Trước khi viết gì, hỏi mình tối đa 5 câu để làm rõ: ai dùng, họ đang giải quyết việc này thế nào,
vì sao cách cũ chưa ổn, đo thành công bằng gì, ràng buộc (thời gian, ngân sách, nền tảng, số người làm).
Sau khi mình trả lời, viết brief ≤ 150 chữ: Vấn đề · Người dùng · Giải pháp đề xuất · Chỉ số thành công · Ngoài phạm vi.
```

## Kiểm chứng thị trường

```
Tìm trên web các sản phẩm đang giải quyết vấn đề: <vấn đề>, ưu tiên thị trường <Việt Nam / quốc tế>.
Với 5 sản phẩm nổi bật: làm tốt gì, user phàn nàn gì (review App Store / Google Play, diễn đàn), giá, mô hình kiếm tiền.
Kết luận: khoảng trống còn lại, 3 rủi ro lớn nhất khiến ý tưởng này thất bại, 3 cách kiểm chứng rẻ nhất trong 2 tuần.
Ghi nguồn cho từng nhận định. Không có nguồn thì ghi rõ là suy đoán.
```

## Phản biện ý tưởng

```
Đóng vai nhà đầu tư khó tính. Đọc brief sau và chỉ ra:
- 5 lý do ý tưởng này sẽ thất bại, xếp theo mức nguy hiểm
- giả định nào mình đang coi là đúng mà chưa có bằng chứng
- nếu chỉ được làm 1 tính năng, đó là gì
Không khen. Brief: <dán>
```

## PRD 1 trang

```
Viết PRD 1 trang từ brief và kết quả kiểm chứng (dán bên dưới):
1. Bối cảnh & vấn đề  2. Mục tiêu + chỉ số (có số cụ thể)  3. Persona (1–2)
4. User journey chính (5–7 bước)  5. Tính năng  6. Ngoài phạm vi
7. Giả định cần kiểm chứng  8. Ràng buộc (thời gian, ngân sách, nền tảng)  9. Câu hỏi mở
Không viết giải pháp kỹ thuật. Giả định nào bạn tự thêm thì đánh dấu [GIẢ ĐỊNH].
Theo mẫu templates/PRD.md nếu mình đính kèm.
```

## Cắt phạm vi MVP

```
Xếp các tính năng trong PRD theo MoSCoW (MUST / SHOULD / COULD / WON'T) cho MVP
làm trong <số> tuần với <số> người. MUST = thiếu nó thì user không hoàn thành được journey chính.
Bảng: tính năng | nhóm | lý do | ước lượng S/M/L.
Phản biện mình nếu MUST chiếm > 40% tổng số.
```

## Chọn chỉ số đo

```
Với sản phẩm <mô tả>, đề xuất 1 chỉ số chính (North Star) và 3–5 chỉ số phụ.
Mỗi chỉ số: định nghĩa chính xác, cách đo (event nào cần ghi), mục tiêu 3 tháng đầu hợp lý, chỉ số nào dễ "ảo".
```
