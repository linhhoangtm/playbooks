# Cách dùng các skill và plugin thông dụng của Claude

Cập nhật: 2026-11-12

Tài liệu đi kèm [Claude Skill và Plugin: là gì, khi nào dùng, dùng thế nào](claude-skill-plugin.md). Bài đó giải thích khái niệm và giới thiệu tổng quát; bài này là **hướng dẫn dùng từng cái**: cài thế nào, gọi thế nào, prompt mẫu, mẹo.

## Cài đặt chung

| Nguồn | Thêm marketplace (1 lần) | Cài |
| --- | --- | --- |
| Plugin chính thức | Có sẵn | `/plugin install <tên>@claude-plugins-official` |
| Skill của Anthropic | `/plugin marketplace add anthropics/skills` | `/plugin install document-skills@anthropic-agent-skills` hoặc `example-skills@anthropic-agent-skills` |
| Cộng đồng | `/plugin marketplace add <owner>/<repo>` | `/plugin install <tên>@<marketplace>` |

Trên claude.ai: skill tài liệu (Word, Excel, PowerPoint, PDF) có sẵn; skill khác bật hoặc tải .zip lên trong Settings.

**Ba cách gọi:**

| Cách | Ví dụ | Khi nào |
| --- | --- | --- |
| Nói tự nhiên | "Tạo file Excel báo cáo doanh thu tháng 10" | Skill tự kích hoạt khi khớp mô tả |
| Slash command | `/commit`, `/feature-dev` | Muốn chắc chắn gọi đúng cái |
| Gọi tên | "Dùng skill frontend-design để…" | Skill không tự bật, hoặc có nhiều skill giống nhau |

Lệnh của plugin có thể hiện dạng ngắn (`/commit`) hoặc có tiền tố plugin (`/commit-commands:commit`) tùy phiên bản. Gõ `/` để xem danh sách đang có; `/plugin` để bật/tắt/gỡ.

Lệnh `/plugin …` gõ **trong phiên Claude Code** (terminal hoặc tab Code của app desktop), không gõ trong chat claude.ai. Từ terminal có thể dùng dạng `claude plugin install <tên>@<marketplace>`.

**Nguyên tắc:** cài ít, dùng thật, gỡ cái không dùng. Mỗi skill/plugin đều chiếm một chút context và có thể chồng chéo với nhau.

## 1. Bộ tài liệu: docx, xlsx, pptx, pdf

**Làm gì:** tạo, đọc, sửa file Office và PDF thật — có định dạng, công thức, biểu đồ, ghi chú, tracked changes. **Gọi:** nói tự nhiên và **nêu rõ định dạng file** ("file Word", "file .xlsx").

| Skill | Prompt mẫu |
| --- | --- |
| **docx** | `Sửa lỗi chính tả và viết gọn file hợp đồng đính kèm, bật tracked changes để mình duyệt từng chỗ. Giữ nguyên định dạng.` |
| **xlsx** | `Tạo file Excel theo dõi chi phí dự án: sheet Chi tiết (ngày, hạng mục, số tiền VND), sheet Tổng hợp dùng công thức SUMIFS theo hạng mục và tháng, biểu đồ cột. Không hardcode số tổng.` |
| **pptx** | `Làm file PowerPoint 8 slide giới thiệu sản phẩm từ PRD đính kèm. Mỗi slide 1 ý, ≤ 30 chữ, có speaker notes. Dùng template công ty đính kèm.` |
| **pdf** | `Gộp 3 file PDF này, thêm số trang, rồi trích bảng ở trang 4–6 ra Excel.` / `Điền form PDF đính kèm bằng dữ liệu sau: …` |

**Mẹo:**

- Có template/file mẫu thì đính kèm — Claude theo đúng layout, font, màu.
- Excel: yêu cầu **dùng công thức** thay vì số tính sẵn, để file còn "sống" khi sửa dữ liệu.
- File dài: làm dàn ý trước, duyệt rồi mới dựng file.
- Trên claude.ai, nếu chỉ cần tài liệu để đọc/chia sẻ (không bắt buộc .docx), Claude có thể tạo dạng doc/artifact sửa trực tiếp và xuất ra Word/PDF sau.

## 2. Skill cho dev

### frontend-design

**Làm gì:** đẩy Claude chọn hướng thiết kế rõ ràng (typography, màu, bố cục, chuyển động) thay vì giao diện "mặc định của AI". **Gọi:** tự kích hoạt khi làm UI web.

```
Làm landing page cho <sản phẩm>, khách hàng là <ai>, cảm giác <trang trọng / trẻ trung / truyền thống Việt>.
Stack: <Next.js + Tailwind>. Dùng component có sẵn trong <thư mục> nếu phù hợp.
Cho mình 2 hướng thị giác khác nhau, mỗi hướng 1 màn hero, rồi chờ mình chọn.
```

Mẹo: nói rõ cảm giác và người dùng; nếu đã có design system thì bảo "theo design system trong repo", tránh skill tự sáng tác lệch thương hiệu.

### webapp-testing

**Làm gì:** dùng Playwright mở web app đang chạy local — bấm, nhập, chụp màn hình, đọc console log. **Cần:** Python + Playwright trên máy; dev server đang chạy.

```
App đang chạy ở http://localhost:3000. Test flow đăng ký: nhập email sai, email đã tồn tại, mật khẩu ngắn, hợp lệ.
Chụp màn hình mỗi bước ở 375px và 1440px. Báo lỗi console. Bảng: bước | mong đợi | thực tế | pass/fail.
```

### mcp-builder

**Làm gì:** quy trình 4 bước xây MCP server (nghiên cứu API → thiết kế tool → code → đánh giá), bằng Python (FastMCP) hoặc TypeScript.

```
Xây MCP server bằng Python cho API nội bộ của mình (OpenAPI đính kèm). Chỉ cần 4 tool đọc:
tìm khách hàng, xem đơn hàng, xem tồn kho, báo cáo doanh thu theo ngày. Không có tool ghi/xóa.
API key đọc từ biến môi trường. Kèm cách thêm vào Claude Code.
```

### claude-api

**Làm gì:** giúp viết code gọi Claude API / SDK đúng cách (model, streaming, tool use, prompt caching…).

```
Thêm tính năng tóm tắt bình luận cho API FastAPI của mình bằng Claude API: streaming về client,
timeout, retry, giới hạn độ dài input, quota theo user. Key đọc từ env.
```

### skill-creator

**Làm gì:** hướng dẫn viết skill mới, viết test case cho skill và đo skill có kích hoạt đúng không.

```
Dùng skill-creator tạo skill "review-pr-team": review PR theo checklist trong docs/review-checklist.md.
Viết 5 câu nên kích hoạt, 3 câu không nên kích hoạt, rồi test.
```

## 3. Plugin quy trình code

### commit-commands

Cài: `/plugin install commit-commands@claude-plugins-official`

| Lệnh | Làm gì |
| --- | --- |
| `/commit` | Xem thay đổi, stage, viết commit message theo phong cách của repo rồi commit |
| `/commit-push-pr` | Tạo nhánh (nếu đang ở main), commit, push, mở PR có mô tả — một bước. Cần GitHub CLI `gh` đã đăng nhập |
| `/clean_gone` | Xóa nhánh local mà remote đã xóa (sau khi PR được merge) |

Quy trình: code → `/commit` nhiều lần → xong tính năng `/commit-push-pr` → merge xong `/clean_gone`. Luôn đọc lại message và mô tả PR trước khi push.

> Dự án quy định "không tự commit" (vd trong CLAUDE.md) thì chỉ gọi `/commit` khi chính bạn muốn commit, đừng giao cho agent tự chạy.

### feature-dev

Cài: `/plugin install feature-dev@claude-plugins-official` · Gọi: `/feature-dev <mô tả tính năng>`

Dẫn Claude qua nhiều giai đoạn: hiểu yêu cầu → khám phá codebase (agent explorer) → hỏi lại chỗ chưa rõ → đề xuất kiến trúc (agent architect) → code → review (agent reviewer) → tóm tắt.

```
/feature-dev Thêm tính năng nhắc ngày giỗ theo âm lịch. Spec ở docs/features/nhac-gio.md.
Ràng buộc: không thêm dependency, dùng hàm đổi lịch có sẵn, test bằng flutter_test.
```

Mẹo: trả lời kỹ ở bước "câu hỏi làm rõ" và chọn phương án kiến trúc trước khi cho code. Hợp tính năng vừa/lớn; sửa nhỏ thì prompt thường nhanh hơn.

### code-review

Cài: `/plugin install code-review@claude-plugins-official` · Gọi: `/code-review` trên nhánh có PR

Review PR bằng nhiều agent chạy song song (tuân thủ CLAUDE.md, tìm bug, lịch sử thay đổi…), mỗi phát hiện có **điểm tin cậy**; chỉ báo cái vượt ngưỡng để giảm nhiễu. Cần `gh` để đọc PR.

Mẹo: CLAUDE.md càng rõ quy ước thì review càng sát, vì một agent chuyên kiểm tra code có theo CLAUDE.md không.

### pr-review-toolkit

Cài: `/plugin install pr-review-toolkit@claude-plugins-official` · Gọi: `/pr-review-toolkit:review-pr [khía cạnh]`

6 agent review chuyên từng mảng: code tổng quát, đơn giản hóa, comment, chất lượng test, lỗi bị nuốt im lặng (silent failure), thiết kế type. Chọn khía cạnh khi cần:

```
/pr-review-toolkit:review-pr tests errors
```

**code-review hay pr-review-toolkit?** code-review: một lệnh, lọc nhiễu tốt, hợp review nhanh trước merge. pr-review-toolkit: sâu theo từng mảng, hợp PR lớn hoặc khi nghi một vấn đề cụ thể (vd test yếu).

### code-simplifier

Cài: `/plugin install code-simplifier@claude-plugins-official`

Agent làm gọn code vừa viết mà giữ nguyên hành vi. Dùng sau khi tính năng chạy được, trước khi review:

```
Dùng code-simplifier làm gọn các file đã đổi trên nhánh này. Không đổi hành vi; chạy test trước và sau.
```

## 4. Bảo mật và luật

### security-guidance

Cài: `/plugin install security-guidance@claude-plugins-official` — cài xong là chạy, không cần gọi.

Gồm hook chạy mỗi khi Claude sửa file (`Edit`, `Write`): cảnh báo mẫu code nguy hiểm như command injection, XSS (`innerHTML`, `dangerouslySetInnerHTML`), `eval`… Phiên bản mới còn review diff khi Claude xong việc.

Mẹo: đây là lớp nhắc nhở, không thay được review bảo mật thật. Kết hợp với lệnh `/security-review` có sẵn của Claude Code và agent bảo mật trong bộ kiểm thử của bạn trước release.

### hookify

Cài: `/plugin install hookify@claude-plugins-official`

Tạo hook bằng file markdown thay vì viết script + sửa `settings.json`. Luật có hiệu lực ngay lần dùng tool kế tiếp, không cần khởi động lại.

| Lệnh | Làm gì |
| --- | --- |
| `/hookify <mô tả>` | Tạo luật từ mô tả. Không ghi gì → tự phân tích cuộc chat tìm hành vi nên chặn |
| `/hookify:list` | Xem các luật |
| `/hookify:configure` | Bật/tắt luật |

Ví dụ:

```
/hookify Chặn mọi lệnh rm -rf, git push --force, và cảnh báo khi sửa file .env hoặc *.keystore
```

Luật được lưu thành file `.claude/hookify.<tên>.local.md` (dự án) hoặc `~/.claude/` (mọi dự án):

```markdown
---
name: block-dangerous-rm
enabled: true
event: bash
pattern: rm\s+-rf
action: block
---
Không dùng rm -rf. Muốn xóa thì hỏi người dùng trước.
```

`event` có thể là lệnh bash, sửa file, prompt của user, hoặc lúc Claude chuẩn bị dừng. `action`: cảnh báo hoặc chặn. Cần Python 3 trên máy. Thêm `.claude/*.local.md` vào `.gitignore` nếu luật chỉ dành cho mình.

Dùng khi nào: có quy tắc trong CLAUDE.md mà Claude vẫn thỉnh thoảng vi phạm → chuyển thành luật hookify.

### Trail of Bits skills

Cài: `/plugin marketplace add trailofbits/skills` rồi `/plugin install <tên>@<marketplace>` (xem danh sách trong `/plugin`).

Bộ skill bảo mật của công ty audit Trail of Bits: chạy static analysis (CodeQL, Semgrep), differential review (review bảo mật theo diff), tìm cấu hình mặc định không an toàn, viết rule Semgrep.

```
Chạy differential review bảo mật cho thay đổi trên nhánh này so với main. Tập trung API trong src/app/api.
Chỉ báo lỗi có bằng chứng, kèm file:dòng và mức độ.
```

Một số skill cần cài sẵn công cụ (Semgrep, CodeQL). Chỉ cài phần cần dùng.

## 5. Code intelligence và tích hợp

### LSP plugin

Cho Claude đọc code như IDE: đi tới định nghĩa, tìm mọi nơi gọi, thấy lỗi type ngay sau khi sửa — thay vì grep và đoán.

```
/plugin install pyright-lsp@claude-plugins-official      # Python
/plugin install gopls-lsp@claude-plugins-official        # Go
/plugin install csharp-lsp@claude-plugins-official       # C#
```

Tìm LSP cho TypeScript, PHP, Dart… trong `/plugin` → Discover (danh sách thay đổi theo thời gian). **Phải cài language server trên máy trước** (vd `pip install pyright`, `go install golang.org/x/tools/gopls@latest`), đọc README của từng plugin. Chỉ cài cho ngôn ngữ chính của dự án.

### GitHub

`/plugin install github@claude-plugins-official` — Claude đọc issue, PR, review comment, CI trực tiếp.

```
Đọc issue #123 và các comment, tóm tắt yêu cầu, rồi lên kế hoạch sửa. Chưa code.
```

```
PR #45 có 3 review comment chưa xử lý. Sửa từng cái, mỗi cái 1 commit, báo lại cái nào không đồng ý và vì sao.
```

### Context7

`/plugin install context7@claude-plugins-official` — lấy tài liệu **phiên bản hiện tại** của thư viện, tránh Claude dùng API cũ đã bị đổi.

```
Dùng Context7 tra tài liệu Next.js 16 về server actions rồi sửa form đăng ký theo cách mới.
```

### Supabase và các tích hợp khác

Plugin chính hãng của Supabase kèm skill + MCP: quản lý project, database, auth, storage, thực hành tốt cho Postgres. Nhiều dịch vụ khác (Vercel, Sentry, Cloudflare, Figma…) cũng có plugin/MCP riêng — tìm trong `/plugin`.

Mẹo an toàn: kết nối dịch vụ có dữ liệu thật thì dùng tài khoản/project **dev hoặc chỉ đọc**; không trỏ Claude thẳng vào database production.

## 6. Superpowers

Cài: `/plugin install superpowers@claude-plugins-official` (hoặc từ marketplace gốc `obra/superpowers-marketplace`).

Bộ skill của Jesse Vincent biến Claude thành "dev có kỷ luật": khi có skill phù hợp với việc đang làm, việc dùng skill là bắt buộc. Phần lớn skill **tự kích hoạt**.

| Skill | Kích hoạt khi | Làm gì |
| --- | --- | --- |
| brainstorming | Bắt đầu tính năng mới | Hỏi từng câu để làm rõ ý định, yêu cầu, thiết kế trước khi code |
| writing-plans | Đã có spec, việc nhiều bước | Viết kế hoạch chi tiết từng bước |
| executing-plans / subagent-driven-development | Có kế hoạch | Thực hiện theo lô có điểm dừng duyệt, hoặc giao mỗi task cho một subagent mới kèm 2 lượt review |
| test-driven-development | Code tính năng / sửa bug | RED → GREEN → REFACTOR: viết test fail trước, rồi code tối thiểu cho pass |
| systematic-debugging | Gặp bug, test fail | Tìm nguyên nhân gốc theo quy trình trước khi đề xuất sửa |
| verification-before-completion | Trước khi báo "xong" | Bắt chạy lệnh kiểm chứng, có bằng chứng mới được nói đã xong |
| requesting-code-review, finishing-a-development-branch, using-git-worktrees | Cuối tính năng | Review, quyết merge hay PR, làm việc song song bằng worktree |

Quy trình mẫu cho một tính năng:

```
Mình muốn thêm tính năng xuất báo cáo doanh thu ra Excel cho admin.   ← brainstorming tự chạy, hỏi lại
(trả lời các câu hỏi, duyệt thiết kế)
Viết kế hoạch thực hiện.                                            ← writing-plans
Thực hiện kế hoạch.                                                 ← executing-plans + TDD
```

Phiên bản có slash command (vd `/superpowers:brainstorm`, `/superpowers:write-plan`, `/superpowers:execute-plan`) — gõ `/` để xem tên đúng với bản bạn cài.

**Khi nào hợp:** việc dài nhiều giờ, muốn Claude tự làm có kỷ luật, dự án coi trọng test. **Khi nào không:** sửa nhỏ, prototype vứt đi, dự án đã có quy trình riêng chặt (vd CLAUDE.md quy định cách test khác) — TDD bắt buộc có thể xung đột. Không bật cùng lúc với `feature-dev` vì hai bên cùng ép quy trình.

## 7. Skill cho PM, BA, designer

Các skill này nằm trong `example-skills@anthropic-agent-skills` (Claude Code) hoặc tải .zip từ repo `anthropics/skills` lên claude.ai.

| Skill | Làm gì | Prompt mẫu |
| --- | --- | --- |
| **doc-coauthoring** | Cùng soạn tài liệu theo vòng: dàn ý → từng phần → rà lại | `Cùng mình viết PRD cho tính năng X. Hỏi mình bối cảnh trước, làm dàn ý, rồi viết từng mục chờ mình duyệt.` |
| **internal-comms** | Viết thông báo nội bộ, báo cáo tuần, FAQ, bản tin sự cố theo mẫu | `Viết báo cáo tuần cho team từ danh sách việc sau: … phần Đã xong / Đang làm / Vướng mắc / Tuần tới.` |
| **brand-guidelines** | Áp màu, font, giọng văn thương hiệu vào output. Bản gốc theo thương hiệu Anthropic — nên **copy và sửa thành thương hiệu của bạn** | `Dùng skill brand-<tên công ty> làm one-pager giới thiệu dịch vụ.` |
| **theme-factory** | Bộ theme màu + font có sẵn áp cho slide, tài liệu, trang HTML | `Áp theme trang nhã cho bộ slide này, giữ nội dung.` |
| **canvas-design** | Tạo hình ảnh tĩnh (poster, bìa, hình minh họa) ra PNG/PDF bằng code | `Làm poster A4 sự kiện ra mắt app, tông xanh trầm, chữ tiếng Việt, xuất PDF in được.` |
| **algorithmic-art** | Nghệ thuật tạo sinh bằng code (p5.js) | `Tạo hình nền trừu tượng lấy cảm hứng hoa văn trống đồng, cho phép chỉnh màu.` |
| **web-artifacts-builder** | Artifact HTML nhiều component (React, Tailwind, shadcn/ui) trên claude.ai | `Dựng prototype bấm thử được 4 màn: danh sách, chi tiết, tạo mới, cài đặt, dữ liệu mẫu tiếng Việt.` |

**Mẹo cho người không code:**

- Bắt đầu trên claude.ai, không cần Claude Code. Skill tài liệu (mục 1) đã có sẵn.
- Skill mạnh nhất cho bạn thường là **skill tự tạo** từ quy trình riêng của team (mẫu PRD công ty, giọng văn thương hiệu). Làm việc đó với Claude một lần cho tới khi ưng, rồi nhờ Claude "biến thành skill".
- Skill thiết kế làm hình ảnh bằng code; muốn thiết kế UI để chỉnh sửa trực quan thì dùng Claude Design (xem [Dùng Claude làm prototype cho Designer, BA, PM](claude-lam-prototype.md)).

## 8. Kết hợp thành quy trình

### Một tính năng từ đầu đến cuối (dev)

| Bước | Dùng |
| --- | --- |
| Đọc issue, làm rõ yêu cầu | GitHub + `/feature-dev` (hoặc Superpowers brainstorming) |
| Tra tài liệu thư viện mới nhất | Context7 |
| Code UI | frontend-design + LSP |
| Trong lúc code | security-guidance + luật hookify chạy nền |
| Commit từng bước | `/commit` |
| Test giao diện | webapp-testing |
| Test toàn diện trước PR | Plugin kiểm thử riêng của bạn (xem [Dùng Claude để test web app và mobile app](claude-test-web-mobile.md)) |
| Làm gọn code | code-simplifier |
| Mở PR | `/commit-push-pr` |
| Review | `/code-review` hoặc `/pr-review-toolkit:review-pr` |
| Dọn nhánh | `/clean_gone` |

### Một đợt phát hành (PM)

| Bước | Dùng |
| --- | --- |
| Viết PRD, báo cáo | doc-coauthoring + docx |
| Bảng kế hoạch, số liệu | xlsx |
| Slide demo cho khách | pptx + theme-factory / brand |
| Thông báo nội bộ, release note | internal-comms |

## Xử lý sự cố

| Hiện tượng | Cách xử lý |
| --- | --- |
| Cài xong không thấy lệnh | Khởi động lại Claude Code; gõ `/` xem tên đúng (có thể có tiền tố `<plugin>:`); kiểm plugin đang bật trong `/plugin` |
| `Marketplace "claude-plugins-official" not found` | `/plugin marketplace add anthropics/claude-plugins-official` |
| Skill không tự kích hoạt | Gọi thẳng tên skill trong prompt hoặc dùng slash command |
| Hai plugin ép quy trình khác nhau | Tắt một cái (vd chỉ giữ feature-dev hoặc Superpowers) |
| `/commit-push-pr`, `/code-review` báo lỗi GitHub | Cài `gh`, chạy `gh auth login` |
| LSP plugin không chạy | Cài language server trên máy, kiểm nằm trong PATH |
| hookify không chặn | File luật nằm ở `.claude/` gốc dự án (hoặc `~/.claude/` cho mọi dự án), `enabled: true`; cần Python 3 |
| Plugin không có trong phiên cloud (claude.ai/code) | Phiên cloud không nạp plugin cài trên máy; dùng Claude Code trên máy hoặc bật plugin qua claude.ai |
| Claude chậm, tốn token | Gỡ bớt plugin/MCP không dùng |

## Nguồn

- [Claude plugins directory](https://claude.com/plugins) · [Commit Commands](https://claude.com/plugins/commit-commands) · [Hookify](https://claude.com/marketplace/plugins/hookify)
- [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · [anthropics/claude-code — plugins](https://github.com/anthropics/claude-code/tree/main/plugins)
- [anthropics/skills](https://github.com/anthropics/skills)
- [obra/superpowers](https://github.com/obra/superpowers) · [trailofbits/skills](https://github.com/trailofbits/skills)
- [Claude Code — Discover and install plugins](https://code.claude.com/docs/en/discover-plugins)
