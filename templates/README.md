# Template

Copy vào dự án rồi sửa phần trong `<...>`. Mỗi template dùng được với prompt tương ứng trong [prompts/](../prompts/).

Xếp theo thứ tự dùng trong một dự án:

| File | Đặt ở đâu | Dùng để |
| --- | --- | --- |
| [IDEA_BRIEF.md](IDEA_BRIEF.md) | `docs/` hoặc Claude Project | Kiểm chứng ý tưởng 1 trang, kết luận Go / No-go |
| [PRD.md](PRD.md) | `docs/` hoặc Claude Project | Mô tả sản phẩm / tính năng 1 trang |
| [user-story.md](user-story.md) | `docs/features/` | User story + acceptance criteria 5 nhóm |
| [DESIGN_SYSTEM.md](DESIGN_SYSTEM.md) | `docs/` | Token màu, chữ, khoảng cách, component, giọng văn |
| [kich-ban-test-user.md](kich-ban-test-user.md) | `docs/research/` | Kịch bản và ghi chép test prototype với 5 user |
| [ban-giao-dev.md](ban-giao-dev.md) | `docs/features/<ten>.md` (lớn thì tách thư mục) | Bàn giao từ PM / BA / Designer sang dev: màn, bảng field, quy tắc, công thức, validation, câu hỏi mở |
| [ARCHITECTURE.md](ARCHITECTURE.md) | `docs/` | Hệ thống đang chạy thế nào: thành phần, module, dữ liệu, vận hành |
| [ADR.md](ADR.md) | `docs/adr/0001-<ten>.md` | Ghi lại một quyết định kiến trúc |
| [ROADMAP.md](ROADMAP.md) | `docs/` | Milestone M0–M5 và task nhỏ cho Claude Code |
| [CLAUDE.md](CLAUDE.md) | Gốc repo | Cho Claude Code biết dự án, lệnh, quy ước, điều cấm |
| [settings.json](settings.json) | `.claude/settings.json` | Chặn cứng điều cấm (đọc `.env`, `git push`, `rm -rf`), hỏi trước khi commit hay cài thư viện |
| [bao-cao-test.md](bao-cao-test.md) | `test-reports/` | Kết quả test: checklist, test case, input, output, kết quả, cách sửa |
| [bao-loi.md](bao-loi.md) | Issue / tracker | Báo lỗi đủ thông tin để tái hiện |
| [checklist-release.md](checklist-release.md) | PR release | Rà trước khi phát hành web và nộp store |
| [release-note.md](release-note.md) | PR release / GitHub Release | Bản cho người dùng (store) và bản cho team (migration, rollback) |
| [store-review.md](store-review.md) | `docs/` | Nhật ký bị từ chối, thông tin cho reviewer |
| [postmortem.md](postmortem.md) | `docs/incidents/` | Phân tích sự cố sau khi khắc phục |

Ví dụ đã điền sẵn cho một tính năng: [examples/nhac-ngay-gio/](../examples/nhac-ngay-gio/).

**CLAUDE.md hay AGENTS.md?** Chỉ dùng Claude Code thì `CLAUDE.md` là đủ. Team dùng nhiều công cụ AI (Copilot, Cursor, Codex…) thì chép nội dung mẫu sang `AGENTS.md`, còn `CLAUDE.md` chỉ cần dòng `@AGENTS.md`.

**settings.json:** quy tắc dạng `Tool(mẫu)`, `deny` chặn hẳn, `ask` hỏi trước khi chạy. Thêm lệnh migrate / deploy production của dự án vào `deny`. Chi tiết cú pháp: [Claude Code settings](https://code.claude.com/docs/en/settings).

**Mã định danh dùng chung giữa các template:** màn `S-01`, story `US-01`, quy tắc `BR-01`, validation `VR-01`, test case `TC-01`, câu hỏi mở `Q-01`, ADR `ADR-0001`.
