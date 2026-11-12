# Playbooks

Tài liệu, hướng dẫn và kinh nghiệm thực tế mình chia sẻ cho bạn bè.

## Mục lục

| Tài liệu | Nội dung |
| --- | --- |
| [Dùng Claude xây dựng sản phẩm từ ý tưởng](guides/claude-tu-y-tuong-den-san-pham.md) | 9 giai đoạn từ ý tưởng đến app phát hành: kiểm chứng thị trường, PRD, kiến trúc theo quy mô, UI/UX, Claude Code, test, deploy. Ví dụ Flutter + Go/FastAPI + PostgreSQL |
| [Hướng dẫn AI làm việc như trợ lý](guides/ai-lam-viec-nhu-tro-ly.md) | Công thức prompt 5 bước và hơn 40 prompt mẫu dùng ngay: viết, tóm tắt, marketing, bán hàng, phân tích, học tập, văn phòng, theo vị trí công việc |
| [Chọn kiến trúc phần mềm phù hợp](guides/chon-kien-truc-phan-mem.md) | 5 nhóm yếu tố quyết định, monolith hay microservices, cây quyết định, khi code cùng AI, case study Shopify, Segment, Prime Video |
| [Chọn công nghệ làm mobile app](guides/chon-cong-nghe-mobile-app.md) | So sánh Flutter, React Native, Kotlin Multiplatform, Native, .NET MAUI, Capacitor, PWA và gợi ý theo loại app |
| [Dùng Claude để test web app và mobile app](guides/claude-test-web-mobile.md) | 5 nhóm test case, UI/UX, security, performance, memory, chống bot và tấn công AI, rủi ro bị App Store / Google Play từ chối. Ví dụ Flutter, React Native, Next.js |
| [Dùng Claude làm prototype cho Designer, BA, PM](guides/claude-lam-prototype.md) | Quy trình 7 bước từ ý tưởng đến prototype, prompt theo vai, test với 5 user, mẫu tài liệu bàn giao cho dev |
| [Claude Skill và Plugin: là gì, khi nào dùng](guides/claude-skill-plugin.md) | So sánh CLAUDE.md, skill, subagent, hook, MCP, plugin; cách tạo skill, plugin, marketplace; giới thiệu skill/plugin nên thử |
| [Cách dùng các skill và plugin thông dụng](guides/claude-skill-plugin-thong-dung.md) | Cài, lệnh gọi, prompt mẫu cho docx/xlsx/pptx/pdf, frontend-design, commit-commands, feature-dev, code-review, hookify, Superpowers… |

## Cấu trúc

```text
playbooks/
├── guides/      # hướng dẫn theo chủ đề
├── prompts/     # prompt mẫu dùng ngay, theo từng giai đoạn
├── templates/   # idea brief, PRD, user story, design system, bàn giao, kiến trúc, ADR, roadmap, CLAUDE.md, báo cáo test, release…
└── examples/    # một tính năng điền sẵn từ PRD đến báo cáo test
```

- [Prompt mẫu](prompts/README.md): ý tưởng và PRD, phân tích nghiệp vụ, thiết kế UI, kiến trúc, code với Claude Code, test, bàn giao và phát hành.
- [Template](templates/README.md): copy vào dự án, điền phần trong `<...>`.
- [Ví dụ điền sẵn](examples/nhac-ngay-gio/README.md): tính năng "Nhắc ngày giỗ" đi từ PRD, user story, tài liệu bàn giao đến báo cáo test.

## Góp ý

Thấy chỗ sai hoặc muốn bổ sung, bạn có thể mở Issue hoặc gửi Pull Request.

## License

Nội dung được chia sẻ theo [CC BY 4.0](LICENSE): bạn được tự do dùng lại, chỉnh sửa và chia sẻ, kể cả cho mục đích thương mại, miễn là ghi nguồn **Linh Hoang** kèm link tới repo này.
