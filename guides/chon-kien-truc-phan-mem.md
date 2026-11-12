# Chọn kiến trúc phần mềm phù hợp

Cập nhật: 2026-11-12

Chọn kiến trúc không dựa vào công nghệ đang “hot”, mà là cân bằng giữa nhu cầu kinh doanh, năng lực đội ngũ và ràng buộc kỹ thuật. Nội dung được đối chiếu với nguồn gốc: Martin Fowler, sách Google SRE, báo cáo DORA 2025, case study của Shopify, Twilio Segment, Amazon Prime Video và các repo GitHub phổ biến (xem mục Nguồn ở cuối). Các mốc về số user hay dung lượng chỉ để định hướng, không phải quy tắc.

## Mục lục

- [1. Năm nhóm yếu tố quyết định kiến trúc](#1-năm-nhóm-yếu-tố-quyết-định-kiến-trúc)
- [2. Yêu cầu phi chức năng (NFRs)](#2-yêu-cầu-phi-chức-năng-nfrs)
- [3. Yêu cầu nghiệp vụ cốt lõi](#3-yêu-cầu-nghiệp-vụ-cốt-lõi)
- [4. Đội ngũ, ngân sách và hạ tầng](#4-đội-ngũ-ngân-sách-và-hạ-tầng)
- [5. Khi code cùng AI: điều gì thay đổi?](#5-khi-code-cùng-ai-điều-gì-thay-đổi)
- [6. Các kiểu kiến trúc và khi nào dùng](#6-các-kiểu-kiến-trúc-và-khi-nào-dùng)
- [7. Cây quyết định](#7-cây-quyết-định)
- [8. Ví dụ áp dụng](#8-ví-dụ-áp-dụng-với-flutter--gofastapi--postgresql)
- [9. Ghi lại quyết định và dùng Claude hỗ trợ](#9-ghi-lại-quyết-định-và-dùng-claude-hỗ-trợ)
- [10. Bài học từ các công ty thật](#10-bài-học-từ-các-công-ty-thật)
- [Nguồn](#nguồn)

## 1. Năm nhóm yếu tố quyết định kiến trúc

Trước khi vẽ bất kỳ sơ đồ nào, hãy trả lời được các câu hỏi dưới đây. Thiếu câu trả lời nào thì ghi lại như một giả định cần kiểm tra.

| Nhóm | Câu hỏi then chốt | Ảnh hưởng tới |
| --- | --- | --- |
| 1. Yêu cầu phi chức năng (NFRs) | Bao nhiêu user, độ trễ bao nhiêu, uptime bao nhiêu, chuẩn bảo mật nào? | Monolith hay phân tán, cache, queue, failover |
| 2. Nghiệp vụ cốt lõi | Domain phức tạp đến đâu? Dữ liệu cần nhất quán tuyệt đối không? | Layered hay DDD, SQL hay NoSQL, Saga |
| 3. Đội ngũ | Bao nhiêu người, đã quen kiến trúc nào? | Số service, mức độ tách module |
| 4. Ngân sách và thời gian | MVP hay hệ thống lõi 5–10 năm? Chi phí vận hành tối đa? | Độ phức tạp chấp nhận được, cloud hay VPS |
| 5. Hạ tầng và hệ sinh thái | Phải nối với ERP, cổng thanh toán, hóa đơn điện tử? Chạy on-premise? | Integration layer, giới hạn công nghệ |

Nguyên tắc chung: **chọn kiến trúc đơn giản nhất đáp ứng được yêu cầu hiện tại**, và thiết kế để có thể tách ra sau này khi số liệu thực tế chứng minh là cần.

Để không bỏ sót yêu cầu chất lượng, có thể dùng mô hình [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) làm checklist. Mô hình này gồm 9 đặc tính chất lượng sản phẩm, ví dụ hiệu năng, độ tin cậy, bảo mật, khả năng bảo trì, tính linh hoạt.

**Thuật ngữ dùng trong tài liệu**

| Thuật ngữ | Nghĩa | Ví dụ |
| --- | --- | --- |
| **Monolith** (“một khối”) | Toàn bộ backend là **một ứng dụng duy nhất**: một codebase, build ra một file chạy, deploy một lần, thường dùng chung một database. Các phần gọi nhau bằng hàm trong cùng tiến trình, không qua mạng. Đơn giản, nhanh, dễ debug; nhược điểm là dễ rối nếu không chia module, và phải scale cả khối cùng lúc | Một API Go duy nhất xử lý cả user, đơn hàng, thanh toán, dùng một PostgreSQL |
| **Modular monolith** | Vẫn là một ứng dụng, deploy một lần, nhưng bên trong **chia thành các module có ranh giới rõ**: mỗi module tự quản dữ liệu của mình, chỉ gọi module khác qua interface công khai | API Go với các thư mục `internal/user`, `internal/order`, `internal/payment`, không module nào đọc thẳng bảng của module khác |
| **Microservices** | Hệ thống chia thành **nhiều service nhỏ chạy riêng**, mỗi service deploy độc lập, thường có database riêng, gọi nhau qua mạng (HTTP, gRPC, message queue) | Service user, service đơn hàng, service thanh toán, mỗi cái một container và một database |
| **CRUD** | Viết tắt của **C**reate (tạo), **R**ead (đọc), **U**pdate (sửa), **D**elete (xóa): bốn thao tác cơ bản với dữ liệu, tương ứng `INSERT`, `SELECT`, `UPDATE`, `DELETE` trong SQL và `POST`, `GET`, `PUT/PATCH`, `DELETE` trong REST API. “Ứng dụng CRUD” là ứng dụng chủ yếu chỉ nhập, xem, sửa, xóa dữ liệu, ít quy tắc nghiệp vụ phức tạp | Quản lý danh bạ, danh mục sản phẩm, ghi chú. Ngược lại, tính lương hay xử lý bảo hiểm có nhiều quy tắc nên không chỉ là CRUD |

Monolith không có nghĩa là “code cũ” hay “lỗi thời”. Nó chỉ nói hệ thống được deploy như một khối. Một monolith thiết kế tốt (modular) có thể phục vụ rất lớn, như trường hợp Shopify ở mục 10.

## 2. Yêu cầu phi chức năng (NFRs)

NFRs là “xương sống” định hình kiến trúc. Hãy ghi chúng thành **con số cụ thể**, không ghi chung chung kiểu “nhanh” hay “chịu tải tốt”.

**Khả năng mở rộng (Scalability)**

- **Scale-up** (tăng cấu hình máy) đơn giản, đủ cho đa số hệ thống nhỏ và vừa.
- **Scale-out** (thêm máy) cần app stateless, session và file để ngoài app (Redis, object storage).
- Traffic tăng đột biến theo giờ cao điểm (ví dụ thương mại điện tử khi flash sale): cần autoscaling, queue để hấp thụ tải. Chỉ tách service khi một phần hệ thống có tải khác hẳn phần còn lại.

**Hiệu năng và độ trễ (Performance & Latency)**

- Cần phản hồi real-time: cache (Redis), index đúng, WebSocket, xử lý gần người dùng (CDN).
- Việc nặng chấp nhận chờ (báo cáo, gửi mail, xử lý ảnh): đưa vào background job.
- Đọc nhiều hơn ghi rất nhiều, hoặc mô hình đọc khác mô hình ghi: cân nhắc **CQRS**. Nhiều hệ thống cần phản ứng theo sự kiện: **Event-Driven Architecture**.

**Tính sẵn sàng và độ tin cậy (Availability & Reliability)**

| Uptime | Downtime tối đa / năm | / tháng (30 ngày) | Thường cần |
| --- | --- | --- | --- |
| 99% | ~3,65 ngày | ~7,2 giờ | 1 server, backup tốt |
| 99,9% | ~8,76 giờ | ~43 phút | Health check, tự restart, DB có replica |
| 99,99% | ~52,6 phút | ~4,3 phút | Nhiều instance sau load balancer, failover tự động, không có single point of failure |
| 99,999% | ~5,3 phút | ~26 giây | Multi-region, đội vận hành 24/7, chi phí rất cao |

Số liệu theo [bảng availability của Google SRE](https://sre.google/sre-book/availability-table/). Hai ý quan trọng từ sách SRE:

- **100% không phải mục tiêu đúng.** Mỗi số 9 thêm vào đòi hỏi thay đổi kiến trúc và chi phí tăng mạnh. Hãy hỏi: “nếu hệ thống ngừng 1 giờ thì thiệt hại bao nhiêu?”.
- **Error budget = 1 − SLO.** Với SLO 99,9%, bạn có 0,1% “ngân sách lỗi”. Còn ngân sách thì được release nhanh; hết ngân sách thì ưu tiên ổn định.

**Bảo mật và tuân thủ (Security & Compliance)**

- Zero-Trust: mọi request đều phải xác thực, kể cả giữa các service nội bộ.
- Phân vùng mạng, mã hóa dữ liệu khi lưu trữ và khi truyền, audit log.
- Quy định như GDPR, PCI-DSS hay pháp luật bảo vệ dữ liệu cá nhân ở Việt Nam có thể buộc bạn tách riêng phần xử lý dữ liệu nhạy cảm (thanh toán, giấy tờ tùy thân, sức khỏe), ghi log truy cập và quy định nơi lưu trữ dữ liệu. Ở Việt Nam, khung chính hiện nay là [Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15](https://thuvienphapluat.vn/van-ban/Bo-may-hanh-chinh/Law-91-2025-QH15-Personal-Data-Protection-665440.aspx) (hiệu lực từ 01/01/2026) và [Nghị định 356/2025/NĐ-CP](https://thuvienphapluat.vn/van-ban/Quyen-dan-su/Nghi-dinh-356-2025-ND-CP-huong-dan-Luat-Bao-ve-du-lieu-ca-nhan-687428.aspx) hướng dẫn. Dự án có dữ liệu cá nhân nên hỏi luật sư sớm, vì yêu cầu về đồng ý, lưu trữ và chuyển dữ liệu ra nước ngoài (kể cả gửi cho AI hay cloud nước ngoài) ảnh hưởng trực tiếp tới kiến trúc.

## 3. Yêu cầu nghiệp vụ cốt lõi

**Độ phức tạp của domain**

| Domain | Dấu hiệu | Kiến trúc code phù hợp |
| --- | --- | --- |
| Đơn giản | Chủ yếu CRUD, ít quy tắc nghiệp vụ | Layered / MVC: handler → service → repository |
| Trung bình | Nhiều quy tắc nhưng ổn định, vài module rõ ràng | Modular monolith, mỗi module có ranh giới và interface riêng |
| Phức tạp | Nghiệp vụ thay đổi liên tục, nhiều bounded context, nhiều thuật ngữ riêng | DDD kết hợp Clean / Hexagonal Architecture để cô lập business logic |

Dùng DDD cho một app CRUD chỉ làm code dài thêm mà không mang lại lợi ích.

**Tính nhất quán dữ liệu**

| Yêu cầu | Ví dụ | Lựa chọn |
| --- | --- | --- |
| Nhất quán tuyệt đối (ACID) | Chuyển tiền, trừ tồn kho, đặt chỗ | SQL (PostgreSQL), transaction trong cùng một database |
| Nhất quán cuối cùng (eventual) chấp nhận được | Lượt thích, thống kê, feed, thông báo | Vẫn dùng PostgreSQL được; thêm cache, NoSQL hoặc đồng bộ qua event khi tải đòi hỏi |
| Giao dịch trải qua nhiều service | Đơn hàng → thanh toán → kho → giao hàng | Saga pattern (bước bù khi lỗi). Tránh 2PC vì chậm và dễ kẹt |

**Hệ quả quan trọng:** ngay khi tách thành nhiều service có database riêng, bạn mất transaction ACID giữa chúng và phải tự xử lý bằng Saga, outbox, retry. Đây là lý do lớn nhất để không tách microservices sớm.

## 4. Đội ngũ, ngân sách và hạ tầng

**Quy mô và năng lực đội ngũ**

- **Định luật Conway:** cấu trúc của hệ thống phản ánh cấu trúc của tổ chức tạo ra nó. Một team thì nên có một deployable; nhiều team độc lập mới cần nhiều service.
- **Điều kiện tiên quyết trước khi dùng microservices** ([Martin Fowler](https://martinfowler.com/bliki/MicroservicePrerequisites.html)). Thay vì đếm số người, hãy kiểm tra team đã có đủ 4 năng lực này chưa:
    - Dựng server mới trong vài giờ (rapid provisioning).
    - Monitoring cơ bản cho cả chỉ số kỹ thuật lẫn nghiệp vụ, và rollback được nhanh.
    - Pipeline deploy lên test và production trong tối đa vài giờ.
    - Văn hóa DevOps: dev và vận hành cùng xử lý sự cố.
- **Không có con số “bao nhiêu người” chuẩn.** Thiếu một trong 4 năng lực trên thì chưa nên dùng microservices, dù team đông hay ít. Các mốc kiểu “dưới 5–10 người” chỉ là kinh nghiệm truyền miệng, không có nguồn chuẩn.
- **Kỹ năng hiện có:** ưu tiên kiến trúc và công nghệ team đã làm thực tế, trừ khi dự án có mục tiêu R&D dài hạn.

**Ngân sách và thời gian ra mắt**

| Giai đoạn | Ưu tiên | Kiến trúc thiên về |
| --- | --- | --- |
| MVP / startup thử ý tưởng | Tốc độ ra mắt, dễ sửa, chi phí thấp | Monolith hoặc BaaS, 1 VPS hoặc PaaS |
| Sản phẩm đã có khách, đang tăng trưởng | Ổn định, mở rộng được từng phần | Modular monolith + cache, queue, worker |
| Hệ thống lõi doanh nghiệp (5–10 năm) | Ổn định, dễ bảo trì, kiểm toán được | Ranh giới domain rõ, tách service khi có lý do cụ thể |

Kiến trúc phân tán tốn hơn nhiều, không chỉ ở tiền cloud mà còn ở công cụ giám sát và nhân sự vận hành.

**Hạ tầng và hệ sinh thái sẵn có**

- **Tích hợp hệ thống cũ:** ERP, cổng thanh toán, hóa đơn điện tử, hệ thống ngân hàng. Nên có một integration layer (adapter) riêng để lỗi hay thay đổi phía đối tác không lan vào business logic.
- **On-premise:** hạ tầng của khách có thể không hỗ trợ container, Kubernetes hay dịch vụ cloud. Nên xác nhận sớm.
- **Hệ sinh thái đã có:** nếu công ty đã dùng sẵn một cloud, một loại database hoặc công cụ monitoring, đi theo nó thường rẻ hơn chọn cái “tốt nhất”.

## 5. Khi code cùng AI: điều gì thay đổi?

Với Claude Code, GitHub Copilot hay vibe coding, **chi phí viết code giảm mạnh**. Nhưng **chi phí vận hành, chi phí sai và chi phí review thì không giảm**. Kiến trúc vì vậy vẫn theo 5 nhóm yếu tố trên, nhưng có thêm một câu hỏi mới: *AI có hiểu và sửa đúng được hệ thống này không?*

| Không thay đổi | Thay đổi |
| --- | --- |
| NFRs: uptime, độ trễ, bảo mật vẫn do bài toán quyết định | Viết boilerplate gần như miễn phí: Clean Architecture, DTO, test không còn “tốn công” như trước |
| Hệ phân tán vẫn khó: lỗi mạng, eventual consistency, Saga. AI viết code nhưng không trực sự cố lúc 3 giờ sáng | **Context** trở thành giới hạn mới: AI làm tốt khi một tính năng nằm gọn trong ít file, một repo |
| Chi phí hạ tầng và vận hành microservices | **Review** trở thành nút thắt: code ra nhanh hơn con người đọc kịp |
| Con người vẫn chịu trách nhiệm khi hệ thống lỗi | Refactor và migrate rẻ hơn, nên “bắt đầu đơn giản, tách sau” càng hợp lý |
| | Team nhỏ làm được nhiều hơn, nhưng **năng lực vận hành** vẫn là của số người thật |

Báo cáo [DORA 2025](https://dora.dev/research/ai) của Google, khảo sát gần 5.000 người làm phần mềm, kết luận **AI là bộ khuếch đại**: nó phóng to điểm mạnh của team tốt và cả điểm yếu của team đang gặp vấn đề. Team có kiến trúc ít phụ thuộc lẫn nhau (loosely coupled) và vòng phản hồi nhanh thì hưởng lợi rõ rệt. Team bị kiềm bởi hệ thống phụ thuộc chặt chẽ và quy trình chậm thì gần như không được lợi gì. Làm việc theo lô nhỏ (small batches) càng quan trọng khi dùng AI.

“Ít phụ thuộc” nói về ranh giới giữa các phần, không bắt buộc phải tách thành nhiều service. Một modular monolith có ranh giới rõ cũng đạt được điều này.

**Kiến trúc “thân thiện với AI”**

- **Modular monolith + monorepo** càng hợp lý: AI thấy được toàn bộ luồng của một tính năng. Microservices chia ở nhiều repo khiến AI thiếu context và dễ làm hỏng contract giữa các service.
- **Feature-first, vertical slice:** mỗi tính năng một thư mục, file nhỏ, tên rõ. AI tìm đúng chỗ cần sửa nhanh hơn.
- **Một pattern duy nhất, lặp lại:** AI bắt chước code đang có. Module đầu tiên chính là template cho mọi module sau, nên phải làm thật chuẩn. Một pattern xấu cũng sẽ bị nhân bản khắp nơi.
- **Kiểu dữ liệu chặt và contract rõ:** Go, Dart, TypeScript, Python với Pydantic; OpenAPI; sinh code từ schema (sqlc, client generator). Compiler và type checker bắt lỗi của AI trước khi bạn phải bắt.
- **Test chạy nhanh:** agent tự chạy test để kiểm tra. Kiến trúc phải dễ test: tách logic khỏi framework, inject dependency.
- **Công nghệ phổ biến, “nhàm chán”:** AI viết tốt với stack phổ biến, nhiều tài liệu. Framework mới hoặc ít người dùng dễ khiến AI bịa API. Ghi rõ phiên bản trong tài liệu dự án.
- **Ranh giới được kiểm tra tự động:** đừng chỉ viết “module A không được gọi module B” trong tài liệu. Hãy dùng linter, test kiến trúc hoặc hook để build báo lỗi khi vi phạm, giống cách Shopify dùng Packwerk. AI sẽ tuân thủ vì bị build chặn.
- **Tài liệu là một phần của kiến trúc:** `ARCHITECTURE.md`, ADR và file hướng dẫn cho AI giúp mọi phiên AI hiểu cùng một kiến trúc.
    - [`AGENTS.md`](https://agents.md) là định dạng mở dùng chung cho nhiều công cụ (Copilot, Codex, Cursor, Gemini…).
    - Copilot đọc `.github/copilot-instructions.md` và `AGENTS.md`.
    - Claude Code đọc `CLAUDE.md`; các bản gần đây có thể đọc `AGENTS.md` khi repo không có `CLAUDE.md` (kiểm tra changelog của bản bạn dùng).
    - Team chỉ dùng Claude Code: một file `CLAUDE.md` là đủ (mẫu: [templates/CLAUDE.md](../templates/CLAUDE.md)).
    - Team dùng nhiều công cụ AI: viết nội dung chung trong `AGENTS.md`; `CLAUDE.md` chỉ cần dòng `@AGENTS.md` để import, cộng với phần riêng cho Claude nếu có. Các guide khác trong repo này gọi chung là `CLAUDE.md`.

**Claude Code và Copilot: có khác gì cho kiến trúc?**

| Cách dùng | AI nhìn thấy | Ảnh hưởng |
| --- | --- | --- |
| Gợi ý inline (Copilot autocomplete) | File đang mở và vài file liên quan | Cần pattern nhất quán và tên rõ để gợi ý đúng |
| Agent (Claude Code, Copilot agent mode) | Cả repo, chạy được lệnh, test, build | Cần tài liệu kiến trúc, test tự động và ranh giới được kiểm tra bằng máy |

Lựa chọn kiến trúc không phụ thuộc vào công cụ nào. Cả hai đều làm tốt nhất với cùng một kiểu codebase: gọn, nhất quán, có kiểu dữ liệu và có test.

**Vibe coding: dùng đúng chỗ**

| Giai đoạn | Vibe coding (AI tự làm, ít review) |
| --- | --- |
| Prototype, demo, thử ý tưởng vài ngày | Phù hợp. Chấp nhận vứt đi sau khi có kết luận |
| MVP có người dùng thật | Chỉ sau khi đã chốt kiến trúc, schema, auth. Review phần bảo mật và dữ liệu |
| Hệ thống production, dữ liệu tiền, dữ liệu cá nhân | Không. AI vẫn viết code, nhưng mọi thay đổi phải qua plan, test và review |

Rủi ro thường gặp khi vibe coding lâu dài: kiến trúc trôi dần (mỗi chỗ một kiểu), thư viện thêm tràn lan, lỗ hổng bảo mật không ai đọc tới. Quyết định kiến trúc vẫn nên do con người chốt và ghi thành ADR. AI đề xuất và phản biện, bạn quyết.

## 6. Các kiểu kiến trúc và khi nào dùng

Các lựa chọn dưới đây không loại trừ nhau. Một hệ thống thường là modular monolith, bên trong mỗi module theo Clean Architecture, và có thêm vài thành phần event-driven.

**Kiến trúc triển khai (hệ thống chia thành bao nhiêu phần chạy riêng)**

| Kiến trúc | Phù hợp khi | Tránh khi |
| --- | --- | --- |
| Monolith | MVP, team 1–3 người, nghiệp vụ đơn giản | Code bắt đầu rối, nhiều team sửa cùng chỗ |
| Modular monolith | Mặc định cho đa số dự án: 1 deploy, module có ranh giới rõ, dễ tách sau này | Một module cần scale hoặc release hoàn toàn độc lập |
| Microservices | Nhiều team độc lập, các phần có tải rất khác nhau, đã có DevOps trưởng thành | Team nhỏ, domain chưa rõ, cần ra mắt nhanh |
| Serverless (FaaS) | Tải thất thường, xử lý theo sự kiện, muốn không quản lý server | Cần kết nối lâu (WebSocket), độ trễ ổn định, tải cao liên tục |
| BaaS (Supabase, Firebase) | MVP cần auth, DB, storage có sẵn; ít logic phía server | Logic nghiệp vụ phức tạp, sợ phụ thuộc nhà cung cấp |

**Kiến trúc code (tổ chức code bên trong)**

| Kiến trúc | Phù hợp khi |
| --- | --- |
| Layered / MVC | CRUD, logic đơn giản |
| Clean / Hexagonal | Logic nghiệp vụ quan trọng, muốn đổi database hay framework mà không đụng logic, cần test dễ |
| DDD | Domain phức tạp, nhiều bounded context, có chuyên gia nghiệp vụ tham gia |

**Mẫu xử lý dữ liệu và giao tiếp**

| Mẫu | Phù hợp khi |
| --- | --- |
| Background job + queue | Việc nặng hoặc chậm không cần trả kết quả ngay |
| Event-Driven | Nhiều phần cần phản ứng với cùng một sự kiện, muốn giảm phụ thuộc trực tiếp |
| CQRS | Phía đọc và phía ghi khác nhau rõ rệt về tải hoặc mô hình dữ liệu |
| Event Sourcing | Cần lịch sử đầy đủ mọi thay đổi (tài chính, kiểm toán). Phức tạp, chỉ dùng khi thật cần |
| Offline-first (mobile) | Người dùng hay mất mạng, cần app phản hồi ngay |

## 7. Cây quyết định

**Nguyên tắc: bắt đầu đơn giản, chỉ tách service khi có lý do cụ thể.** Trả lời từ trên xuống:

1. **MVP, ít logic phía server, 1–2 dev, cần ra mắt rất nhanh?**
    - Có → **BaaS hoặc monolith đơn giản** (Supabase/Firebase, hoặc 1 API + 1 DB).
    - Không → câu 2.
2. **Nhiều team độc lập, DevOps trưởng thành (CI/CD, monitoring)?**
    - Không → **Modular monolith (mặc định)**: 1 deploy, module có ranh giới rõ.
    - Có → câu 3.
3. **Có phần cần tải, công nghệ hoặc team riêng hẳn?**
    - Có → **Tách riêng phần đó thành service**, phần còn lại vẫn là modular monolith.
    - Không → **Giữ modular monolith**, tối ưu module, cache, query trước khi tách.

**Bổ sung theo nhu cầu, với bất kỳ lựa chọn nào ở trên:**

| Nhu cầu | Thêm |
| --- | --- |
| Việc chậm, tải đột biến | Queue + background worker |
| Đọc nhiều, cần nhanh | Cache, read replica, CQRS |
| Domain phức tạp | DDD + Clean Architecture |

Đa số dự án dừng ở modular monolith, rồi thêm queue, cache hay DDD khi có nhu cầu cụ thể ở phần 2 và 3.

## 8. Ví dụ áp dụng với Flutter + Go/FastAPI + PostgreSQL

| Tình huống | Yếu tố nổi bật | Kiến trúc đề xuất |
| --- | --- | --- |
| App quản lý chi tiêu cá nhân, 1 dev, MVP 4 tuần | Domain đơn giản, ngân sách thấp, user hay mất mạng | Flutter offline-first (drift) + 1 API monolith (Go hoặc FastAPI) + PostgreSQL, Docker Compose trên 1 VPS. Backend chia module theo tính năng (`internal/expense`, `internal/user`), bên trong mỗi module là layered handler → service → repository. Đây là ví dụ xuyên suốt trong [Dùng Claude xây dựng sản phẩm từ ý tưởng](claude-tu-y-tuong-den-san-pham.md) |
| App bán hàng cho chuỗi 50 cửa hàng, team 4 người | Trừ tồn kho cần ACID, có báo cáo nặng, nối hóa đơn điện tử | Modular monolith Go (module: đơn hàng, kho, khách hàng, báo cáo), Redis + worker cho báo cáo, read replica, adapter riêng cho hóa đơn điện tử. POS Flutter offline-first |
| Nền tảng có tính năng AI (tóm tắt, gợi ý), team 6 người | Phần AI tốn tài nguyên và chậm, phần còn lại là CRUD | Core API Go (modular monolith) + 1 service AI riêng bằng FastAPI, giao tiếp qua queue. `pgvector` cho semantic search |
| Hệ thống thanh toán cho doanh nghiệp, yêu cầu 99,99% | Tuân thủ bảo mật, audit, ACID, không được mất giao dịch | Clean Architecture, tách riêng vùng xử lý thanh toán, outbox pattern, nhiều instance + failover DB, audit log bất biến |

Chú ý: cả bốn trường hợp đều **chưa cần microservices**. Chỉ tách thêm service khi có một lý do cụ thể: tải khác biệt, công nghệ khác biệt, hoặc team khác phụ trách.

## 9. Ghi lại quyết định và dùng Claude hỗ trợ

**Mẫu ADR (Architecture Decision Record)**

Mỗi quyết định kiến trúc quan trọng ghi thành một file `docs/adr/0001-<ten>.md`. Sau này khi xem lại, bạn sẽ biết vì sao đã chọn như vậy và khi nào nên đổi.

Mẫu [templates/ADR.md](../templates/ADR.md) rút gọn từ mẫu phổ biến của Michael Nygard. Repo [joelparkerhenderson/architecture-decision-record](https://github.com/joelparkerhenderson/architecture-decision-record) trên GitHub có thêm nhiều mẫu khác (MADR, Y-statement…) và ví dụ.

Các phần chính: bối cảnh (con số NFR, ràng buộc team, ngân sách, hạ tầng), các phương án kèm ưu nhược, quyết định và lý do, hệ quả chấp nhận được, và dấu hiệu cụ thể để xem lại (vd hơn 1.000 request/giây, team hơn 10 người).

**Prompt mẫu: phỏng vấn để thu thập yêu cầu**

```text
Bạn là software architect. Tôi sắp chọn kiến trúc cho dự án: <mô tả ngắn>.
Phỏng vấn tôi theo 5 nhóm: NFRs, nghiệp vụ, đội ngũ, ngân sách và thời gian, hạ tầng sẵn có.
Mỗi lần hỏi 3–4 câu, đợi tôi trả lời. Câu nào tôi không biết thì ghi lại là giả định.
Cuối cùng tóm tắt thành bảng yêu cầu, có con số cụ thể.
```

**Prompt mẫu: đề xuất và so sánh phương án**

```text
Dựa trên bảng yêu cầu ở trên, đề xuất 2–3 phương án kiến trúc (stack: <Flutter + Go/FastAPI + PostgreSQL>).
Mỗi phương án: sơ đồ thành phần (Mermaid), chi phí hạ tầng ước tính/tháng, công sức vận hành,
điểm nghẽn khi tải tăng x10, cách nâng cấp sau này.
So sánh trong một bảng, rồi đề xuất phương án phù hợp nhất với giai đoạn hiện tại và viết thành ADR-0001 theo templates/ADR.md.
```

**Prompt mẫu: phản biện kiến trúc đã chọn**

```text
Đây là kiến trúc tôi định dùng: <dán ADR hoặc mô tả>.
Hãy đóng vai architect khó tính. Tìm: điểm lỗi đơn (single point of failure), chỗ quá phức tạp so với nhu cầu,
chỗ chưa đáp ứng NFR, rủi ro về dữ liệu và bảo mật. Xếp theo mức nghiêm trọng, kèm cách khắc phục.
```

**Prompt mẫu: có nên tách service không**

```text
Hệ thống hiện tại: <mô tả modular monolith, số liệu tải, team>.
Tôi đang cân nhắc tách module <tên> thành service riêng vì <lý do>.
Phân tích: lợi ích thật, chi phí vận hành thêm, ảnh hưởng tới tính nhất quán dữ liệu,
và phương án thay thế không cần tách (cache, worker, tối ưu query). Kết luận rõ nên hay chưa.
```

## 10. Bài học từ các công ty thật

| Trường hợp | Chuyện gì đã xảy ra | Bài học |
| --- | --- | --- |
| [Martin Fowler – MonolithFirst](https://martinfowler.com/bliki/MonolithFirst.html) | Fowler nhận thấy hầu hết câu chuyện microservices thành công đều bắt đầu từ một monolith lớn dần rồi được tách ra | Bắt đầu bằng monolith, chỉ tách khi ranh giới domain đã rõ |
| [Shopify](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity) | Một trong những codebase Rails lớn nhất. Thay vì chuyển sang microservices, họ chọn modular monolith: một codebase, ranh giới giữa các component được định nghĩa và bắt buộc tuân thủ. Viết công cụ [Packwerk](https://github.com/Shopify/packwerk) để kiểm tra ranh giới | Modular monolith chạy được ở quy mô rất lớn, nếu ranh giới được công cụ kiểm tra |
| [Twilio Segment](https://segment.com/blog/goodbye-microservices) | Tách thành hơn 140 microservices, chi phí vận hành tăng theo từng service. Sau khi gộp lại một service, một kỹ sư làm trong vài phút việc trước đây phải deploy hơn 140 service. Đánh đổi: mất cô lập lỗi giữa các phần | Mỗi service thêm vào cộng thêm chi phí vận hành. Gộp lại cũng có cái giá |
| [Amazon Prime Video (2023)](https://web.archive.org/web/20230504060528/https://www.primevideotech.com/video-streaming/scaling-up-the-prime-video-audio-video-monitoring-service-and-reducing-costs-by-90) | Dịch vụ giám sát chất lượng stream chuyển từ kiến trúc phân tán (serverless) sang một ứng dụng monolith: chi phí hạ tầng giảm hơn 90%, scale tốt hơn. Đây chỉ là một dịch vụ, Prime Video nói chung không chuyển về monolith | Quyết định theo từng phần và theo số liệu chi phí thật, không theo phong trào |

Các trường hợp trên không chứng minh microservices là sai. Chúng cho thấy microservices có “phụ phí” lớn, chỉ đáng trả khi có lý do cụ thể và đủ năng lực vận hành.

## Nguồn

**Nguyên tắc kiến trúc**

- [Microservice Prerequisites – Martin Fowler](https://martinfowler.com/bliki/MicroservicePrerequisites.html)
- [MonolithFirst – Martin Fowler](https://martinfowler.com/bliki/MonolithFirst.html)
- [Microservices Guide – Martin Fowler](https://martinfowler.com/microservices/)
- [ISO/IEC 25010:2023 – Product quality model](https://www.iso.org/standard/78176.html)

**Độ tin cậy**

- [Availability Table – Google SRE Book](https://sre.google/sre-book/availability-table/)
- [Embracing Risk – Google SRE Book](https://sre.google/sre-book/embracing-risk/)

**AI và phát triển phần mềm**

- [DORA 2025 – State of AI-assisted Software Development](https://dora.dev/research/ai)
- [AGENTS.md – định dạng mở cho coding agent](https://agents.md)
- [GitHub Copilot – Custom instructions support](https://docs.github.com/en/copilot/reference/custom-instructions-support)
- [Claude Code hỗ trợ AGENTS.md – DevOps.com](https://devops.com/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/)

**Case study**

- [Deconstructing the Monolith – Shopify Engineering](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity)
- [Shopify/packwerk – GitHub](https://github.com/Shopify/packwerk)
- [Goodbye Microservices – Twilio Segment](https://segment.com/blog/goodbye-microservices)
- [Prime Video monitoring service – Prime Video Tech (bản lưu)](https://web.archive.org/web/20230504060528/https://www.primevideotech.com/video-streaming/scaling-up-the-prime-video-audio-video-monitoring-service-and-reducing-costs-by-90)

**Repo GitHub tham khảo thêm**

- [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer)
- [joelparkerhenderson/architecture-decision-record](https://github.com/joelparkerhenderson/architecture-decision-record)
