# Hướng dẫn AI làm việc như trợ lý — kèm prompt mẫu

Cập nhật: 2026-11-12

Cách giao việc để AI (Claude, ChatGPT, Gemini…) làm đúng ý bạn, không cần biết lập trình. Mọi prompt mẫu đều copy dùng được ngay, bạn chỉ cần thay phần trong `<ngoặc nhọn>`.

## Mục lục

- [1. AI giống một trợ lý mới](#1-ai-giống-một-trợ-lý-mới)
- [2. Công thức một prompt tốt](#2-công-thức-một-prompt-tốt)
- [3. Dặn một lần, dùng mãi](#3-dặn-một-lần-dùng-mãi)
- [4. Viết và giao tiếp](#4-prompt-mẫu-viết-và-giao-tiếp)
- [5. Tóm tắt, họp, đọc tài liệu](#5-prompt-mẫu-tóm-tắt-họp-đọc-tài-liệu)
- [6. Marketing và bán hàng](#6-prompt-mẫu-marketing-và-bán-hàng)
- [7. Phân tích, quyết định, phản biện](#7-prompt-mẫu-phân-tích-quyết-định-phản-biện)
- [8. Học tập và luyện tập](#8-prompt-mẫu-học-tập-và-luyện-tập)
- [9. Công việc văn phòng](#9-prompt-mẫu-công-việc-văn-phòng)
- [10. Theo vị trí công việc](#10-prompt-mẫu-theo-vị-trí-công-việc)
- [11. Góp ý để AI sửa, và những điều cần nhớ](#11-góp-ý-để-ai-sửa-và-những-điều-cần-nhớ)

## 1. AI giống một trợ lý mới

AI rất giỏi và rất nhanh, nhưng chưa biết gì về bạn. Bạn hướng dẫn càng rõ, AI làm càng đúng ý.

| Điều cần biết | Ý nghĩa với bạn |
| --- | --- |
| AI đã “đọc” lượng văn bản khổng lồ (LLM) | Viết, tóm tắt, dịch, giải thích rất tốt |
| AI không biết bối cảnh của bạn | Phải kể cho nó về công ty, khách hàng, cách làm việc của bạn |
| AI có thể “bịa” (hallucination) | Nó có thể trả lời rất tự tin nhưng sai. Luôn kiểm tra số liệu, tên, ngày tháng |

Tài liệu này nói về **prompting**, tức là cách giao việc cho AI. Nó khác với **train AI**: train là thay đổi chính model, việc của các công ty AI với chi phí rất lớn. Prompting thì ai biết gõ chữ cũng làm được ngay. Ví von: train AI giống cho nhân viên đi học đại học, còn prompting giống đưa nhân viên tờ hướng dẫn công việc.

## 2. Công thức một prompt tốt

**Role + Context + Task + Format + Example**, sau đó dùng **Feedback** để sửa.

| Bước | Nói cho AI biết | Ví dụ |
| --- | --- | --- |
| 1. Role | Nó đóng vai ai | “Bạn là trợ lý chăm sóc khách hàng…” |
| 2. Context | Bạn là ai, làm cho ai, mục tiêu, giới hạn | “…của một tiệm bánh nhỏ ở TP.HCM, khách đặt qua Zalo” |
| 3. Task | Việc cụ thể, kết quả cần có | “Viết tin nhắn xin lỗi vì giao trễ 30 phút, tặng mã giảm 10%” |
| 4. Format | Độ dài, định dạng, ai sẽ đọc | “Dưới 100 chữ, giọng thân thiện” |
| 5. Example | 1–3 mẫu để AI bắt chước (few-shot) | “Đây là 2 tin nhắn mình hay gửi: …” |

**Mẫu trống: copy và điền vào**

```text
Bạn là <vai trò>.
Bối cảnh: <tôi là ai, làm cho ai, mục tiêu, giới hạn>.
Nhiệm vụ: <việc cần làm, kết quả mong muốn>.
Định dạng: <độ dài, gạch đầu dòng / bảng / đoạn văn, giọng văn, người đọc>.
Mẫu tham khảo: <dán 1–3 ví dụ, nếu có>.
Nếu thiếu thông tin, hãy hỏi tôi trước khi làm.
```

**Giao việc mơ hồ và giao việc rõ ràng**

| Mơ hồ | Rõ ràng |
| --- | --- |
| “Viết email cho khách.” | “Viết email xin lỗi khách vì giao bánh trễ 30 phút, tặng mã giảm 10%, dưới 100 chữ.” |
| “Tóm tắt tài liệu này.” | “Tóm tắt tài liệu thành 5 gạch đầu dòng để sếp đọc trong 1 phút.” |
| “Làm bài đăng Facebook.” | “Viết 3 phiên bản bài đăng Facebook giới thiệu bánh mới, mỗi bài kết thúc bằng 1 câu mời đặt hàng.” |

**Mẹo:** câu cuối “nếu thiếu thông tin, hãy hỏi tôi trước” giúp AI không tự đoán bừa. Đây là câu nên thêm vào hầu hết prompt.

## 3. Dặn một lần, dùng mãi

Những điều lặp lại (bạn là ai, muốn AI trả lời thế nào) thì nên dặn một lần trong phần cài đặt, không phải gõ lại ở mỗi cuộc chat.

| Bạn muốn | ChatGPT | Claude |
| --- | --- | --- |
| Dặn chung cho mọi cuộc chat | Settings → Personalization → Custom instructions | Settings → Profile → Preferences |
| AI tự ghi nhớ về bạn | Settings → Personalization → Memory | Settings → Capabilities → Memory |
| Phòng làm việc riêng, kèm tài liệu | Projects ở thanh bên trái | Projects ở thanh bên trái |
| Đóng gói quy trình hay lặp lại | Custom GPTs, Skills | Skills |

Tên menu có thể thay đổi theo phiên bản ứng dụng.

**Mẫu: dặn chung (Custom instructions / Preferences)**

```text
Về tôi: Tôi là <nghề nghiệp> tại <công ty / lĩnh vực>, ở <thành phố>.
Công việc thường nhờ AI: <viết email, tóm tắt tài liệu, lên ý tưởng nội dung…>.

Cách trả lời tôi muốn:
- Trả lời bằng tiếng Việt, ngắn gọn, đi thẳng vào ý chính.
- Dùng gạch đầu dòng khi có nhiều ý.
- Nếu không chắc chắn, hãy nói rõ là không chắc, đừng đoán.
- Thiếu thông tin thì hỏi lại tôi trước khi làm.
```

**Mẫu: hướng dẫn cho một Project (ví dụ tiệm bánh)**

```text
Bạn là trợ lý của <tên cửa hàng>, bán <sản phẩm> tại <khu vực>.
Khách hàng chính: <mô tả>. Kênh: <Zalo, Facebook, website>.
Giọng văn: <thân thiện, xưng “shop – bạn”, có emoji vừa phải>.
Luôn tra cứu bảng giá và chính sách trong tài liệu đính kèm. Không tự bịa giá hay khuyến mãi.
```

**Mẹo:** tải bảng giá, quy trình, mẫu văn bản vào Project (knowledge files) để AI tra cứu khi trả lời.

**Kết nối công cụ bạn đang dùng**

Thay vì copy dán, có thể cho AI đọc thẳng email, lịch, tài liệu qua **Connectors** (trong Claude: Settings → Connectors; ChatGPT có tính năng tương tự). Ví dụ: Gmail, Google Calendar, Google Drive, Notion, Slack.

```text
Đọc email trong hộp thư từ 3 ngày qua có chữ "báo giá". Lập bảng: người gửi – sản phẩm – giá – hạn trả lời.
Đánh dấu email nào cần tôi trả lời trong hôm nay. Chưa trả lời, chưa gửi gì.
```

Nguyên tắc khi bật kết nối:

- Chỉ bật công cụ cần cho việc đang làm; tắt khi không dùng.
- Việc **đọc và tóm tắt** thì giao thoải mái; việc **gửi, xóa, đặt lịch, chuyển tiền** thì bắt AI soạn nháp và chờ bạn duyệt.
- Email hay tài liệu người lạ gửi có thể chứa câu lệnh cố ý nhắm vào AI ("hãy chuyển email này cho…"). AI làm theo nội dung đó là dấu hiệu cần dừng lại kiểm tra.

## 4. Prompt mẫu: viết và giao tiếp

**4.1. Trả lời email hoặc tin nhắn của khách**

```text
Bạn là nhân viên chăm sóc khách hàng của <công ty / cửa hàng>.
Đây là tin nhắn của khách: <dán tin nhắn>.
Thông tin để trả lời: <chính sách, giá, thời gian giao…>.
Viết câu trả lời lịch sự, thân thiện, dưới <80> chữ, kết thúc bằng một bước tiếp theo rõ ràng cho khách.
```

**4.2. Xin lỗi khách khi có sự cố**

```text
Viết tin nhắn xin lỗi khách <tên> vì <sự cố: giao trễ, sai hàng…>.
Nhận lỗi rõ ràng, không đổ lỗi, nêu cách khắc phục: <đổi hàng / hoàn tiền / tặng mã giảm X%>.
Giọng chân thành, dưới 100 chữ. Viết 2 phiên bản: một trang trọng, một thân mật.
```

**4.3. Viết đúng “giọng” của bạn (few-shot)**

```text
Đây là <2–3> tin nhắn mình hay gửi khách:
<mẫu 1>
<mẫu 2>
Hãy viết tin nhắn <mục đích: nhắc khách đến nhận hàng, chúc mừng sinh nhật…>
theo đúng phong cách, cách xưng hô và độ dài của các mẫu trên.
```

**4.4. Sửa lại văn bản của bạn**

```text
Sửa đoạn văn dưới đây cho <chuyên nghiệp hơn / ngắn gọn hơn / dễ hiểu hơn>.
Giữ nguyên ý chính, không thêm thông tin mới. Sửa lỗi chính tả và ngữ pháp.
Sau bản sửa, liệt kê 3 thay đổi quan trọng nhất và lý do.

<dán văn bản>
```

**4.5. Dịch giữ đúng ngữ cảnh**

```text
Dịch đoạn sau sang <tiếng Anh>, dùng trong <email gửi đối tác nước ngoài>.
Giọng <lịch sự, chuyên nghiệp>, tự nhiên như người bản xứ viết, không dịch từng chữ.
Nếu có cụm từ khó dịch, ghi chú cách bạn xử lý ở cuối.

<dán văn bản>
```

**4.6. Email khó nói (từ chối, đòi nợ, phản hồi tiêu cực)**

```text
Tôi cần <từ chối đề nghị / nhắc thanh toán quá hạn / góp ý cho đồng nghiệp> về <chuyện gì>.
Quan hệ với người nhận: <khách lâu năm / sếp / đồng nghiệp>. Tôi muốn giữ quan hệ tốt.
Viết 2 cách: một mềm mỏng, một thẳng thắn. Mỗi cách dưới 120 chữ.
```

## 5. Prompt mẫu: tóm tắt, họp, đọc tài liệu

Đính kèm file (bấm nút “+”) hoặc dán nội dung vào, rồi dùng các prompt dưới đây.

**5.1. Tóm tắt cho sếp đọc nhanh**

```text
Tóm tắt tài liệu đính kèm thành 5 gạch đầu dòng để <sếp / khách> đọc trong 1 phút.
Dòng đầu tiên là kết luận quan trọng nhất. Giữ nguyên các con số và ngày tháng.
Cuối cùng: 1 câu “cần quyết định gì” nếu có.
```

**5.2. Biên bản họp từ ghi chú hoặc bản ghi âm**

```text
Đây là ghi chú / transcript cuộc họp <tên cuộc họp> ngày <ngày>: <dán vào>.
Viết biên bản gồm: mục tiêu, các quyết định, vấn đề còn mở,
bảng việc cần làm (việc – người phụ trách – hạn chót).
Chỗ nào không rõ ai phụ trách thì ghi “chưa rõ”, không tự đặt tên.
```

**5.3. Hỏi đáp trên tài liệu dài**

```text
Chỉ dựa vào tài liệu đính kèm, trả lời: <câu hỏi>.
Trích dẫn trang hoặc đoạn liên quan. Nếu tài liệu không có thông tin này, nói rõ là không có.
```

**5.4. So sánh hai tài liệu (hợp đồng, báo giá, phiên bản)**

```text
So sánh 2 file đính kèm: <file A> và <file B>.
Lập bảng các điểm khác nhau: mục – file A – file B – ảnh hưởng đến tôi.
Đánh dấu điểm nào bất lợi cho <bên tôi>.
```

**5.5. Biến tài liệu thành checklist hành động**

```text
Đọc <quy định / hướng dẫn> đính kèm và biến nó thành checklist từng bước cho <ai> thực hiện.
Mỗi bước 1 dòng, bắt đầu bằng động từ. Đánh dấu bước nào bắt buộc, bước nào tùy chọn.
```

**Lưu ý:** không tải lên tài liệu chứa mật khẩu, số tài khoản hay dữ liệu nhạy cảm của khách hàng.

## 6. Prompt mẫu: marketing và bán hàng

**6.1. Bài đăng mạng xã hội**

```text
Bạn là copywriter cho <thương hiệu>, bán <sản phẩm> cho <khách hàng mục tiêu>.
Viết 3 phiên bản bài đăng <Facebook / TikTok / Instagram> giới thiệu <sản phẩm / khuyến mãi>.
Mỗi bài: câu mở đầu gây chú ý, dưới <100> chữ, kết thúc bằng 1 câu kêu gọi hành động.
3 bài theo 3 góc khác nhau: cảm xúc, lợi ích, khan hiếm. Gợi ý 3–5 hashtag.
```

**6.2. Lịch nội dung 1 tháng**

```text
Lập lịch nội dung <tháng> cho fanpage <tên>, đăng <3> bài/tuần.
Mục tiêu: <tăng tương tác / ra mắt sản phẩm / bán hàng>. Có các dịp: <lễ, sự kiện>.
Trình bày dạng bảng: ngày – chủ đề – dạng bài (ảnh, video, carousel) – ý chính – mục tiêu.
```

**6.3. Mô tả sản phẩm**

```text
Viết mô tả sản phẩm cho <Shopee / website> từ thông tin sau: <tên, chất liệu, kích thước, giá, điểm khác biệt>.
Gồm: tiêu đề có từ khóa, 5 gạch đầu dòng lợi ích (không chỉ tính năng), 1 đoạn ngắn cho ai nên mua.
Không phóng đại, không dùng từ “tốt nhất”, “số 1”.
```

**6.4. Xử lý từ chối của khách**

```text
Tôi bán <sản phẩm / dịch vụ>, giá <X>. Khách thường từ chối với các lý do:
<“giá cao quá”, “để suy nghĩ thêm”, “bên kia rẻ hơn”>.
Với mỗi lý do, viết 2 cách đáp lại ngắn, tự nhiên, không ép khách,
kèm 1 câu hỏi để hiểu nhu cầu thật của khách.
```

**6.5. Email chào hàng lần đầu**

```text
Viết email chào hàng gửi <chức danh> tại <loại công ty>. Sản phẩm của tôi: <mô tả 1 câu>.
Vấn đề họ thường gặp: <vấn đề>. Tối đa 120 chữ, tiêu đề dưới 8 chữ.
Không mở đầu bằng “Tôi là…”. Kết thúc bằng 1 lời mời dễ nhận lời (ví dụ gọi 15 phút).
```

**6.6. Chân dung khách hàng**

```text
Sản phẩm của tôi: <mô tả>, giá <X>, bán tại <khu vực / kênh>.
Vẽ 3 chân dung khách hàng tiềm năng: tuổi, công việc, nỗi lo, lý do mua, nơi họ tìm thông tin,
và 1 thông điệp nên nói với từng người.
```

## 7. Prompt mẫu: phân tích, quyết định, phản biện

Ở nhóm này AI đóng vai cố vấn (Advisor) hoặc người phản biện (Critic). Hãy yêu cầu nó nói thẳng, vì mặc định AI hay trả lời theo hướng dễ nghe.

**7.1. So sánh các phương án**

```text
Tôi đang phải chọn giữa: <phương án A>, <phương án B>, <phương án C>.
Bối cảnh: <ngân sách, thời gian, ưu tiên của tôi>.
Lập bảng so sánh theo: chi phí, rủi ro, thời gian, lợi ích dài hạn.
Sau đó nói phương án bạn chọn và điều kiện nào sẽ khiến bạn đổi ý.
```

**7.2. Phản biện kế hoạch hoặc ý tưởng**

```text
Đây là kế hoạch của tôi: <dán vào>.
Hãy đóng vai người phản biện khó tính. Không khen.
Chỉ ra 5 điểm yếu hoặc giả định rủi ro nhất, xếp theo mức nghiêm trọng,
và với mỗi điểm, đề xuất cách kiểm tra hoặc khắc phục.
```

**7.3. Phân tích số liệu từ file Excel**

```text
Đính kèm là file <doanh thu / chi phí> từ <tháng> đến <tháng>.
Cho tôi biết: 3 xu hướng chính, điểm bất thường, sản phẩm / kênh nào đóng góp nhiều nhất.
Vẽ biểu đồ nếu giúp dễ hiểu. Nêu rõ cách bạn tính để tôi kiểm tra lại.
```

**7.4. Phân tích SWOT nhanh**

```text
Phân tích SWOT cho <doanh nghiệp / dự án / sản phẩm> với thông tin: <mô tả, đối thủ, thị trường>.
Mỗi ô tối đa 4 ý, cụ thể, không chung chung.
Cuối cùng: 3 hành động ưu tiên trong 3 tháng tới.
```

**7.5. Brainstorm ý tưởng**

```text
Cho tôi 20 ý tưởng để <mục tiêu: tăng khách quay lại, giảm chi phí, tên sản phẩm…>.
Ràng buộc: <ngân sách, nhân lực>. Gồm cả ý tưởng an toàn lẫn táo bạo.
Sau đó chọn ra 3 ý tưởng tốt nhất theo tiêu chí dễ làm và hiệu quả, giải thích vì sao.
```

**7.6. Nghiên cứu có nguồn**

```text
Tìm hiểu về <chủ đề / thị trường / đối thủ> tại <Việt Nam>, thông tin trong <12 tháng> gần đây.
Mỗi con số hoặc nhận định phải kèm link nguồn. Chỗ nào các nguồn mâu thuẫn thì nêu ra.
Tóm tắt thành 1 trang.
```

Với 7.6, hãy bật tính năng tìm kiếm web hoặc Research / Deep Research để AI tìm thông tin mới. Sau đó vẫn nên mở một vài link để kiểm tra.

## 8. Prompt mẫu: học tập và luyện tập

**8.1. Gia sư giải thích từ dễ đến khó (Tutor)**

```text
Giải thích <khái niệm> cho người mới, không có nền tảng về <lĩnh vực>.
Dùng 1 ví dụ đời thường, rồi đi dần từ dễ đến khó qua 3 mức.
Sau mỗi mức, hỏi tôi 1 câu để kiểm tra tôi đã hiểu chưa, đợi tôi trả lời rồi mới đi tiếp.
```

**8.2. Tạo bài kiểm tra từ tài liệu**

```text
Từ tài liệu đính kèm, tạo 10 câu hỏi trắc nghiệm (4 đáp án) từ dễ đến khó.
Hỏi từng câu một, chờ tôi trả lời, giải thích đúng sai, cuối cùng cho điểm
và chỉ ra phần tôi cần ôn lại.
```

**8.3. Luyện phỏng vấn (Role-play)**

```text
Bạn là nhà tuyển dụng cho vị trí <vị trí> tại <loại công ty>. Đây là CV của tôi: <dán / đính kèm>.
Phỏng vấn tôi, mỗi lần 1 câu, đợi tôi trả lời.
Sau 6 câu, nhận xét: điểm mạnh, điểm cần cải thiện, và câu trả lời mẫu tốt hơn cho câu tôi trả lời yếu nhất.
```

**8.4. Luyện tình huống khó với khách**

```text
Bạn đóng vai khách hàng khó tính, đang <phàn nàn về … / mặc cả …>.
Tôi là <nhân viên bán hàng / CSKH>. Hãy phản ứng như khách thật, không dễ dãi.
Khi tôi gõ “DỪNG”, hãy chấm điểm cách tôi xử lý và gợi ý cách làm tốt hơn.
```

**8.5. Học tiếng Anh qua công việc**

```text
Tôi là <nghề>, trình độ tiếng Anh <cơ bản / trung bình>.
Mỗi ngày cho tôi 5 cụm từ hay dùng trong <email / họp / thuyết trình> của ngành tôi,
kèm nghĩa tiếng Việt, 1 câu ví dụ, rồi yêu cầu tôi đặt câu và sửa cho tôi.
```

**8.6. Lộ trình tự học**

```text
Tôi muốn học <kỹ năng> để <mục tiêu> trong <8 tuần>, mỗi ngày <1 giờ>.
Hiện tại tôi đã biết: <…>. Lập lộ trình theo tuần: mục tiêu, nội dung, bài tập thực hành,
cách tự kiểm tra cuối tuần. Ưu tiên tài liệu miễn phí.
```

## 9. Prompt mẫu: công việc văn phòng

**9.1. Lên kế hoạch tuần**

```text
Đây là việc của tôi tuần này: <liệt kê, kèm hạn chót nếu có>. Tôi làm <Thứ 2 – Thứ 7>, <8> giờ/ngày.
Xếp thành kế hoạch theo ngày, ưu tiên việc gấp và quan trọng, để lại 20% thời gian dự phòng.
Chỉ ra việc nào nên dời hoặc nhờ người khác nếu không đủ thời gian.
```

**9.2. Công thức Excel / Google Sheets**

```text
Bảng của tôi có các cột: <A: Ngày, B: Tên khách, C: Số tiền, …>, dữ liệu từ dòng 2 đến <500>.
Tôi muốn: <tính tổng tiền theo từng khách trong tháng 10 / đánh dấu đơn quá hạn…>.
Cho tôi công thức <Excel / Google Sheets>, giải thích từng phần, và cách kiểm tra nó chạy đúng.
```

**9.3. Soạn quy trình làm việc (SOP)**

```text
Viết quy trình <tên quy trình, ví dụ: xử lý đơn đổi trả> cho nhân viên mới.
Cách tôi đang làm: <mô tả bằng lời, lộn xộn cũng được>.
Trình bày: mục đích, ai làm, các bước đánh số, tình huống ngoại lệ và cách xử lý.
```

**9.4. Mô tả công việc (JD) và tin tuyển dụng**

```text
Viết tin tuyển <vị trí> cho <công ty, quy mô, lĩnh vực> tại <địa điểm>.
Công việc chính: <…>. Yêu cầu bắt buộc: <…>. Quyền lợi: <…>.
Giọng văn <trẻ trung / chuyên nghiệp>. Tách rõ yêu cầu bắt buộc và điểm cộng.
```

**9.5. Dàn ý slide thuyết trình**

```text
Tôi cần thuyết trình <chủ đề> cho <người nghe> trong <15> phút. Mục tiêu: <thuyết phục / báo cáo / đào tạo>.
Lập dàn ý <10> slide: tiêu đề mỗi slide là 1 câu kết luận, 3 ý chính, gợi ý hình ảnh hoặc biểu đồ.
Kèm lời nói ngắn cho slide mở đầu và slide kết.
```

**9.6. Báo cáo công việc tuần / tháng**

```text
Từ ghi chú sau: <dán việc đã làm, số liệu, vấn đề gặp phải>,
viết báo cáo gửi <sếp>: kết quả nổi bật, số liệu chính, vướng mắc và cần hỗ trợ gì, kế hoạch tuần tới.
Tối đa 200 chữ, không phóng đại.
```

## 10. Prompt mẫu theo vị trí công việc

| Vị trí | AI thường đóng vai | Nên “dạy” AI biết |
| --- | --- | --- |
| IT Developer | Pair programmer, người review code | Tech stack, coding convention, cấu trúc project |
| IT Helpdesk | Người tra cứu lỗi, người soạn hướng dẫn | Lỗi thường gặp, quy trình xử lý, giọng văn trả lời |
| Sale | Người soạn email, bạn tập đàm phán | Sản phẩm, bảng giá, chân dung khách, lời từ chối hay gặp |
| Marketing | Copywriter, bạn cùng brainstorm | Brand voice, khách hàng mục tiêu, kênh đăng bài |
| CEO | Cố vấn, người phản biện, người tóm tắt | Mục tiêu công ty, số liệu chính, quyết định đang cân nhắc |

**10.1. IT Developer: review code**

```text
Bạn là senior developer review code <ngôn ngữ / framework>.
Convention của team: <…>. Đây là đoạn code: <dán vào>.
Tìm bug, lỗi bảo mật, vấn đề hiệu năng, chỗ khó đọc. Xếp theo mức nghiêm trọng,
mỗi vấn đề kèm dòng code và cách sửa. Không viết lại toàn bộ.
```

**10.2. IT Developer: đọc lỗi**

```text
Tôi gặp lỗi này khi <làm gì>: <dán thông báo lỗi / log>.
Môi trường: <hệ điều hành, phiên bản, framework>. Tôi đã thử: <…>.
Giải thích nguyên nhân có thể có, xếp theo khả năng, và cách kiểm tra từng nguyên nhân.
```

**10.3. IT Helpdesk: hướng dẫn người dùng**

```text
Viết hướng dẫn cho nhân viên không rành máy tính cách <cài VPN / đổi mật khẩu email / kết nối máy in>
trên <Windows 11 / macOS>. Từng bước đánh số, câu ngắn, không dùng thuật ngữ.
Thêm mục “nếu gặp lỗi” với 3 lỗi hay gặp nhất.
```

**10.4. Sale: chuẩn bị cuộc gọi với khách**

```text
Tôi sắp gọi cho <chức danh> tại <công ty, ngành>. Sản phẩm của tôi: <mô tả>.
Chuẩn bị cho tôi: 5 câu hỏi khám phá nhu cầu, 3 lợi ích phù hợp nhất với ngành này,
3 phản đối có thể gặp và cách trả lời, câu chốt để hẹn bước tiếp theo.
```

**10.5. Marketing: ý tưởng chiến dịch**

```text
Brand voice: <mô tả>. Khách hàng mục tiêu: <…>. Ngân sách: <…>. Kênh: <…>.
Đề xuất 3 ý tưởng chiến dịch cho <dịp / mục tiêu>. Mỗi ý tưởng: thông điệp chính,
cách triển khai trên từng kênh, chỉ số đo, rủi ro.
```

**10.6. CEO: chuẩn bị một quyết định**

```text
Tôi đang cân nhắc <quyết định, ví dụ mở chi nhánh mới / tuyển thêm 5 người>.
Số liệu hiện tại: <doanh thu, chi phí, dòng tiền…>. Mục tiêu năm: <…>.
Hãy đóng vai cố vấn độc lập: nêu các câu hỏi tôi nên trả lời trước khi quyết,
kịch bản tốt / xấu / trung bình, và dấu hiệu cần theo dõi sau khi quyết.
```

## 11. Góp ý để AI sửa, và những điều cần nhớ

Lần đầu chưa đúng là bình thường. Đừng gõ lại từ đầu, hãy nhận xét cụ thể như với nhân viên. Vòng hỏi, sửa, hỏi lại này gọi là **iteration**.

**Câu góp ý hay dùng**

| Muốn | Gõ |
| --- | --- |
| Ngắn hơn | “Ngắn lại một nửa, giữ ý chính.” |
| Đổi giọng | “Bớt trang trọng, thêm emoji vừa phải.” / “Chuyên nghiệp hơn, bỏ từ lóng.” |
| Sửa một phần | “Giữ đoạn 2, viết lại phần mở đầu.” |
| Thêm lựa chọn | “Cho tôi thêm 3 phiên bản khác hẳn nhau.” |
| Đổi định dạng | “Chuyển thành bảng.” / “Chuyển thành gạch đầu dòng.” |
| Kiểm tra độ tin cậy | “Thông tin nào ở trên bạn không chắc chắn? Nguồn ở đâu?” |
| Tự rà soát | “Đọc lại câu trả lời như một người khó tính và sửa các chỗ yếu.” |
| Hiểu cách làm | “Giải thích vì sao bạn viết như vậy.” |

**Nên**

- Kiểm tra lại số liệu, tên người, ngày tháng.
- Coi kết quả của AI là bản nháp đầu tiên.
- Chia việc lớn thành nhiều bước nhỏ, mỗi bước một prompt.
- Lưu lại những prompt dùng tốt để dùng lại.

**Không nên**

- Đưa mật khẩu, số tài khoản, dữ liệu nhạy cảm của khách hàng.
- Tin tuyệt đối khi AI trả lời quá tự tin.
- Để AI ra quyết định quan trọng mà không xem lại.

**Công thức cần nhớ**

```text
Bạn là <vai trò>. Bối cảnh: <tình huống>. Hãy <nhiệm vụ>, trình bày dạng <định dạng>, theo mẫu sau: <ví dụ>.
```

Hướng dẫn rõ ràng thì kết quả tốt, giống như với một trợ lý giỏi.
