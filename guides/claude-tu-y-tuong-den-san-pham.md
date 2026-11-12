# Hướng dẫn dùng Claude xây dựng sản phẩm từ ý tưởng

Cập nhật: 2026-11-12

Đi từ ý tưởng đến app đã phát hành qua 9 giai đoạn. Mỗi giai đoạn dùng công cụ phù hợp của Claude và ra một deliverable cụ thể, rồi deliverable đó làm context cho giai đoạn sau. Ví dụ xuyên suốt: app mobile **Flutter**, backend **Go hoặc FastAPI**, database **PostgreSQL**.

| # | Giai đoạn | Công cụ chính | Deliverable |
| --- | --- | --- | --- |
| 1 | Kiểm chứng ý tưởng | Chat + Research | `IDEA_BRIEF.md` |
| 2 | Đặc tả sản phẩm | Chat trong Project | `PRD.md`, scope MVP |
| 3 | Kiến trúc | Chat trong Project | `ARCHITECTURE.md`, schema, `openapi.yaml` |
| 4 | Thiết kế UI/UX | Claude Design | Mockup, design system |
| 5 | Lập kế hoạch | Chat hoặc Sheets | `ROADMAP.md` |
| 6 | Build | Claude Code | Repo chạy được |
| 7 | Test và review | Claude Code + Chrome | Test pass, review xong |
| 8 | Deploy và phát hành | Claude Code + Chrome | CI/CD, app trên store |
| 9 | Vận hành | Chat + Scheduled tasks | Task cho vòng tiếp theo |

Giai đoạn 6 chiếm nhiều thời gian nhất. Sau khi phát hành, giai đoạn 9 tạo task mới và vòng lặp quay lại từ giai đoạn 5.

## Mục lục

- [0. Nền tảng](#0-nền-tảng-đúng-công-cụ-cho-đúng-việc)
- [1. Ý tưởng → kiểm chứng thị trường](#1-ý-tưởng--kiểm-chứng-thị-trường)
- [2. Đặc tả sản phẩm (PRD)](#2-đặc-tả-sản-phẩm-prd-và-scope-mvp)
- [3. Kiến trúc](#3-kiến-trúc-chọn-theo-quy-mô-không-theo-trend)
- [4. Thiết kế UI/UX](#4-thiết-kế-uiux)
- [5. Lập kế hoạch](#5-lập-kế-hoạch-chia-nhỏ-để-claude-code-làm-tốt)
- [6. Build với Claude Code](#6-build-với-claude-code)
- [7. Test và review](#7-test-và-review)
- [8. Deploy và phát hành](#8-deploy-và-phát-hành)
- [9. Vận hành và cải tiến](#9-vận-hành-và-cải-tiến)
- [Phụ lục](#phụ-lục)

## 0. Nền tảng: đúng công cụ cho đúng việc

| Công cụ | Dùng khi | Deliverable điển hình |
| --- | --- | --- |
| Chat + Web search / Research | Brainstorm, phản biện, nghiên cứu thị trường | Idea Brief |
| Projects | Lưu context chung: PRD, kiến trúc, quyết định, custom instructions | “Bộ não” của dự án |
| Artifacts: Docs, Sheets, Slides | Viết tài liệu, backlog, pitch | PRD, backlog, deck |
| Claude Design | Wireframe, mockup, prototype bấm thử, design system | Mockup màn hình chính |
| Mermaid trong chat | User flow, ERD, sơ đồ kiến trúc dạng văn bản, lưu được vào repo | Sơ đồ trong `docs/` |
| Claude Code | Viết code, refactor, chạy test, git, chạy lệnh | Repo chạy được |
| Claude in Chrome | Test UI web, thao tác trên console của store, đọc dashboard | Báo cáo bug, checklist release |
| Scheduled tasks | Việc lặp lại theo lịch | Báo cáo review hằng tuần |

### Thiết lập Project (làm một lần)

1. Tạo một Project đặt tên theo dự án, ví dụ `Expense App`.
2. Dán custom instructions mẫu bên dưới vào Project.
3. Sau mỗi giai đoạn, lưu deliverable (Idea Brief, PRD, ARCHITECTURE…) vào Project để các chat sau tự có context.

```text
Bạn là tech lead cho dự án <tên app>. Stack: Flutter (BLoC), Go hoặc FastAPI, PostgreSQL.
- Trước khi trả lời, đọc PRD.md và ARCHITECTURE.md trong Project.
- Với quyết định kỹ thuật: đưa 2–3 phương án kèm trade-off rồi mới đề xuất.
- Thiếu thông tin thì hỏi lại, không tự giả định.
- Trả lời bằng tiếng Việt, giữ thuật ngữ kỹ thuật bằng tiếng Anh, ngắn gọn.
```

### 5 nguyên tắc vàng

- **Context quan trọng hơn prompt hay.** Hãy đưa PRD, schema và code mẫu thay vì mô tả bằng lời.
- **Mỗi phiên làm một việc.** Phiên lẫn nhiều chủ đề làm Claude dễ nhầm và tốn token.
- **Bắt Claude hỏi trước.** Thêm câu “Hỏi tôi tối đa 5 câu nếu còn thiếu thông tin” vào prompt.
- **Claude đề xuất, bạn quyết định.** Kiến trúc, schema, bảo mật và chi phí là những thứ bạn phải tự duyệt.
- **Luôn kiểm chứng.** Chạy test, đọc diff, mở lại nguồn tham khảo. Đừng tin output khi chưa kiểm tra.

## 1. Ý tưởng → kiểm chứng thị trường

Mục tiêu: trả lời “có nên làm không?” **trước khi viết dòng code đầu tiên**. Giai đoạn này dùng Chat với Web search hoặc Research được bật, và ra một `IDEA_BRIEF.md` kèm kết luận Go hoặc No-go.

1. **Phản biện ý tưởng.** Yêu cầu Claude đóng vai nhà đầu tư khó tính, không khen.
2. **Nghiên cứu thị trường thật.** Tìm đối thủ, lượt tải, review 1–2 sao, giá bán. Phải có link nguồn.
3. **Tìm “khe hở”.** Đối thủ bị chê điểm gì mà bạn làm tốt hơn được?
4. **Chốt Go hoặc No-go.** Nếu không tìm được bằng chứng là có người cần, dừng lại hoặc đổi hướng.

Prompt đầy đủ của giai đoạn này (làm rõ ý tưởng, chọn chỉ số…) ở [prompts/y-tuong-va-prd.md](../prompts/y-tuong-va-prd.md).

**Prompt mẫu: phản biện**

```text
Đóng vai nhà đầu tư khó tính. Đọc brief sau và chỉ ra:
- 5 lý do ý tưởng này sẽ thất bại, xếp theo mức nguy hiểm
- giả định nào mình đang coi là đúng mà chưa có bằng chứng, và cách kiểm tra nó trong 1 tuần không cần code
- ai đang trả tiền để giải quyết vấn đề này hôm nay
- nếu chỉ được làm 1 tính năng, đó là gì
Không khen. Brief: <dán>
```

**Prompt mẫu: nghiên cứu thị trường (bật Research)**

```text
Tìm trên web các sản phẩm đang giải quyết vấn đề: <vấn đề>, ưu tiên thị trường <Việt Nam / quốc tế>.
Với 5–10 sản phẩm nổi bật: nền tảng, lượt tải hoặc traffic, làm tốt gì, user phàn nàn gì
(review 1–2 sao trên App Store / Google Play, diễn đàn), giá, mô hình kiếm tiền.
Có tín hiệu nhu cầu nào không (nhóm Facebook, Reddit, lượng tìm kiếm)?
Kết luận: khoảng trống còn lại, 3 rủi ro lớn nhất khiến ý tưởng này thất bại,
3 cách kiểm chứng rẻ nhất trong 2 tuần, Go / No-go kèm 3 lý do.
Ghi nguồn cho từng nhận định. Không có nguồn thì ghi rõ là suy đoán.
```

**Prompt mẫu: chốt Idea Brief**

```text
Tổng hợp thành IDEA_BRIEF.md (tối đa 1 trang): vấn đề, người dùng, giải pháp,
đối thủ và khe hở, mô hình kiếm tiền, rủi ro lớn nhất, kết luận.
```

**Lỗi hay gặp:** hỏi “ý tưởng này hay không?”. Claude sẽ có xu hướng trả lời lạc quan. Hãy luôn hỏi “vì sao nó thất bại?” và đòi link nguồn.

## 2. Đặc tả sản phẩm (PRD) và scope MVP

PRD là “hợp đồng” giữa bạn và Claude: mọi giai đoạn sau đều tham chiếu nó. Giai đoạn này dùng Chat trong Project và ra `PRD.md` (lưu vào Project).

PRD theo mẫu [templates/PRD.md](../templates/PRD.md), gọn trong 1 trang:

- **Bối cảnh, mục tiêu** và 1–2 chỉ số thành công, ví dụ 100 user hoạt động tuần sau 1 tháng.
- **Persona** (1–2) và **user journey chính** (5–7 bước).
- **Tính năng** xếp theo MoSCoW (Must, Should, Could, Won’t) và **ngoài phạm vi**.
- **Giả định cần kiểm chứng.**
- **Ràng buộc và yêu cầu phi chức năng:** nền tảng, offline, bảo mật, số user dự kiến.
- **Câu hỏi mở.**

User story và acceptance criteria viết riêng theo [templates/user-story.md](../templates/user-story.md), lưu ở `docs/features/`, để PRD không phình to (prompt ở [prompts/phan-tich-nghiep-vu.md](../prompts/phan-tich-nghiep-vu.md)).

**Prompt mẫu: để Claude phỏng vấn bạn**

```text
Dựa trên IDEA_BRIEF.md trong Project, hãy phỏng vấn tôi để viết PRD.
Hỏi từng nhóm 3–5 câu: người dùng, tính năng, dữ liệu, nền tảng, kiếm tiền.
Khi đủ thông tin, viết PRD.md theo mẫu templates/PRD.md (9 mục). Không viết user story,
không viết giải pháp kỹ thuật. Giả định nào bạn tự thêm thì đánh dấu [GIẢ ĐỊNH].
```

**Prompt mẫu: cắt scope**

```text
Xếp các tính năng trong PRD theo MoSCoW (MUST / SHOULD / COULD / WON'T) cho MVP
làm trong <4> tuần với <1> người. MUST = thiếu nó thì user không hoàn thành được journey chính.
Bảng: tính năng | nhóm | lý do | ước lượng S/M/L.
Phản biện mình nếu MUST chiếm > 40% tổng số.
```

Với 1 người làm trong 4 tuần, MUST thường chỉ còn 3–5 tính năng: đủ để đi hết journey chính và kiểm chứng giả định rủi ro nhất trong IDEA_BRIEF.

**Mẹo:** mở một chat mới, dán PRD vào và hỏi “Tìm 10 chỗ mơ hồ hoặc mâu thuẫn trong PRD này”. Một phiên mới không bị thiên vị bởi cuộc trò chuyện trước đó.

## 3. Kiến trúc: chọn theo quy mô, không theo trend

Nguyên tắc: **bắt đầu bằng một monolith chia module rõ** (modular monolith), chỉ tách thêm khi có số liệu chứng minh là cần. MVP ít logic phía server thì BaaS (Supabase, Firebase) còn nhanh hơn nữa. Cách chọn chi tiết theo từng yếu tố: [Chọn kiến trúc phần mềm phù hợp](chon-kien-truc-phan-mem.md#7-cây-quyết-định). Giai đoạn này ra `ARCHITECTURE.md`, schema/migration, `openapi.yaml` và các ADR (Architecture Decision Record).

### Kiến trúc theo quy mô

Các mốc user và dung lượng dưới đây chỉ là ước lượng để định hướng. Hãy dựa vào số liệu thật của bạn.

| Quy mô | Dấu hiệu | Kiến trúc | Stack ví dụ |
| --- | --- | --- | --- |
| Nhỏ (MVP) | Dưới ~10k user, dữ liệu dưới ~10 GB, 1 dev | Monolith chia module (1 API, 1 DB), hoặc BaaS nếu ít logic phía server | Flutter + Go/FastAPI + PostgreSQL, Docker Compose trên 1 VPS; hoặc Flutter + Supabase |
| Vừa | ~10k–500k user, hàng chục tới hàng trăm GB, có job nặng | Monolith + cache + queue + worker, read replica, object storage | Thêm Redis, worker (Asynq / Celery), S3/R2, CDN, PgBouncer |
| Lớn | Hơn ~500k user, dữ liệu cỡ TB, nhiều team | Tách service theo domain, event-driven, tách OLTP và OLAP | Kafka/NATS, partitioning/sharding, ClickHouse/BigQuery, Kubernetes |

### Khi dữ liệu lớn

| Vấn đề | Giải pháp |
| --- | --- |
| Query chậm | Index đúng (B-tree, GIN cho JSONB và full-text), kiểm tra bằng `EXPLAIN ANALYZE` |
| Phân trang chậm | Keyset/cursor pagination thay cho `OFFSET` |
| Bảng log/event tăng nhanh | Partition theo thời gian; dữ liệu time-series có thể dùng TimescaleDB |
| Báo cáo và analytics nặng | Không chạy trên DB chính. Đồng bộ sang ClickHouse/BigQuery hoặc dùng read replica |
| Tìm kiếm | Bắt đầu với Postgres FTS, chuyển sang Meilisearch/Elasticsearch khi cần |
| Ảnh, file | Lưu trên object storage + CDN, DB chỉ lưu URL |
| Xử lý hàng loạt | Queue + background worker, không xử lý trong request |
| Tìm kiếm AI (semantic) | Extension `pgvector` |
| Quá nhiều connection | PgBouncer, connection pool trong app |

### Go hay FastAPI?

- **Go:** hiệu năng và concurrency cao, hợp realtime/WebSocket, build ra một binary gọn để deploy.
- **FastAPI:** viết nhanh, hệ sinh thái AI/ML và xử lý dữ liệu mạnh.
- **Kết hợp:** Go làm core API, FastAPI làm service AI/data riêng. Chỉ nên làm vậy khi thật sự cần.

### Flutter: DI và offline theo quy mô

Tổ chức code theo feature-first, dùng BLoC/Cubit và repository pattern. Một codebase chạy được mobile, web và desktop. Riêng web cần SEO thì nên cân nhắc framework web (ví dụ Next.js) cho phần public.

- **DI:** app nhỏ **không cần get_it**. Dùng `RepositoryProvider` và `BlocProvider` có sẵn trong flutter_bloc, hoặc truyền qua constructor. Chỉ thêm get_it hay injectable khi app lớn, có nhiều module.
- **Offline-first khi người dùng hay mất mạng** (ghi chép, bán hàng, làm việc ngoài hiện trường): UI chỉ đọc từ local DB, repository tự đồng bộ với API khi có mạng. App chủ yếu xem nội dung online thì cache đơn giản là đủ, vì offline-first tốn thêm nhiều công cho đồng bộ và xử lý xung đột.
- **Đồng bộ an toàn:** mỗi bản ghi có cờ trạng thái sync, xóa bằng soft delete, id sinh ở client (UUID) để không trùng khi sync.

| Nhu cầu lưu local | Chọn |
| --- | --- |
| Token, refresh token, khóa bí mật | `flutter_secure_storage` (Keychain / Keystore). Không lưu trong Hive hay SharedPreferences |
| Key-value: settings, cache API đơn giản | `hive_ce`, bản cộng đồng còn được duy trì. Package `hive` gốc đã ngừng cập nhật |
| Dữ liệu nghiệp vụ có quan hệ, cần query, filter, join, nhiều bản ghi | `drift` (SQLite) |

Nhiều app dùng cả ba: `flutter_secure_storage` cho token, `hive_ce` cho settings, `drift` cho dữ liệu nghiệp vụ.

**Prompt mẫu: chọn kiến trúc**

```text
Đọc PRD.md. Ràng buộc: 1 dev, ngân sách server <X>/tháng, dự kiến <N> user và <M> bản ghi/ngày sau 1 năm.
Đề xuất 2–3 phương án kiến trúc (Flutter + Go hoặc FastAPI + PostgreSQL).
Mỗi phương án nêu: sơ đồ thành phần, chi phí, điểm nghẽn khi tăng x10, cách nâng cấp sau này.
Kết luận: phương án nên chọn cho MVP, ghi thành ADR-0001 theo templates/ADR.md.
```

**Prompt mẫu: thiết kế database**

```text
Thiết kế schema PostgreSQL cho các user stories trong PRD.md.
Yêu cầu: ERD dạng Mermaid, migration SQL, index cho từng query chính (giải thích vì sao),
bảng nào sẽ lớn nhanh nhất và chiến lược (partition, archive) khi qua 100 triệu dòng.
```

**Prompt mẫu: API contract**

```text
Viết openapi.yaml cho MVP: auth JWT, cursor pagination, format lỗi thống nhất, versioning /v1.
API contract này là nguồn sự thật duy nhất cho cả Flutter client và backend.
```

## 4. Thiết kế UI/UX

Hãy dựng mockup **trước** khi code UI. Sửa trên mockup mất vài phút, còn sửa trên Flutter có thể mất vài giờ. Giai đoạn này dùng Claude Design để làm mockup và prototype, Chat (Mermaid) để vẽ user flow, và ra các thứ sau: user flow, mockup các màn hình chính, `DESIGN_SYSTEM.md` gồm color, typography, spacing và component.

1. **User flow:** vẽ luồng từ lúc mở app đến khi hoàn thành việc chính, và đếm số bước.
2. **Design system:** chốt màu, font, spacing và component cơ bản trước.
3. **Mockup:** dựng 3–5 màn hình quan trọng nhất và lặp lại vài vòng.
4. **Chuyển sang Flutter:** đưa mockup và design system cho Claude Code để tạo `ThemeData` và các widget dùng chung.

**Prompt mẫu: user flow**

```text
Từ các user stories trong PRD.md, vẽ user flow cho hành trình chính <...>.
Đánh dấu bước nào có thể bỏ hoặc gộp để người dùng hoàn thành với ít thao tác nhất.
```

**Prompt mẫu: mockup**

```text
Thiết kế mockup mobile cho 4 màn hình: Onboarding, Home, Thêm giao dịch, Báo cáo.
Phong cách: tối giản, Material 3, màu chủ đạo <...>, hỗ trợ dark mode.
Dùng dữ liệu mẫu tiếng Việt thật (tên, số tiền VNĐ), có trạng thái empty, loading và error.
```

**Prompt mẫu: chuyển design sang Flutter (trong Claude Code)**

```text
Đọc docs/DESIGN_SYSTEM.md và ảnh mockup trong docs/mockups/.
Tạo lib/core/theme/ (ThemeData light và dark) cùng các widget dùng chung trong lib/core/widgets/.
Không hard-code màu hay size trong các màn hình.
```

Quy trình chi tiết (wireframe → prototype → test với 5 user → tài liệu bàn giao): [Dùng Claude làm prototype cho Designer, BA, PM](claude-lam-prototype.md).

**Mẹo:** chụp màn hình app đối thủ mà bạn thích rồi gửi cho Claude, hỏi “phân tích điểm tốt và điểm dở” để lấy ý tưởng. Đừng nhờ sao chép nguyên giao diện.

## 5. Lập kế hoạch: chia nhỏ để Claude Code làm tốt

Mỗi task nên đủ nhỏ để làm xong và test được trong một phiên (khoảng 1–3 giờ làm việc). Giai đoạn này ra `docs/ROADMAP.md`, hoặc một backlog trên Sheets hay GitHub Issues.

Một thứ tự milestone phù hợp cho MVP:

1. **M0 – Skeleton:** repo, CLAUDE.md, CI, Docker Compose, health check, Flutter app chạy được và gọi được API.
2. **M1 – Auth và user:** đăng ký, đăng nhập, refresh token, profile.
3. **M2 – Core feature:** tính năng Must quan trọng nhất, làm xong end-to-end.
4. **M3 – Các tính năng Must còn lại.**
5. **M4 – Hoàn thiện:** error, empty, loading state, analytics, crash report.
6. **M5 – Release:** build, store listing, deploy production.

**Prompt mẫu**

```text
Từ PRD.md và ARCHITECTURE.md, chia MVP thành milestone M0–M5 và các task.
Mỗi task gồm: ID, mô tả 1 dòng, layer (Flutter/API/DB), task phụ thuộc, acceptance criteria,
ước lượng (S/M/L). Task nào lớn hơn L thì chia nhỏ tiếp.
Xuất ra docs/ROADMAP.md dạng checklist.
```

**Mẹo:** làm theo **vertical slice**, nghĩa là mỗi task đi qua đủ DB, API và Flutter của một tính năng. Đừng làm hết backend rồi mới làm frontend, vì như vậy lỗi tích hợp sẽ lộ ra rất muộn.

## 6. Build với Claude Code

Claude Code làm tốt nhất khi có ba thứ: **context rõ ràng** (CLAUDE.md và docs), **task nhỏ** (lấy từ ROADMAP), và **cách tự kiểm tra** (test, lint, build). Giai đoạn này ra một repo chạy được, mỗi task là một commit hoặc PR.

### Cấu trúc repo gợi ý

```text
my-app/
├── CLAUDE.md            # context chung, luôn được nạp
├── docs/                # PRD, ARCHITECTURE, ROADMAP, ADR, DESIGN_SYSTEM, openapi.yaml
├── app/                 # Flutter (có thể có CLAUDE.md riêng)
├── server/              # Go hoặc FastAPI (có thể có CLAUDE.md riêng)
├── docker-compose.yml
└── .claude/
    ├── skills/<tên>/SKILL.md   # quy trình và kiến thức dùng khi cần
    ├── agents/                  # subagents: reviewer, test-writer
    └── settings.json            # permissions, hooks
```

### Dùng công cụ nào cho việc gì

| Công cụ | Vai trò | Ví dụ cho dự án |
| --- | --- | --- |
| CLAUDE.md | Context luôn được nạp. Nên giữ ngắn | Stack, lệnh build và test, convention, những điều cấm |
| Plan mode | Claude đọc code và lập kế hoạch, không sửa file | Mọi feature từ cỡ M trở lên |
| Skills | Kiến thức hoặc quy trình, chỉ nạp khi cần | `new-feature` (tạo đủ bộ BLoC, repository, screen), `db-migration` |
| Subagents | Chạy việc trong context riêng, trả về bản tóm tắt | `code-reviewer`, `test-writer`, khảo sát codebase lớn |
| Hooks | Tự động và chắc chắn chạy mỗi lần | Chạy `dart format`, `gofmt` hoặc `ruff` sau khi sửa file |
| MCP | Kết nối công cụ bên ngoài | Postgres (đọc schema), GitHub, trình duyệt |
| Plugins | Đóng gói skills, agents, hooks và MCP để dùng lại | Bộ công cụ chung cho mọi dự án của bạn |
| `settings.json` (permissions) | Cho phép / chặn cứng tool và lệnh | Chặn đọc `.env`, chặn `git push` (mẫu: [templates/settings.json](../templates/settings.json)) |

Quy tắc dễ nhớ: những gì **bắt buộc** phải xảy ra mỗi lần thì dùng hook. Những gì chỉ là hướng dẫn thì để ở CLAUDE.md hoặc skill.

### Khởi động dự án

1. Tạo repo và copy thư mục `docs/` từ Project vào.
2. Chạy `claude`, gõ `/init` để Claude tạo CLAUDE.md, sau đó sửa lại theo mẫu ở Phụ lục.
3. Giao task M0 (skeleton) và commit ngay khi nó chạy được.
4. Nếu bạn có starter template riêng, đóng gói nó thành skill để mọi dự án sau dùng chung một pattern.

### Vòng lặp cho mỗi feature

1. `/clear` để bắt đầu một phiên sạch.
2. Vào plan mode (nhấn Shift+Tab để chuyển mode) và giao task.
3. Đọc plan, sửa cho đúng rồi mới duyệt.
4. Cho Claude thực thi: viết code kèm test.
5. Chạy test, lint, build. Nếu lỗi, đưa lỗi cho Claude sửa và lặp lại.
6. Review: đọc diff và gọi subagent `code-reviewer`.
7. Bạn commit (hoặc cho phép Claude commit sau khi đã duyệt diff), đánh dấu task xong trong ROADMAP.

**Prompt mẫu: feature (trong plan mode)**

```text
Task T-12 trong @docs/ROADMAP.md: <mô tả>.
Đọc @docs/openapi.yaml và code hiện có trong server/internal/expense và app/lib/features/expense.
Lập plan: file nào tạo hoặc sửa, migration, test cần viết, rủi ro.
Chưa code. Nếu còn chỗ mơ hồ, hỏi tôi trước.
```

**Prompt mẫu: sửa bug**

```text
Bug: <hiện tượng>. Các bước tái hiện: <...>. Log hoặc lỗi: <dán vào>.
Viết test tái hiện bug trước, chạy để thấy nó fail, rồi mới sửa.
Giải thích nguyên nhân gốc, không chỉ vá triệu chứng.
```

**Prompt mẫu: tạo subagent reviewer**

```text
Tạo subagent code-reviewer trong .claude/agents/: chỉ được đọc, không được sửa file.
Check: bảo mật (SQL injection, auth), N+1 query, thiếu index, lỗi chưa xử lý,
vi phạm convention trong CLAUDE.md. Output: danh sách vấn đề xếp theo mức độ nghiêm trọng.
```

### Quản lý context và token

- Dùng `/clear` giữa các task không liên quan, và `/compact` khi phiên đã dài.
- Dùng `@file` để chỉ đúng file cần đọc, không bắt Claude đọc cả repo.
- Việc khảo sát lớn (“tìm mọi chỗ dùng X”) nên giao cho subagent để không làm đầy context chính.

### An toàn khi để Claude chạy lệnh

Claude Code chạy lệnh thật trên máy bạn, với quyền của bạn. Vài quy tắc tối thiểu:

- **Chặn cứng điều cấm bằng `.claude/settings.json`**, không chỉ dặn trong CLAUDE.md: đọc `.env` và file khóa, `git push`, `rm -rf`, lệnh migrate / deploy production. Mẫu: [templates/settings.json](../templates/settings.json).
- **Chế độ bỏ qua permission** (tự chạy mọi lệnh không hỏi) chỉ dùng trong môi trường cô lập: container, máy ảo, worktree không có secret. Không dùng trên máy có dữ liệu thật hay quyền vào production.
- **Nội dung Claude đọc có thể chứa lệnh ẩn** (prompt injection): issue, README của thư viện lạ, trang web, file khách gửi. Khi giao việc đọc nguồn không tin cậy, giữ chế độ hỏi trước khi chạy lệnh và đọc kỹ lệnh Claude đề xuất.
- **Không trỏ MCP vào database production.** Dùng DB local, bản sao đã ẩn dữ liệu, hoặc tài khoản chỉ đọc.
- **Secret không đi vào prompt:** không dán API key, mật khẩu, dữ liệu khách hàng thật vào chat. Nếu lỡ dán, coi như đã lộ và đổi key.
- **Dữ liệu chat có được dùng để huấn luyện không:** gói cá nhân xem và chỉnh trong phần cài đặt quyền riêng tư của Claude; gói Team / Enterprise theo điều khoản thương mại của tổ chức. Kiểm lại trước khi đưa tài liệu nội bộ vào.

## 7. Test và review

Claude viết test rất nhanh, nhưng **bạn phải chỉ rõ test cái gì**. Nếu không, nó dễ viết test chỉ để pass. Giai đoạn này dùng Claude Code (cho test và subagent review) và Claude in Chrome (cho test UI web).

| Loại | Flutter | Backend |
| --- | --- | --- |
| Unit | `bloc_test`, `mocktail` | Go: `testing` + `testify` · FastAPI: `pytest` |
| Integration | `integration_test` | Testcontainers chạy PostgreSQL thật |
| Contract | Sinh client từ `openapi.yaml` | Kiểm tra response đúng schema |
| UI / E2E | Flutter web hoặc thiết bị thật, có thể nhờ Claude in Chrome thao tác trên bản web | — |

**Prompt mẫu: viết test**

```text
Viết test cho ExpenseService dựa trên acceptance criteria của US-03 trong docs/features/them-giao-dich.md.
Bao gồm: happy path, input sai, không có quyền, dữ liệu trống, giá trị biên.
Không mock database, dùng Testcontainers. Không sửa code đang có chỉ để test pass.
```

**Prompt mẫu: review bảo mật trước khi release**

```text
Review toàn bộ server/ theo OWASP API Top 10: auth, phân quyền theo resource (IDOR),
rate limit, validate input, lộ secret, CORS. Liệt kê lỗi theo mức độ kèm file:line và cách sửa.
```

## 8. Deploy và phát hành

Mục tiêu là một pipeline tự động: push code → test → build → deploy. Bạn không phải deploy bằng tay nữa. Giai đoạn này dùng Claude Code (Dockerfile, CI/CD), Claude in Chrome (điền thông tin trên Play Console, App Store Connect) và Chat (viết store listing).

- **Backend:** Dockerfile multi-stage, Docker Compose hoặc PaaS, migration chạy tự động khi deploy, backup DB hằng ngày.
- **CI/CD:** GitHub Actions chạy lint, test và build cho cả Flutter lẫn backend.
- **Mobile:** tách flavor dev/prod, ký app, build `appbundle` cho Android và `ipa` cho iOS. Chuẩn bị privacy policy và khai báo data safety.
- **Observability:** structured log, health check, crash report (ví dụ Sentry hoặc Crashlytics).

**Prompt mẫu: CI/CD**

```text
Tạo GitHub Actions: PR thì chạy lint và test (Flutter + server).
Merge vào main thì build Docker image, push lên registry, deploy lên VPS qua SSH, chạy migration.
Secret lấy từ GitHub Secrets, không hard-code. Viết kèm docs/DEPLOY.md hướng dẫn rollback.
```

**Prompt mẫu: store listing**

```text
Viết store listing tiếng Việt và tiếng Anh cho app <...>: tên (tối đa 30 ký tự),
mô tả ngắn (tối đa 80 ký tự), mô tả dài, 5 caption cho ảnh chụp màn hình, từ khóa ASO.
Dựa trên IDEA_BRIEF.md, nhấn mạnh điểm khác biệt so với đối thủ.
```

**Lưu ý:** khi để Claude thao tác trên console của store bằng trình duyệt, bạn nên tự bấm nút Submit cuối cùng. Prompt viết privacy policy từ chính source code, và các prompt CI/CD, store listing: [prompts/ke-hoach-trien-khai-van-hanh.md](../prompts/ke-hoach-trien-khai-van-hanh.md). Việc cần làm về pháp lý: [Phụ lục D](#d-pháp-lý-cần-biết-ở-việt-nam).

## 9. Vận hành và cải tiến

Sau khi phát hành, Claude giúp biến phản hồi và dữ liệu thành task tiếp theo.

- **Gom phản hồi:** dán review trên store, ticket và crash log vào Chat, nhờ phân nhóm theo chủ đề và ưu tiên.
- **Scheduled task:** đặt lịch hằng tuần để Claude tổng hợp review mới và đề xuất việc cần làm.
- **Cập nhật tài liệu:** mỗi quyết định mới ghi thêm một ADR, cập nhật PRD và ROADMAP trong Project, để context không bị lỗi thời.
- **Theo dõi hiệu năng:** khi có slow query log, dán `EXPLAIN ANALYZE` cho Claude phân tích, rồi đối chiếu bảng quy mô ở Phần 3 để biết đã đến lúc nâng cấp kiến trúc chưa.

**Prompt mẫu**

```text
Đây là 120 review và 30 crash log trong tháng: <dán vào>.
Phân nhóm theo vấn đề, đếm số lần xuất hiện, đánh giá mức ảnh hưởng.
Đề xuất 5 task ưu tiên cho sprint tới, đúng format của docs/ROADMAP.md.
```

## Phụ lục

### A. Ví dụ CLAUDE.md đã điền

Mẫu trống để điền: [templates/CLAUDE.md](../templates/CLAUDE.md). Dưới đây là ví dụ đã điền cho Expense App.

```markdown
# Expense App
Ứng dụng quản lý chi tiêu cá nhân. Chi tiết: @docs/PRD.md, @docs/ARCHITECTURE.md

## Stack
- app/: Flutter 3.x, BLoC, go_router, dio, flutter_secure_storage (token), hive_ce (settings), drift (dữ liệu offline)
- server/: Go 1.2x (chi, sqlc, pgx) | PostgreSQL 18

## Lệnh
- Chạy local: docker compose up -d
- Test server: cd server && go test ./...
- Test app: cd app && flutter test
- Migration: make migrate-up

## Quy ước
- Flutter: feature-first (lib/features/<feature>/{data,domain,presentation})
- Server: handler -> service -> repository, không gọi DB trong handler
- API theo docs/openapi.yaml. Đổi API thì cập nhật spec trước
- Offline-first: UI đọc từ local DB, repository sync với API khi có mạng
- DI: RepositoryProvider/BlocProvider, không dùng get_it
- Mỗi feature xét đủ 5 nhóm test; integration test dùng PostgreSQL thật qua Testcontainers

## Không được làm
- Không tự commit / push; làm xong báo file đã đổi, chờ duyệt
- Không đọc / sửa .env*, không commit secret
- Không sửa migration đã chạy, chỉ tạo migration mới
- Không thêm dependency mới khi chưa hỏi
```

Các điều cấm quan trọng (đọc `.env`, push, xóa hàng loạt) nên chặn cứng thêm bằng `.claude/settings.json`, vì CLAUDE.md chỉ là lời dặn. Mẫu: [templates/settings.json](../templates/settings.json).

### B. Checklist từ ý tưởng đến phát hành

- [ ] IDEA_BRIEF có bằng chứng thị trường kèm link, kết luận là Go
- [ ] PRD có MVP với MUST gọn (chỉ thứ cần cho journey chính), có Out of scope
- [ ] ARCHITECTURE và ADR-0001 phù hợp quy mô dự kiến
- [ ] Schema có index cho các query chính, đã biết bảng nào sẽ lớn nhanh
- [ ] openapi.yaml đã chốt
- [ ] Mockup 3–5 màn hình chính và DESIGN_SYSTEM
- [ ] ROADMAP chia thành task theo vertical slice
- [ ] Repo có CLAUDE.md, CI, hook format
- [ ] Tất cả task Must xong, test pass
- [ ] Review bảo mật xong
- [ ] Deploy tự động, có backup và crash report
- [ ] Store listing và privacy policy đã sẵn sàng

### C. Lỗi thường gặp

| Lỗi | Hậu quả | Cách tránh |
| --- | --- | --- |
| Code ngay từ ý tưởng | Làm xong mới biết không ai cần | Làm Phần 1 trước, đòi link nguồn |
| Một prompt “làm cả app” | Code rối, không kiểm soát được | Chia task nhỏ, dùng plan mode |
| Không có CLAUDE.md và docs | Mỗi phiên Claude làm một kiểu | Docs làm nguồn sự thật, CLAUDE.md ngắn gọn |
| CLAUDE.md quá dài | Tốn context, Claude bỏ qua bớt chỉ dẫn | Đưa phần chi tiết sang skills hoặc docs |
| Micro-service ngay từ MVP | Chậm, tốn chi phí | Bắt đầu với modular monolith |
| Phiên làm việc quá dài | Claude quên hoặc nhầm context | `/clear` sau mỗi task |
| Accept code không đọc | Bug và lỗ hổng bảo mật ẩn | Đọc diff, chạy test, dùng subagent review |

### D. Pháp lý cần biết ở Việt Nam

Phần này chỉ để biết cần hỏi gì, không thay cho tư vấn pháp lý. Văn bản thay đổi nhanh, hãy kiểm tra bản hiện hành trên cổng văn bản chính thức trước khi áp dụng.

| Chủ đề | Khi nào liên quan | Việc cần làm |
| --- | --- | --- |
| Bảo vệ dữ liệu cá nhân: Luật 91/2025/QH15 (hiệu lực 01/01/2026), Nghị định 356/2025/NĐ-CP hướng dẫn | App có tài khoản, số điện thoại, vị trí, ảnh, dữ liệu sức khỏe, tài chính | Xin đồng ý rõ ràng, cho xem / sửa / xóa dữ liệu, chính sách quyền riêng tư, xác định dữ liệu nào gửi ra nước ngoài (AI, cloud, analytics) |
| Thương mại điện tử | App hoặc web có bán hàng, đặt hàng, thanh toán | Thông báo hoặc đăng ký với Bộ Công Thương qua cổng online.gov.vn; hiển thị thông tin doanh nghiệp, chính sách đổi trả, giải quyết khiếu nại. Quy định đang được thay bằng văn bản mới, kiểm tra trước khi nộp |
| Chính sách store | Mọi app lên App Store / Google Play | Privacy policy có link công khai, khai báo App Privacy / Data safety khớp thực tế, xóa tài khoản trong app |

Dùng Claude để chuẩn bị: prompt **Privacy policy** trong [prompts/ke-hoach-trien-khai-van-hanh.md](../prompts/ke-hoach-trien-khai-van-hanh.md) liệt kê dữ liệu app thực thu thập từ source code rồi viết nháp; luật sư duyệt bản cuối.

### E. Chi phí ước tính cho một MVP

Giá tham khảo tháng 11/2026, bằng USD, chưa gồm thuế. Kiểm lại trên trang giá chính thức trước khi lập ngân sách.

| Khoản | Mức | Ghi chú |
| --- | --- | --- |
| Gói Claude | Pro $20/tháng; Max $100 hoặc $200/tháng | Claude Code và Claude Design dùng chung hạn mức gói. Làm hằng ngày nhiều giờ thường cần Max ([claude.com/pricing](https://claude.com/pricing)) |
| Tính năng AI trong app | Tính theo token qua Claude API | Đặt quota theo user và `max_tokens` ngay từ đầu; ước tính = số user hoạt động × số lượt / ngày × token / lượt |
| Server | VPS $5–20/tháng cho MVP; PaaS hoặc BaaS có gói miễn phí giới hạn | Thêm backup DB và object storage |
| Tài khoản nhà phát triển | Apple $99/năm; Google Play $25 một lần | Đăng ký tài khoản tổ chức cần mã số D-U-N-S, mất vài ngày đến vài tuần |
| Build iOS | Cần máy Mac, hoặc dịch vụ build cloud (Codemagic, EAS Build, GitHub Actions macOS) có gói miễn phí giới hạn | |
| SMS OTP, email | Tính theo tin | Rate limit để tránh bị spam OTP làm tốn tiền ([guide test, mục 10](claude-test-web-mobile.md#10-chống-bot-và-tấn-công-bằng-ai)) |
| Tên miền, crash report, analytics | Tên miền ~$10–15/năm; Sentry, Crashlytics có gói miễn phí | |

### Nguồn tham khảo

- [Claude Code: Features overview](https://code.claude.com/docs/en/features-overview)
- [Claude Code docs map](https://code.claude.com/docs/en/claude_code_docs_map)
- [Claude Code power user tips](https://support.claude.com/en/articles/14554000-claude-code-power-user-tips)
- [Migrate a Flutter app from Hive to Drift (hive_ce, drift)](https://startdebugging.net/2026/10/migrate-a-flutter-app-from-hive-to-drift/)
- [Hive vs Drift vs Floor vs Isar](https://quashbugs.com/blog/hive-vs-drift-vs-floor-vs-isar-2025) · [hive_ce](https://pub.dev/packages/hive_ce) · [drift](https://pub.dev/packages/drift) · [flutter_secure_storage](https://pub.dev/packages/flutter_secure_storage)
- [Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15](https://thuvienphapluat.vn/van-ban/Bo-may-hanh-chinh/Law-91-2025-QH15-Personal-Data-Protection-665440.aspx) · [Nghị định 356/2025/NĐ-CP](https://thuvienphapluat.vn/van-ban/Quyen-dan-su/Nghi-dinh-356-2025-ND-CP-huong-dan-Luat-Bao-ve-du-lieu-ca-nhan-687428.aspx)
- [Claude pricing](https://claude.com/pricing) · [Apple Developer Program](https://developer.apple.com/programs/) · [Google Play Console — đăng ký](https://support.google.com/googleplay/android-developer/answer/6112435)
