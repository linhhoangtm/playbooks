# Playbooks

Tài liệu, hướng dẫn và kinh nghiệm thực tế mình chia sẻ cho bạn bè.

## Bắt đầu từ đâu

| Bạn là | Đọc trước | Rồi dùng |
| --- | --- | --- |
| Mới dùng AI, làm văn phòng | [Hướng dẫn AI làm việc như trợ lý](guides/ai-lam-viec-nhu-tro-ly.md) | 40+ prompt trong chính guide đó |
| PM, BA, Designer | [Dùng Claude làm prototype](guides/claude-lam-prototype.md) | [Prompt ý tưởng, nghiệp vụ, UI, bàn giao](prompts/README.md) · template PRD, user story, bàn giao · [ví dụ điền sẵn](examples/nhac-ngay-gio/README.md) |
| Dev tự làm sản phẩm từ đầu | [Dùng Claude xây dựng sản phẩm từ ý tưởng](guides/claude-tu-y-tuong-den-san-pham.md) | [Template](templates/README.md) CLAUDE.md, settings.json, ROADMAP · [prompt code với Claude Code](prompts/code-voi-claude-code.md) |
| Dev / tech lead cần chọn stack | [Chọn kiến trúc](guides/chon-kien-truc-phan-mem.md), [Chọn công nghệ mobile](guides/chon-cong-nghe-mobile-app.md) | [Prompt kiến trúc](prompts/kien-truc.md) · template ARCHITECTURE, ADR |
| Dev / QA trước khi merge, release | [Dùng Claude để test web và mobile](guides/claude-test-web-mobile.md) | [Prompt test](prompts/test.md) · template báo cáo test, checklist release |
| Muốn đóng gói quy trình cho team | [Claude Skill và Plugin](guides/claude-skill-plugin.md) | [Cách dùng skill, plugin thông dụng](guides/claude-skill-plugin-thong-dung.md) |

## Theo giai đoạn của một sản phẩm

| Giai đoạn | Guide | Prompt | Template |
| --- | --- | --- | --- |
| 1. Ý tưởng, kiểm chứng | [Từ ý tưởng đến sản phẩm §1](guides/claude-tu-y-tuong-den-san-pham.md#1-ý-tưởng--kiểm-chứng-thị-trường) | [y-tuong-va-prd](prompts/y-tuong-va-prd.md) | [IDEA_BRIEF](templates/IDEA_BRIEF.md) |
| 2. PRD, MVP | [§2](guides/claude-tu-y-tuong-den-san-pham.md#2-đặc-tả-sản-phẩm-prd-và-scope-mvp), [Prototype §4](guides/claude-lam-prototype.md#4-prompt-mẫu-cho-pm) | [y-tuong-va-prd](prompts/y-tuong-va-prd.md) | [PRD](templates/PRD.md) |
| 3. Nghiệp vụ | [Prototype §5](guides/claude-lam-prototype.md#5-prompt-mẫu-cho-ba) | [phan-tich-nghiep-vu](prompts/phan-tich-nghiep-vu.md) | [user-story](templates/user-story.md) |
| 4. UI/UX, prototype, test user | [Prototype §6–8](guides/claude-lam-prototype.md#6-prompt-mẫu-cho-designer) | [thiet-ke-ui](prompts/thiet-ke-ui.md) | [DESIGN_SYSTEM](templates/DESIGN_SYSTEM.md), [kich-ban-test-user](templates/kich-ban-test-user.md) |
| 5. Bàn giao dev | [Prototype §9](guides/claude-lam-prototype.md#9-tạo-tài-liệu-bàn-giao-cho-dev) | [ban-giao-va-phat-hanh](prompts/ban-giao-va-phat-hanh.md) | [ban-giao-dev](templates/ban-giao-dev.md) |
| 6. Kiến trúc | [Chọn kiến trúc](guides/chon-kien-truc-phan-mem.md), [Chọn công nghệ mobile](guides/chon-cong-nghe-mobile-app.md) | [kien-truc](prompts/kien-truc.md) | [ARCHITECTURE](templates/ARCHITECTURE.md), [ADR](templates/ADR.md) |
| 7. Kế hoạch, build | [Từ ý tưởng §5–6](guides/claude-tu-y-tuong-den-san-pham.md#5-lập-kế-hoạch-chia-nhỏ-để-claude-code-làm-tốt) | [ke-hoach-trien-khai-van-hanh](prompts/ke-hoach-trien-khai-van-hanh.md), [code-voi-claude-code](prompts/code-voi-claude-code.md) | [ROADMAP](templates/ROADMAP.md), [CLAUDE.md](templates/CLAUDE.md), [settings.json](templates/settings.json) |
| 8. Test, review | [Test web và mobile](guides/claude-test-web-mobile.md) | [test](prompts/test.md) | [bao-cao-test](templates/bao-cao-test.md), [bao-loi](templates/bao-loi.md) |
| 9. Phát hành | [Từ ý tưởng §8](guides/claude-tu-y-tuong-den-san-pham.md#8-deploy-và-phát-hành), [Test §11](guides/claude-test-web-mobile.md#11-test-tính-năng-và-rủi-ro-bị-store-từ-chối) | [ban-giao-va-phat-hanh](prompts/ban-giao-va-phat-hanh.md), [ke-hoach-trien-khai-van-hanh](prompts/ke-hoach-trien-khai-van-hanh.md) | [checklist-release](templates/checklist-release.md), [release-note](templates/release-note.md), [store-review](templates/store-review.md) |
| 10. Vận hành | [Từ ý tưởng §9](guides/claude-tu-y-tuong-den-san-pham.md#9-vận-hành-và-cải-tiến) | [ke-hoach-trien-khai-van-hanh](prompts/ke-hoach-trien-khai-van-hanh.md) | [postmortem](templates/postmortem.md) |

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

- [Prompt mẫu](prompts/README.md): ý tưởng và PRD, phân tích nghiệp vụ, thiết kế UI, kiến trúc, code với Claude Code, test, bàn giao và phát hành, vận hành. Có 5 nguyên tắc làm việc với Claude dùng chung cho cả repo.
- [Template](templates/README.md): copy vào dự án, điền phần trong `<...>`.
- [Ví dụ điền sẵn](examples/nhac-ngay-gio/README.md): tính năng "Nhắc ngày giỗ" đi từ PRD, user story, tài liệu bàn giao đến báo cáo test.

## Góp ý

Thấy chỗ sai hoặc muốn bổ sung, bạn có thể mở Issue hoặc gửi Pull Request. Quy ước viết và sửa tài liệu: [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Nội dung được chia sẻ theo [CC BY 4.0](LICENSE): bạn được tự do dùng lại, chỉnh sửa và chia sẻ, kể cả cho mục đích thương mại, miễn là ghi nguồn **Linh Hoang** kèm link tới repo này.
