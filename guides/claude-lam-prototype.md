# Dùng Claude làm prototype cho Designer, BA, PM

Cập nhật: 2026-11-12

Dành cho **Designer, BA, PM** muốn biến ý tưởng thành prototype bấm thử được trong vài giờ thay vì vài tuần, rồi bàn giao cho dev mà không phải giải thích lại từ đầu. Không cần biết code.

Cách đọc: mục 1–3 để hiểu quy trình, mục 4–6 lấy prompt theo vai của bạn, mục 7 xem ví dụ trọn vẹn, mục 8–9 để test với user và bàn giao.

## 1. Tổng quan

**Prototype** là bản mô phỏng sản phẩm đủ để người khác **xem và bấm thử**, làm ra để trả lời một câu hỏi trước khi tốn tiền code thật: user có hiểu không, flow có trôi không, khách hàng có đồng ý không.

### Các mức độ chi tiết (fidelity)

| Mức | Trông như thế nào | Trả lời câu hỏi | Với Claude |
| --- | --- | --- | --- |
| **Sketch** | Phác tay, ô và chữ | Cần những màn nào? | Vài phút, ngay trong chat |
| **Wireframe** | Khung xám, đúng bố cục, chưa có màu | Nội dung nào ở đâu? Thứ tự ưu tiên? | 10–30 phút |
| **Mockup** | Đủ màu, font, icon, dữ liệu mẫu | Trông có đúng thương hiệu? Khách có duyệt? | 30–60 phút |
| **Prototype tương tác** | Bấm chuyển màn, nhập liệu, có trạng thái lỗi/rỗng | User có tự làm xong việc không? | 1–3 giờ |

Nguyên tắc: **làm ở mức thấp nhất đủ trả lời câu hỏi đang có**. Khi còn tranh luận "có nên làm tính năng này không", đừng chỉnh màu. Với AI, làm bản chi tiết rất rẻ, nên bẫy dễ gặp là đánh bóng quá sớm.

### Ai làm gì

| Vai | Đầu vào | Đầu ra cho prototype |
| --- | --- | --- |
| **PM** | Ý tưởng, mục tiêu kinh doanh, phản hồi khách | Brief, PRD 1 trang, phạm vi MVP, tiêu chí thành công |
| **BA** | Brief, quy trình nghiệp vụ hiện tại | User story, acceptance criteria, user flow, dữ liệu mẫu |
| **Designer** | Flow, dữ liệu mẫu, thương hiệu | Wireframe → mockup → prototype tương tác, design system |
| **Dev** | Prototype + spec | Xác nhận khả thi, ước lượng, code thật |

Trong team nhỏ, một người có thể ôm cả 3 vai đầu. Claude giúp mỗi vai làm nhanh hơn, nhưng **quyết định làm gì và cho ai vẫn là của người**.

## 2. Chọn công cụ

| Công cụ | Mạnh ở | Dùng khi |
| --- | --- | --- |
| **Claude chat** (claude.ai, app) | Nghĩ, viết, phản biện: brief, PRD, user story, flow, nội dung màn hình | Mọi bước trước khi vẽ. Giữ mỗi dự án trong 1 **Project** để Claude nhớ tài liệu |
| **Claude Design** | Mockup, prototype tương tác, design system, slide, one-pager trên canvas | Wireframe → prototype; tạo nhiều hướng thiết kế để so sánh; bàn giao sang Claude Code |
| **Artifact / Docs** trong chat | Tài liệu có link chia sẻ, bình luận được | PRD, spec, tài liệu bàn giao |
| **Figma** (+ Figma MCP) | File thiết kế chuẩn của team, component, Dev Mode | Team đã có design system trên Figma; cần pixel-perfect |
| **Claude Code** | Prototype chạy bằng code thật, dữ liệu thật, đọc được codebase | Prototype cần gọi API thật, hoặc dev nhận bàn giao để code |

Vài điểm cần biết về **Claude Design**:

- Ra mắt tháng 4/2026, thuộc Anthropic Labs, đang ở dạng research preview. Có cho gói Pro, Max, Team, Enterprise (Enterprise do admin bật).
- Đọc được codebase và file thiết kế của team để áp màu, font, component đúng thương hiệu.
- Đóng gói bản thiết kế thành **handoff bundle cho Claude Code**, mang theo ý đồ thiết kế sang bước code.
- Tốn token nhiều hơn chat thường: một design system + vài màn có thể đốt một phần lớn hạn mức tuần. Chốt flow và nội dung ở chat trước rồi mới sang Design.

Về **Figma MCP**: Figma có MCP server chính thức (`https://mcp.figma.com/mcp`) cho Claude Code đọc frame (layout, màu, font, component). Gói Figma miễn phí bị giới hạn số lượt gọi rất thấp, nên kiểm tra gói trước khi lấy đây làm quy trình chính.

**Chọn nhanh:** team chưa có Figma → chat + Claude Design. Team đã có Figma → chat cho nội dung, Figma cho thiết kế chính thức, Claude Design để khám phá nhanh nhiều hướng.

## 3. Quy trình 7 bước

**Prototype chỉ sang bàn giao khi user tự làm xong việc.**

1. **Brief** — PM
2. **PRD + MVP** — PM
3. **Story + flow** — BA
4. **Wireframe** — Designer
5. **Prototype** — Designer
6. **Test với user** — cả team, 5 user. Đạt → bước 7; user chưa làm được → quay lại bước 5 sửa
7. **Bàn giao dev** — PM + BA + Designer

Vòng lặp quan trọng nhất là 5 ↔ 6: sửa prototype cho đến khi user tự làm xong việc mà không cần hỏi. Thường mất 2–3 vòng.

| Bước | Đầu ra | Thời gian với Claude |
| --- | --- | --- |
| 1. Brief | 1 đoạn: vấn đề, cho ai, đo thành công bằng gì | 15 phút |
| 2. PRD + MVP | PRD 1 trang, danh sách tính năng MUST / SHOULD / COULD / WON'T | 1 giờ |
| 3. Story + flow | User story + acceptance criteria, sơ đồ flow, dữ liệu mẫu | 1–2 giờ |
| 4. Wireframe | Khung xám các màn chính | 30 phút |
| 5. Prototype | Bấm thử được, đủ trạng thái loading / rỗng / lỗi | 1–3 giờ |
| 6. Test với user | 5 phiên test, danh sách vấn đề theo mức độ | 1 ngày |
| 7. Bàn giao dev | Gói bàn giao: spec, prototype, dữ liệu mẫu, câu hỏi mở | 1–2 giờ |

Mẹo xuyên suốt: tạo **1 Claude Project cho mỗi dự án**, đưa brief, PRD, story vào phần tài liệu của Project. Mọi chat sau đó Claude đều đã biết bối cảnh, không phải dán lại.

## 4. Prompt mẫu cho PM

### 4.1 Từ ý tưởng mơ hồ → brief

```
Mình có ý tưởng: <mô tả 1–3 câu>.
Trước khi viết gì, hỏi mình tối đa 5 câu để làm rõ: ai dùng, họ đang giải quyết việc này thế nào,
vì sao cách cũ chưa ổn, đo thành công bằng gì, ràng buộc (thời gian, ngân sách, nền tảng, số người làm).
Sau khi mình trả lời, viết brief ≤ 150 chữ: Vấn đề · Người dùng · Giải pháp đề xuất · Chỉ số thành công · Ngoài phạm vi.
```

### 4.2 Kiểm chứng trước khi làm

Bật Web search hoặc Research trước khi gửi.

```
Tìm trên web các sản phẩm đang giải quyết vấn đề: <vấn đề>, ưu tiên thị trường <Việt Nam / quốc tế>.
Với 5–10 sản phẩm nổi bật: nền tảng, lượt tải hoặc traffic, làm tốt gì, user phàn nàn gì
(review 1–2 sao trên App Store / Google Play, diễn đàn), giá, mô hình kiếm tiền.
Có tín hiệu nhu cầu nào không (nhóm Facebook, Reddit, lượng tìm kiếm)?
Kết luận: khoảng trống còn lại, 3 rủi ro lớn nhất khiến ý tưởng này thất bại,
3 cách kiểm chứng rẻ nhất trong 2 tuần, Go / No-go kèm 3 lý do.
Ghi nguồn cho từng nhận định. Không có nguồn thì ghi rõ là suy đoán.
```

### 4.3 PRD 1 trang

```
Viết PRD 1 trang từ brief và kết quả kiểm chứng (dán bên dưới):
1. Bối cảnh & vấn đề  2. Mục tiêu + chỉ số (có số cụ thể)  3. Persona (1–2)
4. User journey chính (5–7 bước)  5. Tính năng  6. Ngoài phạm vi
7. Giả định cần kiểm chứng  8. Ràng buộc và yêu cầu phi chức năng (thời gian, ngân sách, nền tảng,
offline, bảo mật, số user dự kiến)  9. Câu hỏi mở
Không viết user story (làm riêng ở bước BA), không viết giải pháp kỹ thuật. Giả định nào bạn tự thêm thì đánh dấu [GIẢ ĐỊNH].
Theo mẫu templates/PRD.md nếu mình đính kèm.
```

### 4.4 Cắt phạm vi MVP

```
Xếp các tính năng trong PRD theo MoSCoW (MUST / SHOULD / COULD / WON'T) cho MVP
làm trong <số> tuần với <số> người. MUST = thiếu nó thì user không hoàn thành được journey chính.
Bảng: tính năng | nhóm | lý do | ước lượng S/M/L.
Phản biện mình nếu MUST chiếm > 40% tổng số.
```

### 4.5 Chọn câu hỏi cho prototype

```
Từ mục "Giả định" trong PRD, chọn 3 giả định rủi ro nhất có thể kiểm bằng prototype.
Với mỗi cái: màn/flow cần làm, nhiệm vụ giao cho user khi test, dấu hiệu đạt / không đạt.
Màn nào không phục vụ 3 giả định này thì đừng làm trong prototype.
```

## 5. Prompt mẫu cho BA

### 5.1 User story + acceptance criteria

```
Từ PRD (đính kèm / đã có trong Project), viết user story cho các tính năng MUST.
Mỗi story: "Là <vai>, tôi muốn <việc>, để <lợi ích>" + acceptance criteria dạng Given / When / Then.
Mỗi story xét đủ 5 nhóm criteria: happy path, input sai, không có quyền, dữ liệu trống, giá trị biên;
nhóm nào không áp dụng thì ghi N/A kèm lý do. Story > 10 criteria thì tách nhỏ. Đánh số US-01, US-02…
Theo mẫu templates/user-story.md.
```

### 5.2 User flow

```
Vẽ user flow cho <journey> bằng Mermaid flowchart:
màn hình = hình chữ nhật, quyết định = hình thoi, hành động hệ thống = hình tròn.
Gồm nhánh lỗi (mất mạng, hết phiên, dữ liệu rỗng, không có quyền) và đường quay lại.
Sau sơ đồ: danh sách màn hình (ID S-01…, tên, mục đích, story liên quan).
```

### 5.3 Quy tắc nghiệp vụ

```
Liệt kê quy tắc nghiệp vụ ẩn trong các story: giới hạn, điều kiện, công thức tính, phân quyền, trạng thái.
Bảng: ID BR-01… | quy tắc | ví dụ có số cụ thể | story liên quan | ai xác nhận.
Quy tắc nào bạn suy ra chứ không có trong PRD → ghi "cần PM xác nhận".
```

### 5.4 Dữ liệu mẫu

```
Tạo dữ liệu mẫu dạng JSON, tiếng Việt, giống thật, cho <tính năng>:
- 3 user khác vai, tên Việt có dấu (có 1 tên rất dài)
- đủ ca: list rỗng, 1 phần tử, 50 phần tử, giá trị biên, ngày quá khứ / tương lai
- tiền VND (số nguyên), ngày trong JSON dạng ISO 8601 (hiển thị dd/mm/yyyy), số điện thoại +84 giả
Không dùng dữ liệu thật của ai. Kèm bảng: bộ dữ liệu nào dùng cho màn / trạng thái / test nào.
```

### 5.5 Rà thiếu sót

```
Đóng vai dev và tester khó tính. Đọc story, flow, quy tắc và liệt kê:
- mâu thuẫn giữa story và flow
- trường hợp chưa nói tới (hủy giữa chừng, làm 2 lần, 2 người cùng sửa, offline, hết hạn)
- câu chữ mơ hồ dev sẽ phải hỏi lại ("nhanh", "dễ", "phù hợp", "khoảng")
Mỗi mục 1 dòng + đề xuất cách viết lại.
```

## 6. Prompt mẫu cho Designer

### 6.1 Design system trước, màn hình sau

Làm design system một lần thì mọi màn sau đều đồng bộ. Nếu đã có app/web, đưa link repo hoặc ảnh chụp để Claude Design đọc theo.

```
Tạo design system cho <tên sản phẩm> — <cảm giác: vd trang nhã, trẻ trung, dễ đọc cho người lớn tuổi>.
Gồm: bảng màu (primary, neutral, success / warning / error, cả dark mode), font hỗ trợ tiếng Việt đủ dấu,
thang cỡ chữ, spacing 4/8, bo góc, component: button, input, card, list item, tab bar, dialog, toast, empty state.
Contrast đạt WCAG AA, vùng chạm ≥ 44pt (iOS) / 48dp (Android). Theo repo / ảnh đính kèm nếu có.
```

### 6.2 Wireframe

```
Từ danh sách màn S-01…S-xx và user flow (đính kèm), vẽ wireframe xám cho <mobile 390×844 / desktop 1440>:
chỉ bố cục, nội dung thật từ dữ liệu mẫu, không màu, không ảnh.
Mỗi màn ghi ID + story liên quan. Cho 2 phương án bố cục khác hẳn nhau cho màn <quan trọng nhất>.
```

### 6.3 Mockup nhiều hướng

```
Áp design system vào wireframe đã chọn. Làm 3 hướng thị giác khác nhau cho màn <S-01>
(vd: tối giản / ấm áp / hiện đại nhiều màu). Mỗi hướng 1 dòng ưu / nhược.
Chưa làm các màn khác, chờ mình chọn.
```

### 6.4 Prototype tương tác

```
Nối các màn thành prototype bấm được theo user flow:
- nhập liệu thật được, có validate và thông báo lỗi theo acceptance criteria
- mỗi màn có 4 trạng thái: loading, có dữ liệu, rỗng, lỗi (có nút nhỏ để chuyển trạng thái khi demo)
- quay lại, hủy, xác nhận hoạt động đúng
- dữ liệu lấy từ JSON mẫu, đổi JSON là màn đổi theo
Chỉ làm các màn phục vụ <giả định cần test>.
```

### 6.5 Tự rà trước khi cho người khác xem

```
Rà <ảnh chụp / prototype / file UI> theo: 10 heuristic của Nielsen, contrast, vùng chạm,
text tiếng Việt dài bị cắt, cỡ chữ phóng to 200%, màn nhỏ 360×640, dark mode, thao tác một tay, đủ 4 trạng thái.
Bảng: màn | vấn đề | mức (cao / vừa / thấp) | cách sửa. Nếu là file UI sửa được thì sửa luôn mục mức cao.
```

Mẹo với Claude Design: **đặt giới hạn rõ trong prompt** (số màn, số hướng, kích thước). Prompt mở như "làm app cho tôi" sẽ sinh nhiều màn không cần, tốn token, và khó sửa.

## 7. Ví dụ: tính năng "Nhắc ngày giỗ" cho app gia phả

Ví dụ minh họa cho một app gia phả (Flutter, có nhà chung và gia phả), không phải kế hoạch thật của sản phẩm nào.

**Bước 1 — Brief (PM, 15 phút).** Sau 5 câu hỏi của Claude, ra brief:

> Con cháu xa nhà hay quên ngày giỗ theo âm lịch. Người dùng: thành viên nhà chung, 25–60 tuổi. Giải pháp: nhắc trước 7 ngày và 1 ngày, xem ai sẽ về, ghi đóng góp. Thành công: 60% nhà chung bật nhắc trong 1 tháng. Ngoài phạm vi: thanh toán online.

**Bước 2 — PRD + MVP (PM).** Claude xếp MoSCoW:

| Tính năng | Nhóm |
| --- | --- |
| Ngày giỗ từ gia phả (ngày mất âm lịch), đổi sang dương lịch từng năm | MUST |
| Thông báo trước 7 ngày / 1 ngày | MUST |
| Báo "tôi sẽ về" | SHOULD |
| Ghi đóng góp tiền / lễ vật | COULD |
| Livestream buổi giỗ | WON'T (bản này) |

Giả định rủi ro nhất cần test: *người lớn tuổi tự bật được nhắc cho một ngày giỗ trong 1 phút*.

**Bước 3 — Story + flow (BA).** Vài criteria Claude viết ra:

- *US-02 · giá trị biên:* Given người mất ngày 30 tháng Chạp, When năm âm lịch đó tháng Chạp chỉ có 29 ngày, Then giỗ vào ngày 29 và hiển thị ghi chú.
- *US-02 · không quyền:* Given thành viên không phải trưởng tộc, When sửa ngày giỗ, Then không thấy nút sửa.
- *US-03 · dữ liệu trống:* Given gia phả chưa có ai có ngày mất, Then hiện hướng dẫn thêm ngày mất, không hiện list rỗng.

Bước rà thiếu sót (5.5) bắt được thêm: *tháng nhuận* và *nhiều nhánh cùng giỗ một người*. Cả hai đưa vào câu hỏi mở cho PM.

**Bước 4–5 — Wireframe → prototype (Designer, Claude Design).** 4 màn: danh sách ngày giỗ · chi tiết 1 ngày giỗ · cài đặt nhắc · xác nhận "tôi sẽ về". Áp design system có sẵn của app, cỡ chữ lớn hơn mặc định vì nhóm tuổi lớn.

**Bước 6 — Test 5 người.** Giả sử kết quả: 3/5 không thấy nút bật nhắc vì nằm trong menu "…". Sửa: đưa nút ra ngoài, chữ "Nhắc tôi". Vòng 2: 5/5 làm được.

**Bước 7 — Bàn giao.** Tạo gói bàn giao theo mục 9, đính kèm link prototype, story US-01…US-05, quy tắc âm lịch BR-01…BR-03, JSON mẫu, 2 câu hỏi mở.

## 8. Test prototype với người dùng

**5 người là đủ cho một vòng.** Theo Nielsen Norman Group, 5 người cùng nhóm tìm ra khoảng 85% vấn đề usability. Có ngân sách cho 15 người thì chia thành 3 vòng × 5 người, sửa giữa các vòng. App có nhiều nhóm user khác hẳn nhau (vd người lớn tuổi và người trẻ) thì mỗi nhóm 3–4 người.

Claude **không thay được user thật**. Claude giúp chuẩn bị kịch bản và tổng hợp ghi chép; còn quan sát người dùng thật bấm sai ở đâu là việc phải làm trực tiếp.

### 8.1 Kịch bản test

```
Viết kịch bản usability test 20 phút cho prototype (3 giả định trong Project):
- 2 câu khởi động về thói quen hiện tại của họ
- 3 nhiệm vụ viết theo tình huống thật, KHÔNG chứa tên nút/menu (vd "Tháng sau là giỗ ông nội, bác muốn được nhắc trước")
- mỗi nhiệm vụ: dấu hiệu thành công, thời gian tối đa, câu hỏi sau nhiệm vụ
- 3 câu kết thúc, không hỏi "bác có thích không"
- lời dặn cho người dẫn: không gợi ý, không giải thích, hỏi "bác đang nghĩ gì?"
```

### 8.2 Tổng hợp sau test

```
Đây là ghi chép 5 phiên test (đã bỏ tên thật): <dán ghi chép hoặc transcript>.
Gom thành bảng: vấn đề | màn | số người gặp (x/5) | mức (chặn / khó chịu / nhỏ) | trích dẫn ngắn | đề xuất sửa.
Sắp xếp theo mức rồi số người. Chỉ đưa vào điều thấy trong ghi chép, không suy diễn.
Kết luận từng giả định: đúng / sai / chưa rõ.
```

Quyền riêng tư: xin phép trước khi ghi âm/ghi màn hình, bỏ tên và số điện thoại trước khi dán ghi chép vào Claude.

### 8.3 Khi nào dừng lặp

- Không còn vấn đề mức **chặn**.
- ≥ 4/5 người tự làm xong nhiệm vụ chính.
- 3 giả định đều có kết luận. Giả định sai → quay lại PM, có thể cắt tính năng. Đây là kết quả tốt: rẻ hơn nhiều so với biết điều này sau khi đã code.

## 9. Tạo tài liệu bàn giao cho dev

Mục tiêu: dev đọc xong là **ước lượng và bắt đầu code được**, không phải hỏi lại những thứ đã quyết. Prototype cho thấy "trông thế nào"; tài liệu bàn giao nói "chạy thế nào, đúng là gì, chưa chốt gì".

### 9.1 Gói bàn giao gồm gì

| Thành phần | Ai chuẩn bị | Dev dùng để |
| --- | --- | --- |
| Tài liệu bàn giao (mẫu ở 9.2) | BA, Claude viết nháp | Hiểu phạm vi, ước lượng, viết test |
| Ảnh chụp mọi màn và trạng thái, đặt tên theo mã màn | Designer | Đối chiếu khi code, Claude Code đọc |
| Link prototype (Claude Design / Figma) | Designer | Xem giao diện, flow |
| Handoff bundle Claude Design hoặc link frame Figma | Designer | Claude Code đọc thiết kế |
| Design system / token | Designer | Dùng đúng màu, font, component |
| User story + acceptance criteria | BA | Viết code + test |
| Dữ liệu mẫu JSON | BA | Seed DB, mock API, test |
| Kết quả test với user | Designer / PM | Hiểu vì sao thiết kế như vậy |

### 9.2 Mẫu tài liệu bàn giao

Dùng mẫu [templates/ban-giao-dev.md](../templates/ban-giao-dev.md), gồm 14 mục: tóm tắt · link · thuật ngữ · danh sách màn + user flow · chi tiết từng màn (bố cục, bảng field, trạng thái) · user story + acceptance criteria · quy tắc nghiệp vụ và công thức · validation · dữ liệu và API đề xuất · trường hợp biên · yêu cầu không chức năng · câu hỏi mở · tiêu chí nghiệm thu · lịch sử thay đổi.

Ba điểm làm tài liệu bàn giao khác với PRD:

- **Bảng field cho mọi form:** kiểu, bắt buộc, mặc định, quy tắc hợp lệ, thông báo lỗi. Đây là phần dev và QA hỏi lại nhiều nhất.
- **Công thức cho mọi con số trên UI** (tổng, badge, phần trăm) và quy tắc phụ thuộc giữa các field.
- **Mã duy nhất** (S-01, US-01, BR-01, VR-01, Q-01) để tham chiếu thay vì chép lại. Tính năng lớn thì tách thành nhiều file theo hướng dẫn ở đầu mẫu.

### 9.3 Prompt: Claude viết tài liệu bàn giao

Chạy trong Claude Project của dự án (đã có PRD, story, flow, kết quả test), đính kèm toàn bộ ảnh chụp màn hình các trạng thái. Prompt đầy đủ ở [prompts/ban-giao-va-phat-hanh.md](../prompts/ban-giao-va-phat-hanh.md#viết-tài-liệu-bàn-giao-cho-dev). Điểm chính của prompt:

1. Claude liệt kê từng ảnh thuộc màn nào, trạng thái nào trước khi viết, để không bỏ sót hay nhầm màn.
2. Viết đủ 14 mục theo mẫu; chỗ phải suy luận đánh dấu **[GIẢ ĐỊNH]** và đưa vào Câu hỏi mở.
3. Dữ liệu và API chỉ là đề xuất, dev quyết cuối.
4. Trả lời câu hỏi mở rồi cho Claude cập nhật ra bản thứ hai. **Đừng gửi dev bản đầu.**

Rồi để Claude tự rà trước khi gửi dev:

```
Đóng vai dev senior nhận tài liệu này. Liệt kê mọi câu bạn sẽ hỏi trước khi ước lượng:
thiếu trạng thái màn hình, quy tắc không rõ, dữ liệu thiếu trường, mâu thuẫn prototype với story,
phân quyền chưa nói, trường hợp lỗi / mất mạng. Sắp theo mức cản trở ước lượng.
```

### 9.4 Phía dev: nhận bàn giao bằng Claude Code

Dev có 3 đường đưa thiết kế vào Claude Code:

| Đường | Cách làm |
| --- | --- |
| Claude Design handoff bundle | Designer xuất bundle cho Claude Code; dev mở trong repo |
| Figma MCP | `claude mcp add --transport http figma https://mcp.figma.com/mcp`, rồi dán link frame |
| Ảnh chụp + tài liệu | Dán ảnh màn hình + file bàn giao .md vào repo (vd `docs/features/<ten>.md`) |

Prompt đầu tiên của dev, **chưa code**:

```
Đọc docs/features/<ten>.md và thiết kế (<handoff bundle / link Figma / ảnh>). Đọc CLAUDE.md và code hiện có.
Chưa viết code. Trả về:
1. Component / màn / API đã có trong repo dùng lại được (file:dòng)
2. Phần phải làm mới: màn, state, API, migration
3. Chỗ thiết kế lệch design system / component hiện có → hỏi lại hay theo code
4. Câu hỏi cho PM / BA / Designer (không trùng mục Câu hỏi mở)
5. Kế hoạch chia task, mỗi task ≤ 1 ngày, ước lượng S/M/L
```

Sau đó dev theo quy trình trong [Dùng Claude xây dựng sản phẩm từ ý tưởng](claude-tu-y-tuong-den-san-pham.md) và [Dùng Claude để test web app và mobile app](claude-test-web-mobile.md). Acceptance criteria trong bàn giao chính là đầu vào cho ma trận 5 nhóm test case.

### 9.5 Buổi bàn giao 30 phút

1. Gửi tài liệu + prototype trước 1 ngày. Dev chạy prompt 9.4, mang câu hỏi tới.
2. Designer demo prototype 5 phút, chỉ flow chính và trạng thái lỗi/rỗng.
3. 20 phút trả lời câu hỏi. Câu nào chưa trả lời được → ghi vào mục Câu hỏi mở, có người + hạn.
4. Chốt: tài liệu bàn giao là **nguồn duy nhất**. Thay đổi sau buổi này ghi vào Lịch sử thay đổi, không chỉ nói qua chat.

Prompt tóm tắt buổi họp:

```
Đây là ghi chép buổi bàn giao: <dán>. Cập nhật tài liệu bàn giao: đóng câu hỏi đã trả lời,
thêm câu hỏi mới (người + hạn), ghi quyết định mới vào Lịch sử thay đổi, tăng số phiên bản.
```

## 10. Lỗi thường gặp và checklist

### Lỗi thường gặp

| Lỗi | Hậu quả | Cách tránh |
| --- | --- | --- |
| Nhảy thẳng vào mockup đẹp | Tranh luận màu sắc khi chưa chốt làm gì | Brief → flow → wireframe trước |
| Prompt mở "làm app cho tôi" | Nhiều màn thừa, tốn token, khó sửa | Giới hạn số màn, số hướng, kích thước |
| Dữ liệu mẫu "Lorem ipsum", tên ngắn | Vỡ layout khi gặp tên Việt dài, số tiền lớn | Dữ liệu mẫu giống thật, có ca biên (5.4) |
| Chỉ làm trạng thái "có dữ liệu" | Dev tự đoán màn rỗng/lỗi, mỗi người một kiểu | 4 trạng thái cho mỗi màn |
| Hỏi user "có thích không" | Ai cũng nói thích, không học được gì | Giao nhiệm vụ, quan sát họ làm |
| Tin Claude khi nó "đóng vai user" | Phản hồi chung chung, sót vấn đề thật | Claude chuẩn bị + tổng hợp, user thật test |
| Bàn giao chỉ bằng link prototype | Dev hỏi lại từng quy tắc, ước lượng sai | Tài liệu bàn giao theo mẫu 9.2 |
| Claude tự điền chỗ trống trong spec | Dev code theo quy tắc không ai quyết | Bắt Claude đánh dấu [GIẢ ĐỊNH], đưa vào câu hỏi mở |
| Dán dữ liệu khách hàng thật vào prompt | Rủi ro quyền riêng tư | Dùng dữ liệu giả, bỏ tên/số điện thoại |

### Checklist trước khi bàn giao

- [ ] Brief và PRD đã duyệt, phạm vi MVP có MUST / WON'T rõ
- [ ] Mọi story MUST đã xét đủ 5 nhóm acceptance criteria
- [ ] User flow có nhánh lỗi và đường quay lại
- [ ] Prototype đủ 4 trạng thái cho mỗi màn, dùng dữ liệu mẫu giống thật
- [ ] Đã test ≥ 1 vòng 5 user, không còn vấn đề mức chặn
- [ ] Tài liệu bàn giao theo mẫu: mọi form có bảng field, mọi con số trên UI có công thức, không còn [GIẢ ĐỊNH] chưa xác nhận
- [ ] Đã qua bước "đóng vai dev senior" rà lại và là bản thứ hai (sau khi trả lời câu hỏi mở)
- [ ] Câu hỏi mở đều có người trả lời + hạn
- [ ] Design system / token và handoff bundle (hoặc link Figma) đã gửi

## Nguồn

- [Introducing Claude Design by Anthropic Labs](https://www.anthropic.com/news/claude-design-anthropic-labs)
- [Figma connector cho Claude](https://claude.com/connectors/figma) · [Figma MCP server — Figma Help](https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server)
- [Nielsen Norman Group — Why You Only Need to Test with 5 Users](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/)
- [Nielsen Norman Group — 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) · [Material Design 3](https://m3.material.io/)
