# Prompt mẫu

Prompt copy là dùng được ngay. Thay phần trong `<...>` bằng thông tin của bạn.

Đây là **bản chuẩn**. Guide trong [guides/](../guides/) dùng lại đúng nguyên văn kèm giải thích và ví dụ; guide có thể điền sẵn giá trị ví dụ vào `<...>` nhưng không đổi ý prompt. Muốn sửa prompt thì sửa ở đây trước, rồi tìm cùng đoạn trong guides/ để sửa theo.

| File | Dùng khi |
| --- | --- |
| [y-tuong-va-prd.md](y-tuong-va-prd.md) | Làm rõ ý tưởng, kiểm chứng thị trường, phản biện, viết PRD, cắt phạm vi MVP, chọn chỉ số |
| [phan-tich-nghiep-vu.md](phan-tich-nghiep-vu.md) | User story, acceptance criteria, user flow, quy tắc nghiệp vụ, phân quyền, dữ liệu mẫu |
| [thiet-ke-ui.md](thiet-ke-ui.md) | Design system, wireframe, mockup, prototype, UX writing, test prototype với user, tự rà UI/UX |
| [kien-truc.md](kien-truc.md) | Chọn kiến trúc, chọn công nghệ, thiết kế database và API, viết ADR |
| [code-voi-claude-code.md](code-voi-claude-code.md) | Lên kế hoạch, code từng bước, debug, refactor, review |
| [test.md](test.md) | 5 nhóm test case, UI/UX, security, chống bot, tấn công AI, performance, memory |
| [ban-giao-va-phat-hanh.md](ban-giao-va-phat-hanh.md) | Tài liệu bàn giao cho dev (từ PRD + ảnh chụp màn hình), cập nhật sau câu hỏi mở, release note, permission, nộp App Store / Google Play |
| [ke-hoach-trien-khai-van-hanh.md](ke-hoach-trien-khai-van-hanh.md) | Roadmap, CI/CD, store listing, privacy policy, gom phản hồi sau phát hành, query chậm, postmortem |

## 5 nguyên tắc làm việc với Claude

Mọi prompt trong repo đều theo 5 nguyên tắc này. Guide nào nhắc tới nguyên tắc cũng dùng đúng bản này.

1. **Bối cảnh trước, yêu cầu sau.** Nói rõ bạn là ai, dự án là gì, đã có gì. Đưa tài liệu thật (PRD, schema, code mẫu) thay vì mô tả bằng lời; để sẵn trong Project hoặc `CLAUDE.md` để khỏi lặp lại.
2. **Nói rõ đầu ra và giới hạn.** Định dạng (bảng, checklist, file), độ dài, ngôn ngữ; số mục, số màn, "chưa viết code", "không sửa file X".
3. **Bắt Claude hỏi lại hoặc đánh dấu giả định** thay vì tự điền chỗ trống: "Hỏi tôi tối đa 5 câu nếu còn thiếu", "đánh dấu [GIẢ ĐỊNH]".
4. **Một việc một lần.** Việc lớn thì chia bước, duyệt từng bước; mỗi phiên chat một chủ đề, xong thì mở phiên mới.
5. **Claude đề xuất, bạn quyết và kiểm chứng.** Kiến trúc, schema, bảo mật, chi phí do bạn duyệt. Chạy test, đọc diff, mở lại nguồn trước khi tin kết quả.

Mới dùng AI, cần công thức để viết từng prompt (vai trò, bối cảnh, nhiệm vụ, định dạng, ví dụ) hoặc prompt cho công việc văn phòng (viết, tóm tắt, marketing, bán hàng…): xem [Hướng dẫn AI làm việc như trợ lý](../guides/ai-lam-viec-nhu-tro-ly.md#2-công-thức-một-prompt-tốt).
