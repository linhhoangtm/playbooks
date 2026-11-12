# Prompt mẫu

Prompt copy là dùng được ngay. Thay phần trong `<...>` bằng thông tin của bạn.

Đây là bản gọn để copy; các guide trong [guides/](../guides/) có cùng prompt kèm giải thích và ví dụ. Sửa prompt ở đây thì sửa luôn ở guide tương ứng.

| File | Dùng khi |
| --- | --- |
| [y-tuong-va-prd.md](y-tuong-va-prd.md) | Làm rõ ý tưởng, kiểm chứng thị trường, viết PRD, cắt phạm vi MVP |
| [phan-tich-nghiep-vu.md](phan-tich-nghiep-vu.md) | User story, acceptance criteria, user flow, quy tắc nghiệp vụ, dữ liệu mẫu |
| [thiet-ke-ui.md](thiet-ke-ui.md) | Design system, wireframe, mockup, prototype, tự rà UI/UX |
| [kien-truc.md](kien-truc.md) | Chọn kiến trúc, chọn công nghệ, thiết kế database và API, viết ADR |
| [code-voi-claude-code.md](code-voi-claude-code.md) | Lên kế hoạch, code từng bước, debug, refactor, review |
| [test.md](test.md) | 5 nhóm test case, UI/UX, security, chống bot, tấn công AI, performance, memory, store |
| [ban-giao-va-phat-hanh.md](ban-giao-va-phat-hanh.md) | Bàn giao cho dev, release note, rà trước khi nộp App Store / Google Play |

## 5 nguyên tắc viết prompt

1. **Bối cảnh trước, yêu cầu sau.** Nói rõ bạn là ai, dự án là gì, đã có gì.
2. **Nói rõ đầu ra.** Định dạng (bảng, checklist, file), độ dài, ngôn ngữ.
3. **Đặt giới hạn.** Số mục, số màn, "chưa viết code", "không sửa file X".
4. **Bắt Claude hỏi lại hoặc đánh dấu giả định** thay vì tự điền chỗ trống.
5. **Một việc một lần.** Việc lớn thì chia bước, duyệt từng bước.

Muốn prompt cho công việc văn phòng (viết, tóm tắt, marketing, bán hàng…), xem [Hướng dẫn AI làm việc như trợ lý](../guides/ai-lam-viec-nhu-tro-ly.md).
