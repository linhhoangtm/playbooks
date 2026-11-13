# Góp ý và sửa tài liệu

Cảm ơn bạn muốn góp ý. Repo này là tài liệu tiếng Việt, nên phần lớn quy ước dưới đây là về cách viết và giữ các file nhất quán với nhau.

## Cách góp ý

- **Báo sai, link chết, thông tin lỗi thời:** mở Issue, ghi file, đoạn sai và nguồn đúng (link).
- **Sửa nhỏ** (chính tả, link, câu chữ): gửi Pull Request thẳng.
- **Thêm guide, prompt, template mới:** mở Issue trước để thống nhất phạm vi, tránh trùng với file đang có.

## Repo tổ chức thế nào

| Thư mục | Chứa gì | Quy tắc |
| --- | --- | --- |
| `guides/` | Hướng dẫn theo chủ đề, có giải thích và ví dụ | Mỗi guide có dòng `Cập nhật: yyyy-mm-dd` và mục Nguồn ở cuối |
| `prompts/` | Prompt ngắn, copy là dùng | **Bản chuẩn** của mọi prompt |
| `templates/` | Mẫu tài liệu để copy vào dự án | Phần cần điền đặt trong `<...>` |
| `examples/` | Template đã điền cho một tính năng mẫu | Dữ liệu giả, ghi rõ là ví dụ minh họa |

## Sửa prompt

Prompt có thể xuất hiện ở cả `prompts/` và trong guide. Để hai nơi không lệch nhau:

1. Sửa ở `prompts/` trước.
2. Tìm cùng đoạn trong `guides/` (tìm theo câu đầu của prompt) và sửa y hệt. Guide được điền sẵn giá trị ví dụ vào `<...>`, nhưng không đổi ý prompt.
3. Prompt mới viết theo [5 nguyên tắc làm việc với Claude](prompts/README.md#5-nguyên-tắc-làm-việc-với-claude): có bối cảnh, nói rõ đầu ra và giới hạn, bắt Claude hỏi lại hoặc đánh dấu `[GIẢ ĐỊNH]`, một việc một lần.

## Mã định danh dùng chung

Template, prompt và ví dụ tham chiếu nhau bằng mã. Giữ đúng tiền tố:

| Mã | Dùng cho |
| --- | --- |
| `S-01` | Màn hình |
| `US-01` | User story |
| `BR-01` | Quy tắc nghiệp vụ |
| `VR-01` | Validation |
| `TC-01` | Test case |
| `Q-01` | Câu hỏi mở |
| `ADR-0001` | Quyết định kiến trúc |
| `T-01`, `M0` | Task, milestone trong roadmap |

Nhãn cho chỗ AI tự suy luận: `[GIẢ ĐỊNH]`.

## Cách viết

- Tiếng Việt có dấu, câu ngắn, nói thẳng việc cần làm. Giữ nguyên tiếng Anh cho thuật ngữ kỹ thuật, tên lệnh, tên thư viện.
- Ưu tiên bảng và checklist hơn đoạn văn dài. Mỗi mục có ví dụ cụ thể (con số, tên file, câu lệnh) thay vì nói chung chung.
- Số liệu, phiên bản, giá, quy định pháp luật: luôn kèm link nguồn; không chắc thì ghi rõ "kiểm lại" thay vì đoán.
- Cập nhật dòng `Cập nhật:` ở đầu guide khi sửa nội dung (không cần khi chỉ sửa chính tả).
- Ví dụ dùng dữ liệu giả: tên người, số điện thoại, email, dự án đều bịa. Không đưa dữ liệu thật của ai, kể cả tên dự án nội bộ.
- Link nội bộ dùng đường dẫn tương đối (`../templates/PRD.md`), anchor theo kiểu GitHub (chữ thường, giữ dấu tiếng Việt, khoảng trắng thành `-`).

## Kiểm tra trước khi gửi

GitHub Actions tự chạy trên mỗi Pull Request ([.github/workflows/docs.yml](.github/workflows/docs.yml)):

- **markdownlint:** định dạng markdown, cấu hình ở [.markdownlint-cli2.jsonc](.markdownlint-cli2.jsonc).
- **lychee:** kiểm link nội bộ, anchor và link ngoài. Trang chặn trình kiểm tra tự động (trả 403, 429) được chấp nhận; link chết thật (404) làm CI đỏ.

Chạy trên máy trước (cần Node.js):

```bash
npx markdownlint-cli2 "**/*.md"
```

## License

Khi gửi Pull Request, bạn đồng ý cho nội dung của mình được chia sẻ theo [CC BY 4.0](LICENSE) như phần còn lại của repo.
