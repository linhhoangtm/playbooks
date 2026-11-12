# Hướng dẫn dùng Claude xây dựng sản phẩm từ ý tưởng

Cập nhật: 2026-11-12 · Tác giả: Linh Hoang

Đi từ ý tưởng đến app đã phát hành qua 9 giai đoạn. Mỗi giai đoạn dùng đúng một công cụ của Claude và ra một deliverable cụ thể, rồi deliverable đó làm context cho giai đoạn sau. Ví dụ xuyên suốt: app mobile **Flutter**, backend **Go hoặc FastAPI**, database **PostgreSQL**.

| # | Giai đoạn | Công cụ chính | Deliverable |
| --- | --- | --- | --- |
| 1 | Kiểm chứng ý tưởng | Chat + Research | `IDEA_BRIEF.md` |
| 2 | Đặc tả sản phẩm | Chat trong Project | `PRD.md`, scope MVP |
| 3 | Kiến trúc | Chat trong Project | `ARCHITECTURE.md`, schema, `openapi.yaml` |
| 4 | Thiết kế UI/UX | Artifacts: Design | Mockup, design system |
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
| Artifacts: Design / Whiteboard | Wireframe, mockup, user flow, sơ đồ kiến trúc | Mockup màn hình chính |
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

**Prompt mẫu: phản biện**

```text
Ý tưởng: <mô tả 1–2 câu>. Người dùng mục tiêu: <ai>. Thị trường: Việt Nam.
Hãy đóng vai nhà đầu tư khó tính:
1. 5 lý do ý tưởng này có thể thất bại.
2. Giả định nào rủi ro nhất, và cách kiểm tra nó trong 1 tuần mà không cần code.
3. Ai đang trả tiền để giải quyết vấn đề này hôm nay?
Không khen, chỉ phản biện.
```

**Prompt mẫu: nghiên cứu thị trường (bật Research)**

```text
Nghiên cứu thị trường cho ý tưởng: <...>.
- Liệt kê 5–10 đối thủ (app/web) đang hoạt động: tên, nền tảng, lượt tải hoặc traffic, mô hình giá.
- Tóm tắt các phàn nàn lặp lại trong review 1–2 sao.
- Có tín hiệu nhu cầu nào không (nhóm Facebook, Reddit, lượng tìm kiếm)?
Bắt buộc có link nguồn cho mỗi số liệu. Cuối cùng: kết luận Go/No-go và 3 lý do.
```

**Prompt mẫu: chốt Idea Brief**

```text
Tổng hợp thành IDEA_BRIEF.md (tối đa 1 trang): vấn đề, người dùng, giải pháp,
đối thủ và khe hở, mô hình kiếm tiền, rủi ro lớn nhất, kết luận.
```

**Lỗi hay gặp:** hỏi “ý tưởng này hay không?”. Claude sẽ có xu hướng trả lời lạc quan. Hãy luôn hỏi “vì sao nó thất bại?” và đòi link nguồn.

## 2. Đặc tả sản phẩm (PRD) và scope MVP

PRD là “hợp đồng” giữa bạn và Claude: mọi giai đoạn sau đều tham chiếu nó. Giai đoạn này dùng Chat trong Project và ra `PRD.md` (lưu vào Project).

Một PRD gọn gồm:

- **Mục tiêu** và 1–2 chỉ số thành công, ví dụ 100 user hoạt động tuần sau 1 tháng.
- **Persona:** 1–2 người dùng chính.
- **User stories** kèm acceptance criteria.
- **MVP scope** theo MoSCoW (Must, Should, Could, Won’t).
- **Non-functional:** đa ngôn ngữ, offline, bảo mật, số user dự kiến.
- **Out of scope:** những gì chưa làm.

**Prompt mẫu: để Claude phỏng vấn bạn**

```text
Dựa trên IDEA_BRIEF.md trong Project, hãy phỏng vấn tôi để viết PRD.
Hỏi từng nhóm 3–5 câu: người dùng, tính năng, dữ liệu, nền tảng, kiếm tiền.
Khi đủ thông tin, viết PRD.md theo cấu trúc: Mục tiêu, Persona, User stories
(kèm acceptance criteria dạng Given/When/Then), MVP (MoSCoW), Non-functional, Out of scope.
```

**Prompt mẫu: cắt scope**

```text
Đây là danh sách tính năng tôi muốn: <...>.
Tôi code một mình, muốn ra MVP trong 4 tuần. Hãy cắt còn tối đa 5 tính năng Must
đủ để kiểm chứng giả định rủi ro nhất trong IDEA_BRIEF. Giải thích vì sao bỏ từng cái.
```

**Mẹo:** mở một chat mới, dán PRD vào và hỏi “Tìm 10 chỗ mơ hồ hoặc mâu thuẫn trong PRD này”. Một phiên mới không bị thiên vị bởi cuộc trò chuyện trước đó.

## 3. Kiến trúc: chọn theo quy mô, không theo trend

Nguyên tắc: **bắt đầu bằng modular monolith**, chỉ tách thêm khi có số liệu chứng minh là cần. Giai đoạn này ra `ARCHITECTURE.md`, schema/migration, `openapi.yaml` và các ADR (Architecture Decision Record).

### Kiến trúc theo quy mô

Các mốc user và dung lượng dưới đây chỉ là ước lượng để định hướng. Hãy dựa vào số liệu thật của bạn.

| Quy mô | Dấu hiệu | Kiến trúc | Stack ví dụ |
| --- | --- | --- | --- |
| Nhỏ (MVP) | Dưới ~10k user, dữ liệu dưới ~10 GB, 1 dev | Modular monolith, 1 API, 1 DB | Flutter + Go/FastAPI + PostgreSQL, Docker Compose trên 1 VPS |
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
- **Offline-first là mặc định cho mobile:** UI chỉ đọc từ local DB. Repository tự đồng bộ với API khi có mạng.
- **Đồng bộ an toàn:** mỗi bản ghi có cờ trạng thái sync, xóa bằng soft delete, id sinh ở client (UUID) để không trùng khi sync.

| Nhu cầu lưu local | Chọn |
| --- | --- |
| Key-value: settings, token, cache API đơn giản | `hive_ce`, bản cộng đồng còn được duy trì. Package `hive` gốc đã ngừng cập nhật |
| Dữ liệu nghiệp vụ có quan hệ, cần query, filter, join, nhiều bản ghi | `drift` (SQLite) |

Nhiều app dùng cả hai: `hive_ce` cho settings, `drift` cho dữ liệu nghiệp vụ.

**Prompt mẫu: chọn kiến trúc**

```text
Đọc PRD.md. Ràng buộc: 1 dev, ngân sách server <X>/tháng, dự kiến <N> user và <M> bản ghi/ngày sau 1 năm.
Đề xuất 2–3 phương án kiến trúc (Flutter + Go hoặc FastAPI + PostgreSQL).
Mỗi phương án nêu: sơ đồ thành phần, chi phí, điểm nghẽn khi tăng x10, cách nâng cấp sau này.
Kết luận: phương án nên chọn cho MVP, ghi thành ADR-001.
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

Hãy dựng mockup **trước** khi code UI. Sửa trên mockup mất vài phút, còn sửa trên Flutter có thể mất vài giờ. Giai đoạn này dùng Chat với Artifacts (Design để làm mockup, Whiteboard để vẽ user flow) và ra các thứ sau: user flow, mockup các màn hình chính, `DESIGN_SYSTEM.md` gồm color, typography, spacing và component.

1. **User flow:** vẽ luồng từ lúc mở app đến khi hoàn thành việc chính, và đếm số bước.
2. **Design system:** chốt màu, font, spacing và component cơ bản trước.
3. **Mockup:** dựng 3–5 màn hình quan trọng nhất và lặp lại vài vòng.
4. **Chuyển sang Flutter:** đưa mockup và design system cho Claude Code để tạo `ThemeData` và các widget dùng chung.

**Prompt mẫu: user flow**

```text
Từ các user stories trong PRD.md, vẽ user flow cho hành trình chính <...>.
Đánh dấu bước nào có thể bỏ hoặc gộp để người dùng hoàn thành trong tối đa 3 thao tác.
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
7. Commit, đánh dấu task xong trong ROADMAP.

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
- Chỉ dùng chế độ bỏ qua permission trong môi trường cô lập, không chạy trên máy có dữ liệu thật.

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
Viết test cho ExpenseService dựa trên acceptance criteria của US-03 trong PRD.md.
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

**Lưu ý:** khi để Claude thao tác trên console của store bằng trình duyệt, bạn nên tự bấm nút Submit cuối cùng.

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

### A. Mẫu CLAUDE.md

```markdown
# Expense App
Ứng dụng quản lý chi tiêu cá nhân. Chi tiết: @docs/PRD.md, @docs/ARCHITECTURE.md

## Stack
- app/: Flutter 3.x, BLoC, go_router, dio, hive_ce (settings), drift (dữ liệu offline)
- server/: Go 1.2x (chi, sqlc, pgx) | PostgreSQL 16

## Lệnh
- Chạy local: docker compose up -d
- Test server: cd server && go test ./...
- Test app: cd app && flutter test
- Migration: make migrate-up

## Convention
- Flutter: feature-first (lib/features/<feature>/{data,domain,presentation})
- Server: handler -> service -> repository, không gọi DB trong handler
- API theo docs/openapi.yaml. Đổi API thì cập nhật spec trước
- Offline-first: UI đọc từ local DB, repository sync với API khi có mạng
- DI: RepositoryProvider/BlocProvider, không dùng get_it
- Mỗi feature phải có test

## Cấm
- Không commit secret hoặc .env
- Không sửa migration đã chạy, chỉ tạo migration mới
- Không thêm dependency mới khi chưa hỏi
```

### B. Checklist từ ý tưởng đến phát hành

- [ ] IDEA_BRIEF có bằng chứng thị trường kèm link, kết luận là Go
- [ ] PRD có MVP tối đa 5 tính năng Must, có Out of scope
- [ ] ARCHITECTURE và ADR-001 phù hợp quy mô dự kiến
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

### Nguồn tham khảo

- [Claude Code: Features overview](https://code.claude.com/docs/en/features-overview)
- [Claude Code docs map](https://code.claude.com/docs/en/claude_code_docs_map)
- [Claude Code power user tips](https://support.claude.com/en/articles/14554000-claude-code-power-user-tips)
- [Migrate a Flutter app from Hive to Drift (hive_ce, drift)](https://startdebugging.net/2026/10/migrate-a-flutter-app-from-hive-to-drift/)
- [Hive vs Drift vs Floor vs Isar](https://quashbugs.com/blog/hive-vs-drift-vs-floor-vs-isar-2025)
