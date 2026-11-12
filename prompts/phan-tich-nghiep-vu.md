# Prompt: phân tích nghiệp vụ (BA)

Chi tiết: [Dùng Claude làm prototype cho Designer, BA, PM](../guides/claude-lam-prototype.md). Mẫu: [templates/user-story.md](../templates/user-story.md).

## User story + acceptance criteria

```
Từ PRD (đính kèm / đã có trong Project), viết user story cho các tính năng MUST.
Mỗi story: "Là <vai>, tôi muốn <việc>, để <lợi ích>" + acceptance criteria dạng Given / When / Then.
Mỗi story xét đủ 5 nhóm criteria: happy path, input sai, không có quyền, dữ liệu trống, giá trị biên;
nhóm nào không áp dụng thì ghi N/A kèm lý do. Story > 10 criteria thì tách nhỏ. Đánh số US-01, US-02…
Theo mẫu templates/user-story.md.
```

## User flow

```
Vẽ user flow cho <journey> bằng Mermaid flowchart:
màn hình = hình chữ nhật, quyết định = hình thoi, hành động hệ thống = hình tròn.
Gồm nhánh lỗi (mất mạng, hết phiên, dữ liệu rỗng, không có quyền) và đường quay lại.
Sau sơ đồ: danh sách màn hình (ID S-01…, tên, mục đích, story liên quan).
```

## Quy tắc nghiệp vụ

```
Liệt kê quy tắc nghiệp vụ ẩn trong các story: giới hạn, điều kiện, công thức tính, phân quyền, trạng thái.
Bảng: ID BR-01… | quy tắc | ví dụ có số cụ thể | story liên quan | ai xác nhận.
Quy tắc nào bạn suy ra chứ không có trong PRD → ghi "cần PM xác nhận".
```

## Ma trận phân quyền

```
Lập ma trận phân quyền: hàng = hành động (xem, tạo, sửa, xóa, duyệt, xuất…) trên từng đối tượng,
cột = vai trò (<khách, user, chủ sở hữu, quản trị…>). Ô ghi: được / không / chỉ của mình.
Đánh dấu ô nào PRD chưa nói rõ.
```

## Dữ liệu mẫu

```
Tạo dữ liệu mẫu dạng JSON, tiếng Việt, giống thật, cho <tính năng>:
- 3 user khác vai, tên Việt có dấu (có 1 tên rất dài)
- đủ ca: list rỗng, 1 phần tử, 50 phần tử, giá trị biên, ngày quá khứ / tương lai
- tiền VND (số nguyên), ngày trong JSON dạng ISO 8601 (hiển thị dd/mm/yyyy), số điện thoại +84 giả
Không dùng dữ liệu thật của ai. Kèm bảng: bộ dữ liệu nào dùng cho màn / trạng thái / test nào.
```

## Rà thiếu sót

```
Đóng vai dev và tester khó tính. Đọc story, flow, quy tắc và liệt kê:
- mâu thuẫn giữa story và flow
- trường hợp chưa nói tới (hủy giữa chừng, làm 2 lần, 2 người cùng sửa, offline, hết hạn)
- câu chữ mơ hồ dev sẽ phải hỏi lại ("nhanh", "dễ", "phù hợp", "khoảng")
Mỗi mục 1 dòng + đề xuất cách viết lại.
```

## Từ cuộc họp ra yêu cầu

```
Đây là ghi chép / transcript cuộc họp với khách hàng: <dán, đã bỏ thông tin nhạy cảm>.
Tách thành: yêu cầu đã chốt · yêu cầu còn mơ hồ (kèm câu hỏi cần hỏi lại) · quyết định · việc cần làm (ai, hạn).
Chỉ ghi điều có trong ghi chép, không suy diễn.
```
