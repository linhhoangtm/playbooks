# Claude Skill và Plugin: là gì, khi nào dùng, dùng thế nào

Cập nhật: 2026-11-12

Dành cho dev, BA, PM, designer đang dùng Claude hằng ngày và thấy mình **gõ lại cùng một đoạn hướng dẫn** quá nhiều lần. Đọc xong bạn sẽ biết skill và plugin là gì, khi nào nên dùng thay cho prompt thường, và tự tạo được cái đầu tiên.

## 1. Tổng quan

Claude có nhiều cách để "dạy" thêm. Chúng trông giống nhau nhưng giải bài toán khác nhau:

| Cách | Là gì | Ai kích hoạt | Ví dụ |
| --- | --- | --- | --- |
| **CLAUDE.md** | File hướng dẫn của dự án, Claude Code đọc mỗi phiên | Luôn nạp | Lệnh test, quy ước đặt tên, điều cấm |
| **Skill** | Thư mục có `SKILL.md` (+ file phụ, script) dạy Claude làm một việc cụ thể | Claude tự nạp khi thấy liên quan, hoặc bạn gõ `/tên` | Viết release note theo mẫu công ty |
| **Slash command** | Prompt lưu sẵn, gọi bằng `/tên` | Bạn | `/review`, `/pr` |
| **Subagent** | Một Claude khác, có context riêng, prompt riêng, giới hạn tool riêng | Claude giao việc hoặc bạn gọi | Agent chỉ đọc, chuyên rà bảo mật |
| **Hook** | Lệnh shell tự chạy trước/sau một hành động | Hệ thống, luôn luôn | Format code sau mỗi lần sửa, chặn sửa file `.env` |
| **MCP server** | Cổng nối Claude với công cụ ngoài | Claude gọi khi cần | GitHub, Figma, Jira, database |
| **Plugin** | Gói đóng nhiều thứ trên để cài 1 lần, chia sẻ cho cả team | Cài từ marketplace | Bộ kiểm thử: 1 skill + 6 agent |

Ba điều giúp phân biệt nhanh:

- **Skill là chữ Claude đọc; subagent là một Claude thứ hai.** Skill chạy trong cuộc trò chuyện hiện tại; subagent làm việc riêng rồi trả kết quả.
- **Skill là lời dặn, hook là luật.** Claude có thể đánh giá một skill không áp dụng; hook là code chạy mỗi lần sự kiện xảy ra. Quy tắc bắt buộc đúng 100% thì dùng hook.
- **Slash command giờ đã gộp vào skill.** File cũ `.claude/commands/<tên>.md` vẫn chạy, nhưng cả hai đều tạo lệnh `/tên` giống nhau. Viết mới thì viết skill.

## 2. Skill là gì

**Skill** (Agent Skill) là một thư mục chứa file `SKILL.md`: phần đầu là YAML (tên + mô tả), phần sau là hướng dẫn bằng markdown. Có thể kèm file tham khảo, mẫu, script.

```
release-note/
├── SKILL.md            # bắt buộc: tên, mô tả, hướng dẫn
├── references/         # tài liệu chi tiết, chỉ đọc khi cần
│   └── vi-du.md
├── templates/          # mẫu output
└── scripts/            # script Claude chạy được
```

```markdown
---
name: release-note
description: Viết release note tiếng Việt từ git log theo mẫu của team. Dùng khi user nói "viết release note", "có gì mới", "chuẩn bị phát hành".
---

# Viết release note
1. Chạy `git log <tag cũ>..HEAD --oneline`.
2. ...
```

### Claude nạp skill thế nào: từng lớp một

Skill dùng nguyên tắc **progressive disclosure**, nạp thông tin dần theo nhu cầu:

| Lớp | Nạp khi nào | Nội dung |
| --- | --- | --- |
| 1. Metadata | Luôn có trong context | `name` + `description` — vài chục token mỗi skill |
| 2. Thân `SKILL.md` | Khi yêu cầu khớp với mô tả | Quy trình, quy tắc, ví dụ |
| 3. File phụ | Khi `SKILL.md` chỉ tới và cần thật | Tham khảo dài, mẫu, script |

Hệ quả: cài nhiều skill gần như không tốn context, và **phần `description` quyết định skill có được dùng hay không**. Mô tả mơ hồ → Claude không biết lúc nào dùng; mô tả quá rộng → skill nhảy vào việc không liên quan.

### Dùng ở đâu

Cùng một format skill chạy được trên claude.ai, Claude Code, Claude Agent SDK và Claude API; chỉ khác cách cài:

| Nơi dùng | Cách cài |
| --- | --- |
| **claude.ai / app Claude** | Settings → mục Skills, tải lên file .zip; hoặc nhờ Claude tạo skill ngay trong chat |
| **Claude Code — cá nhân** | `~/.claude/skills/<tên>/SKILL.md` — dùng cho mọi dự án trên máy |
| **Claude Code — dự án** | `.claude/skills/<tên>/SKILL.md` trong repo — commit để cả team dùng |
| **Claude Code — qua plugin** | `<plugin>/skills/<tên>/SKILL.md` |
| **Claude API** | Tải lên qua Skills API, gắn `skill_id` khi gọi |

Claude cũng có sẵn skill dựng sẵn của Anthropic (Word, Excel, PowerPoint, PDF…) và skill **skill-creator** để giúp bạn viết skill mới.

## 3. Plugin là gì

**Plugin** là một thư mục đóng gói skill, subagent, hook, MCP server (và slash command kiểu cũ) kèm file khai báo `.claude-plugin/plugin.json`, để Claude Code cài và nạp cả gói một lần. Plugin không phải một loại riêng — nó là **cách phân phối** các thứ ở mục 1.

```
kiem-thu/
├── .claude-plugin/
│   └── plugin.json         # tên, phiên bản, mô tả (bắt buộc)
├── skills/
│   └── chay/SKILL.md       # gọi bằng /kiem-thu:chay
├── agents/
│   ├── bao-mat.md
│   └── chay-test.md
├── hooks/hooks.json        # tuỳ chọn
└── .mcp.json               # tuỳ chọn
```

Lưu ý: chỉ `plugin.json` nằm trong `.claude-plugin/`; các thư mục `skills/`, `agents/`, `hooks/` nằm ở gốc plugin.

### Marketplace

**Marketplace** là một repo git (hoặc thư mục) có file `.claude-plugin/marketplace.json` liệt kê các plugin. Thêm marketplace một lần, sau đó cài từng plugin:

```
/plugin marketplace add <owner/repo | URL git | đường dẫn local>
/plugin install <plugin>@<marketplace>
```

| Marketplace | Nội dung |
| --- | --- |
| `claude-plugins-official` | Marketplace chính thức của Anthropic, có sẵn khi mở Claude Code. Duyệt bằng `/plugin` → tab Discover hoặc trên claude.com/plugins |
| `anthropics/claude-plugins-community` | Plugin bên thứ ba đã qua kiểm tra tự động và sàng lọc bảo mật của Anthropic |
| `anthropics/claude-code` | Plugin mẫu để học |
| Marketplace của bạn / công ty | Repo riêng (public hoặc private), hoặc thư mục trên máy |

Plugin còn dùng được trên claude.ai (bật cho cá nhân hoặc cả tổ chức), và Claude Code tự đồng bộ những plugin đó vào phiên làm việc.

## 4. Lợi ích

| Lợi ích | Prompt thường | Skill / plugin |
| --- | --- | --- |
| **Không lặp lại** | Dán lại hướng dẫn mỗi lần | Viết một lần, gọi bằng 1 câu hoặc `/tên` |
| **Kết quả ổn định** | Mỗi người viết prompt một kiểu | Cả team cùng quy trình, cùng mẫu output |
| **Tiết kiệm context** | Hướng dẫn dài nằm trong mọi cuộc chat | Chỉ nạp khi cần (progressive disclosure) |
| **Đóng gói kinh nghiệm** | Nằm trong đầu người giỏi nhất team | Thành file, người mới dùng ngay được |
| **Kèm công cụ** | Chỉ có chữ | Kèm mẫu, script, subagent, hook, kết nối MCP |
| **Quản lý phiên bản** | Prompt nằm rải rác trong chat | Nằm trong git, review được, có version |
| **Chia việc song song** | Một Claude làm tuần tự | Plugin có nhiều subagent chạy cùng lúc, mỗi cái một context sạch |

## 5. Khi nào dùng cái nào

Hỏi lần lượt, dừng ở câu đầu tiên trả lời **có**:

1. Phải xảy ra mọi lần, không để AI tự quyết? → **Hook** (vd format code, chặn sửa `.env`)
2. Cần đọc / ghi công cụ, dữ liệu bên ngoài? → **MCP server** (vd GitHub, Figma, database)
3. Việc nặng, cần context riêng hoặc chạy song song? → **Subagent** (vd rà bảo mật, chạy test song song)
4. Quy tắc chung mà phiên nào cũng cần? → **CLAUDE.md** (vd lệnh test, quy ước, điều cấm)
5. Quy trình lặp lại cho một loại việc? → **Skill** (vd release note, review theo checklist)
6. Không câu nào "có" → prompt thường là đủ.

**Plugin** không phải một lựa chọn riêng: nó gói skill + subagent + hook + MCP ở trên để cài 1 lần, chia sẻ cho team.

Thứ tự hỏi quan trọng: cái gì **bắt buộc** đặt vào hook trước, vì skill và CLAUDE.md chỉ là lời dặn Claude có thể bỏ qua. Các cách kết hợp được với nhau: hook chạy linter, skill dạy Claude sửa lỗi linter báo.

**Dấu hiệu nên tạo skill:**

- Bạn đã dán cùng một đoạn hướng dẫn vào chat từ 3 lần trở lên.
- Có một mẫu output cố định (báo cáo, release note, tài liệu bàn giao).
- Có kiến thức riêng của team mà Claude không tự biết (quy trình duyệt, quy tắc nghiệp vụ, giọng văn thương hiệu).
- Người mới vào team hay làm sai cùng một việc.

**Dấu hiệu nên gói thành plugin:**

- Nhiều người hoặc nhiều repo cần cùng bộ công cụ.
- Bộ công cụ gồm nhiều phần phải đi cùng nhau (skill điều phối + vài subagent + hook).
- Cần cập nhật phiên bản cho cả team một lần thay vì copy file tay.

## 6. Dùng thế nào

### 6.1 Tạo skill trên claude.ai (không cần code)

Cách nhanh nhất: làm việc đó với Claude một lần cho đến khi ra kết quả ưng ý, rồi nhờ Claude đóng gói:

```
Biến quy trình mình vừa làm trong cuộc chat này thành một skill.
Tên: <ten-ngan-khong-dau>. Dùng khi: <các câu mình hay nói để nhờ việc này>.
Giữ: các bước, mẫu output, những chỗ mình đã sửa bạn. Bỏ: thông tin riêng của lần này.
```

Claude sẽ hiện thẻ đề xuất skill để bạn xem và lưu. Hoặc tự viết thư mục skill, nén .zip và tải lên trong Settings. Sau đó chỉ cần nói tự nhiên ("viết release note cho bản 2.3"), Claude tự nhận ra và dùng skill.

### 6.2 Tạo skill trong Claude Code

```bash
mkdir -p .claude/skills/release-note      # skill của dự án (commit để team dùng)
# hoặc ~/.claude/skills/release-note      # skill cá nhân, dùng mọi dự án
```

Viết `SKILL.md` (xem ví dụ 7.1), rồi gọi bằng `/release-note` hoặc nói tự nhiên. Có thể nhờ luôn Claude Code viết:

```
Tạo skill .claude/skills/<tên>/SKILL.md cho việc: <mô tả>.
Description nói rõ làm gì và khi nào dùng. Thân file dưới ~500 dòng, chi tiết dài để ở references/.
Dùng đúng lệnh có trong repo (đọc package.json / Makefile / CLAUDE.md), không bịa.
```

### 6.3 Cài plugin có sẵn

```
/plugin                                       # mở trình quản lý plugin, tab Discover
/plugin install commit-commands@claude-plugins-official
/commit-commands:commit                       # lệnh của plugin có tiền tố tên plugin
```

Khi cài sẽ chọn phạm vi: chỉ mình bạn, cả dự án (ghi vào cấu hình repo), hoặc chỉ trên máy này. Quản lý, tắt, gỡ trong `/plugin`.

### 6.4 Tạo plugin + marketplace để chia sẻ cho team

```
team-plugins/                       # repo git (private cũng được)
├── .claude-plugin/
│   └── marketplace.json
└── plugins/
    └── kiem-thu/
        ├── .claude-plugin/plugin.json
        ├── skills/chay/SKILL.md
        └── agents/*.md
```

`marketplace.json`:

```json
{
  "name": "team-plugins",
  "owner": { "name": "<tên bạn>" },
  "plugins": [
    { "name": "kiem-thu", "source": "./plugins/kiem-thu", "description": "Kiểm thử toàn bộ project bằng 1 lệnh" }
  ]
}
```

`plugin.json`:

```json
{ "name": "kiem-thu", "version": "0.1.0", "description": "Kiểm thử toàn bộ project bằng 1 lệnh" }
```

Kiểm tra và chia sẻ:

```bash
claude plugin validate .                          # kiểm cấu trúc trước khi đưa lên
/plugin marketplace add <owner>/team-plugins      # mỗi người chạy 1 lần (hoặc đường dẫn local)
/plugin install kiem-thu@team-plugins
```

Khi đang phát triển, không cần marketplace: nạp thẳng bằng `claude --plugin-dir ./plugins/kiem-thu`. Nhớ **tăng `version`** mỗi lần sửa để máy khác nhận bản mới.

## 7. Ví dụ cụ thể

### 7.1 Skill viết release note (dùng được cả claude.ai lẫn Claude Code)

```markdown
---
name: release-note
description: Viết release note tiếng Việt từ git log hoặc danh sách thay đổi, theo mẫu của team. Dùng khi user nói "viết release note", "có gì mới", "nội dung cập nhật lên store".
---

# Viết release note

## Đầu vào
- Có repo: chạy `git log <tag trước>..HEAD --oneline --no-merges`. Không biết tag thì hỏi.
- Không có repo: dùng danh sách user dán vào.

## Viết 2 bản
1. **Cho người dùng** (đăng lên App Store / Google Play): tối đa 5 gạch đầu dòng, mỗi dòng bắt đầu bằng động từ,
   nói lợi ích, không thuật ngữ, ≤ 500 ký tự. Bỏ commit chỉ là refactor / test / CI.
2. **Cho team**: nhóm theo Tính năng / Sửa lỗi / Kỹ thuật; ghi migration, biến môi trường mới, cách rollback.

## Quy tắc
- Không bịa tính năng không có trong log.
- Commit mơ hồ ("fix", "update") → liệt kê cuối báo cáo để user xác nhận.
- Mẫu chi tiết: xem `templates/mau.md`.
```

Dùng: gõ "viết release note bản 2.3" hoặc `/release-note`.

### 7.2 Skill quy ước code của team (Claude Code, đặt trong repo)

Giúp Claude tự theo quy ước khi tạo màn hình mới, không cần nhắc.

```markdown
---
name: tao-man-flutter
description: Tạo màn hình / feature Flutter mới theo cấu trúc của repo này. Dùng khi user yêu cầu thêm màn, thêm tab, thêm feature trong app.
---

# Tạo màn Flutter
1. Đặt trong `lib/features/<ten>/`: `<ten>_screen.dart`, `<ten>_controller.dart`, `<ten>_data.dart`.
2. Khai báo route trong `lib/app/router/routes.dart`; menu chỉ sửa ở `nav_items.dart`.
3. Màn có đủ 4 trạng thái: loading, có dữ liệu, rỗng, lỗi. Dùng widget `EmptyState`, `ErrorView` có sẵn.
4. Chữ trên UI lấy từ file i18n, không hardcode.
5. Thêm widget test `test/features/<ten>_test.dart` cho 4 trạng thái.
6. Chạy `dart format` + `flutter analyze` + test vừa viết.
Mẫu đầy đủ: `references/vi-du-man.md`.
```

(Đường dẫn và tên widget là ví dụ — thay bằng cấu trúc thật của repo bạn.)

### 7.3 Plugin kiểm thử nhiều agent: `kiem-thu`

> Ví dụ minh họa cách tổ chức một plugin nhiều agent, chưa phát hành công khai. Dựng theo cấu trúc này cho nhu cầu của bạn.

Bài toán: mỗi lần thêm tính năng phải chạy cả chục prompt test (5 nhóm case, security, performance, UI, store…). Giải pháp: 1 plugin, gõ 1 lệnh.

| Thành phần | Vai trò |
| --- | --- |
| Skill `chay` | Điều phối: đọc cấu hình `.claude/kiem-thu.md` của repo, xác định phần code đổi (git diff), giao việc, gộp báo cáo |
| Agent `chay-test` | Chạy lint, unit test, regression có sẵn; phân tích vì sao fail |
| Agent `thiet-ke-case` | Lập ma trận 5 nhóm case, tìm case còn thiếu |
| Agent `bao-mat` | Kiểm quyền / IDOR, secrets, chống bot, tấn công tính năng AI |
| Agent `hieu-nang` | N+1, thiếu index, memory leak |
| Agent `giao-dien` | 4 trạng thái màn, text dài, a11y |
| Agent `cua-hang` | Rủi ro bị App Store / Google Play từ chối |

Dùng:

```
/kiem-thu:chay init        # lần đầu mỗi repo: tạo file cấu hình
/kiem-thu:chay             # sau mỗi tính năng: test phần vừa đổi
/kiem-thu:chay release     # trước khi nộp store: test toàn bộ + rà rủi ro store
```

Kết quả là một file markdown: checklist, bảng test case (input, output mong đợi, output thực tế, pass/fail, cách sửa). Các agent được giới hạn tool (phần lớn chỉ đọc), không commit, không sửa code ứng dụng. Đây là lý do nên dùng plugin: **1 skill + 6 agent phải đi cùng nhau**, cài 1 lần cho cả team.

### 7.4 Ý tưởng skill theo vai

| Vai | Skill nên có |
| --- | --- |
| PM | Viết PRD theo mẫu công ty; tóm tắt phản hồi khách hàng thành bảng vấn đề |
| BA | User story + acceptance criteria 5 nhóm; tài liệu bàn giao dev |
| Designer | Design system thương hiệu; rà UI theo checklist a11y |
| Dev | Tạo màn / API theo cấu trúc repo; viết migration an toàn; review PR theo checklist |
| Marketing / sales | Viết bài đúng giọng thương hiệu; trả lời email khách theo kịch bản |

## 8. Viết skill tốt, lỗi thường gặp, an toàn

### Viết skill tốt

- **Description là phần quan trọng nhất.** Nói rõ *làm gì* và *khi nào dùng*, kèm những câu người dùng hay nói. Tránh mô tả chung chung kiểu "xử lý file".
- **Ngắn gọn.** Context là tài nguyên chung với system prompt, lịch sử chat và các skill khác. Thân `SKILL.md` nên dưới ~500 dòng, chi tiết dài để ở `references/`.
- **Chỉ ghi điều Claude không tự biết.** Quy trình riêng, mẫu riêng, bẫy đã gặp. Không giảng lại kiến thức phổ thông.
- **Có ví dụ input → output.** Một ví dụ tốt rõ hơn mười dòng mô tả.
- **Việc cần chính xác thì giao cho script.** Đổi định dạng, tính toán, validate: viết script trong `scripts/`, skill bảo Claude chạy.
- **Test trước khi chia sẻ.** Thử 3–5 yêu cầu nên kích hoạt và vài yêu cầu *không* nên kích hoạt. Skill **skill-creator** có sẵn quy trình này.

### Lỗi thường gặp

| Lỗi | Hậu quả | Cách sửa |
| --- | --- | --- |
| Description mơ hồ | Claude không bao giờ tự dùng skill | Thêm "Dùng khi…" + từ khóa người dùng hay nói |
| Description quá rộng | Skill nhảy vào việc không liên quan | Thu hẹp phạm vi, nói rõ khi nào *không* dùng |
| Nhồi mọi thứ vào `SKILL.md` | Tốn context, Claude bỏ sót ý chính | Tách ra `references/`, `SKILL.md` chỉ là mục lục + quy trình |
| Dùng skill cho quy tắc bắt buộc | Claude đôi khi bỏ qua | Chuyển sang hook |
| Viết lệnh không có trong repo | Claude chạy lệnh sai | Chép đúng lệnh từ `package.json` / `CLAUDE.md` |
| Sửa plugin mà không tăng `version` | Máy khác không nhận bản mới | Tăng version ở `plugin.json` (và `marketplace.json`) |
| Đặt `skills/`, `agents/` trong `.claude-plugin/` | Plugin không nạp được | Chỉ `plugin.json` nằm trong `.claude-plugin/` |

### An toàn

- **Skill và plugin có thể chạy code.** Plugin có thể chạy hook và MCP server trên máy bạn. Đọc nội dung trước khi cài, nhất là từ marketplace bên thứ ba — Anthropic không duyệt marketplace của người khác.
- **Không để secret trong skill.** API key, mật khẩu, URL nội bộ không đưa vào `SKILL.md` hay repo marketplace public.
- **Giới hạn tool cho subagent.** Agent chỉ cần đọc thì chỉ cấp `Read, Grep, Glob`; cấm commit / push / cài dependency ngay trong prompt của agent.
- **Marketplace riêng cho nội dung riêng.** Skill chứa quy trình nội bộ, tên endpoint, cấu trúc dự án thì để ở repo private hoặc thư mục local.

## 9. Skill và plugin nên thử

Danh sách thay đổi nhanh. Kiểm tra bản mới nhất bằng `/plugin` → tab Discover hoặc trên claude.com/plugins.

Mục này chỉ giới thiệu tổng quát. Cách cài, lệnh gọi, prompt mẫu và mẹo cho từng cái: xem [Cách dùng các skill và plugin thông dụng của Claude](claude-skill-plugin-thong-dung.md).

### 9.1 Skill của Anthropic (repo `anthropics/skills`)

Cài trong Claude Code:

```
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills     # docx + pdf + pptx + xlsx
/plugin install example-skills@anthropic-agent-skills      # các skill còn lại
```

Trên claude.ai, các skill tài liệu đã có sẵn và bật trong Settings; skill khác tải .zip từ repo lên.

| Skill | Làm gì | Hợp với |
| --- | --- | --- |
| **docx, xlsx, pptx, pdf** | Tạo, đọc, sửa file Word, Excel, PowerPoint, PDF thật (giữ công thức, định dạng). Đây là bộ skill chạy tính năng tạo file của claude.ai | Ai cũng cần: báo cáo, bảng tính, slide |
| **skill-creator** | Hướng dẫn viết skill mới, test và đo hiệu quả skill | Bước tiếp theo sau khi dùng thử vài skill |
| **frontend-design** | Giao diện có cá tính, tránh kiểu "trang nào do AI làm cũng giống nhau" | Dev web, designer làm prototype bằng code |
| **webapp-testing** | Dùng Playwright mở web app local: kiểm chức năng, chụp màn hình, đọc log trình duyệt | Test UI web |
| **mcp-builder** | Quy trình xây MCP server (Python FastMCP hoặc TypeScript) | Muốn nối Claude với API riêng |
| **claude-api** | Xây app dùng Claude API và SDK của Anthropic | Dev tích hợp AI vào sản phẩm |
| **web-artifacts-builder** | Artifact HTML nhiều component (React, Tailwind, shadcn/ui) trên claude.ai | Prototype tương tác nhanh |
| **brand-guidelines, theme-factory** | Áp màu, font, phong cách thương hiệu cho output | Marketing, tài liệu nội bộ |
| **internal-comms, doc-coauthoring** | Viết thông báo nội bộ, cùng soạn tài liệu | PM, quản lý |
| **canvas-design, algorithmic-art** | Tạo hình ảnh PNG/PDF, nghệ thuật tạo sinh bằng code | Poster, hình minh họa |

Lưu ý license: phần lớn skill trong repo là Apache 2.0; riêng docx, pdf, pptx, xlsx là source-available, xem được nhưng không phải mã nguồn mở.

### 9.2 Plugin chính thức (marketplace `claude-plugins-official`)

Marketplace này có sẵn, cài thẳng: `/plugin install <tên>@claude-plugins-official`.

| Plugin | Làm gì | Khi nào dùng |
| --- | --- | --- |
| **commit-commands** | Lệnh commit, push, tạo PR | Plugin đầu tiên nên thử, dùng hằng ngày |
| **feature-dev** | Quy trình làm tính năng nhiều giai đoạn, có agent khám phá codebase, thiết kế kiến trúc, review | Tính năng vừa và lớn |
| **code-review** | Review PR bằng nhiều agent song song, có điểm tin cậy để lọc nhiễu | Trước khi merge. Claude Code bản mới đã có sẵn `/code-review`, `/simplify`: gõ `/` kiểm trước khi cài |
| **pr-review-toolkit** | Bộ agent review theo từng mảng: test, xử lý lỗi, comment, thiết kế type, đơn giản hóa code | Team review PR thật sự |
| **security-guidance** | Cảnh báo mẫu code nguy hiểm khi sửa file, review diff khi xong | Bật luôn, đặc biệt khi Claude viết nhiều code |
| **frontend-design** | Phiên bản plugin của skill frontend-design | Mọi việc có UI |
| **hookify** | Tạo hook bằng quy tắc viết markdown, không cần viết script | Muốn chặn hành vi không mong muốn |
| **code-simplifier** | Agent làm gọn code, giữ nguyên chức năng | Sau khi code chạy được, trước khi review |
| **plugin-dev, skill-creator, mcp-server-dev** | Công cụ tự xây plugin, skill, MCP server | Khi bắt đầu đóng gói quy trình cho team |
| **claude-md-management** | Quản lý, cập nhật CLAUDE.md | Dự án dài hơi |
| **LSP plugin** (vd `pyright-lsp`, `gopls-lsp`, `rust-analyzer-lsp`, `csharp-lsp`) | Cho Claude "hiểu" code như IDE: đi tới định nghĩa, tìm tham chiếu, báo lỗi type | Cài 1 cái cho ngôn ngữ chính. Cần cài language server trên máy trước |
| **github, supabase, context7…** | Tích hợp đối tác: GitHub (repo, PR), Supabase (DB, auth), Context7 (tài liệu thư viện cập nhật) | Khi dùng dịch vụ đó |

### 9.3 Của cộng đồng, được dùng nhiều

| Tên | Làm gì | Cài |
| --- | --- | --- |
| **Superpowers** (obra / Jesse Vincent) | Bộ skill tự kích hoạt: brainstorm, lập kế hoạch, TDD, debug có hệ thống, review. Ép Claude theo quy trình kỷ luật cho việc dài | `/plugin install superpowers@claude-plugins-official` |
| **Trail of Bits skills** | Bộ skill bảo mật của công ty audit Trail of Bits: static analysis (CodeQL, Semgrep), differential review, tìm cấu hình mặc định không an toàn | Marketplace `trailofbits/skills` |
| **wshobson/agents** | Thư viện lớn subagent theo chuyên môn (backend, DevOps, data…) | Marketplace `wshobson/agents` — chỉ cài phần cần |
| **Skill của chính hãng công cụ** | Vercel, Supabase, Cloudflare, Sentry… tự phát hành skill/plugin cho sản phẩm của họ | Ưu tiên nguồn này khi dùng công cụ đó |

Hệ sinh thái rất lớn (hàng chục nghìn repo có skill trên GitHub) nên chất lượng không đều. Trước khi cài đồ cộng đồng: đọc `SKILL.md`, hook và cấu hình MCP; ưu tiên repo của chính hãng hoặc tổ chức uy tín; cài ít, bỏ cái không dùng.

### 9.4 Bộ khởi động gợi ý theo vai

| Vai | Cài trước |
| --- | --- |
| **Dev fullstack** | LSP cho ngôn ngữ chính · commit-commands · security-guidance · code-review hoặc pr-review-toolkit · webapp-testing |
| **Dev frontend / mobile** | frontend-design · webapp-testing · commit-commands · code-review |
| **Làm việc dài, tính năng lớn** | feature-dev hoặc Superpowers (chọn một, đừng bật cả hai cùng lúc) |
| **PM, BA, văn phòng** | docx · xlsx · pptx · pdf · doc-coauthoring · internal-comms |
| **Designer** | frontend-design · brand-guidelines · canvas-design · web-artifacts-builder |
| **Muốn tự đóng gói quy trình** | skill-creator · plugin-dev · hookify |

## Nguồn

- [Equipping agents for the real world with Agent Skills — Anthropic](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Skill authoring best practices — Claude Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Agent Skills overview — Claude Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Claude Code — Plugins overview](https://code.claude.com/docs/en/plugins/overview) · [Install plugins](https://code.claude.com/docs/en/plugins/install) · [Discover plugins](https://code.claude.com/docs/en/discover-plugins) · [Plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [Claude Code — Subagents](https://code.claude.com/docs/en/sub-agents)
- [anthropics/skills — GitHub](https://github.com/anthropics/skills) · [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)
- [Claude plugins directory](https://claude.com/plugins)
- [Superpowers](https://github.com/obra/superpowers) · [Trail of Bits skills](https://github.com/trailofbits/skills)
