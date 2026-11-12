# Template

Copy vào dự án rồi sửa phần trong `<...>`. Mỗi template dùng được với prompt tương ứng trong [prompts/](../prompts/).

| File | Đặt ở đâu | Dùng để |
| --- | --- | --- |
| [CLAUDE.md](CLAUDE.md) | Gốc repo | Cho Claude Code biết dự án, lệnh, quy ước, điều cấm |
| [settings.json](settings.json) | `.claude/settings.json` | Chặn cứng điều cấm (đọc `.env`, `git push`, `rm -rf`), hỏi trước khi commit hay cài thư viện |
| [PRD.md](PRD.md) | `docs/` hoặc Claude Project | Mô tả sản phẩm / tính năng 1 trang |
| [user-story.md](user-story.md) | `docs/features/` | User story + acceptance criteria 5 nhóm |
| [ADR.md](ADR.md) | `docs/adr/0001-<ten>.md` | Ghi lại một quyết định kiến trúc |
| [ban-giao-dev.md](ban-giao-dev.md) | `docs/features/<ten>.md` (lớn thì tách thư mục) | Bàn giao từ PM / BA / Designer sang dev: màn, bảng field, quy tắc, công thức, validation, câu hỏi mở |
| [bao-cao-test.md](bao-cao-test.md) | `test-reports/` | Kết quả test: checklist, test case, input, output, kết quả, cách sửa |
| [bao-loi.md](bao-loi.md) | Issue / tracker | Báo lỗi đủ thông tin để tái hiện |
| [checklist-release.md](checklist-release.md) | PR release | Rà trước khi phát hành web và nộp store |

**CLAUDE.md hay AGENTS.md?** Chỉ dùng Claude Code thì `CLAUDE.md` là đủ. Team dùng nhiều công cụ AI (Copilot, Cursor, Codex…) thì chép nội dung mẫu sang `AGENTS.md`, còn `CLAUDE.md` chỉ cần dòng `@AGENTS.md`.

**settings.json:** quy tắc dạng `Tool(mẫu)`, `deny` chặn hẳn, `ask` hỏi trước khi chạy. Thêm lệnh migrate / deploy production của dự án vào `deny`. Chi tiết cú pháp: [Claude Code settings](https://code.claude.com/docs/en/settings).

**Mã định danh dùng chung giữa các template:** màn `S-01`, story `US-01`, quy tắc `BR-01`, validation `VR-01`, test case `TC-01`, câu hỏi mở `Q-01`, ADR `ADR-0001`.
