# Prompt: kiến trúc và công nghệ

Đọc kèm: [Chọn kiến trúc phần mềm phù hợp](../guides/chon-kien-truc-phan-mem.md), [Chọn công nghệ làm mobile app](../guides/chon-cong-nghe-mobile-app.md).

## Phỏng vấn để thu thập yêu cầu

```
Bạn là software architect. Tôi sắp chọn kiến trúc cho dự án: <mô tả ngắn>.
Phỏng vấn tôi theo 5 nhóm: NFRs, nghiệp vụ, đội ngũ, ngân sách và thời gian, hạ tầng sẵn có.
Mỗi lần hỏi 3–4 câu, đợi tôi trả lời. Câu nào tôi không biết thì ghi lại là giả định.
Cuối cùng tóm tắt thành bảng yêu cầu, có con số cụ thể.
```

## Chọn kiến trúc

```
Dự án: <mô tả>. Bối cảnh:
- quy mô user dự kiến năm đầu: <số>, đỉnh tải: <số request/giây hoặc mô tả>
- team: <số người, quen ngôn ngữ gì>, ngân sách hạ tầng: <số/tháng>
- dữ liệu: <loại, dung lượng, yêu cầu realtime / offline / báo cáo>
- ràng buộc: <deadline, tuân thủ, tích hợp hệ thống có sẵn>
Đề xuất 2–3 phương án kiến trúc. Mỗi phương án: sơ đồ (Mermaid), ưu, nhược, chi phí vận hành, khi nào phải đổi.
Chọn 1 và nói vì sao. Mặc định ưu tiên đơn giản (monolith tách module) trừ khi có lý do rõ.
```

## Phản biện kiến trúc đã chọn

```
Đây là kiến trúc tôi định dùng: <dán ADR hoặc mô tả>.
Hãy đóng vai architect khó tính. Tìm: điểm lỗi đơn (single point of failure), chỗ quá phức tạp so với nhu cầu,
chỗ chưa đáp ứng NFR, rủi ro về dữ liệu và bảo mật. Xếp theo mức nghiêm trọng, kèm cách khắc phục.
```

## Có nên tách service không

```
Hệ thống hiện tại: <mô tả modular monolith, số liệu tải, team>.
Tôi đang cân nhắc tách module <tên> thành service riêng vì <lý do>.
Phân tích: lợi ích thật, chi phí vận hành thêm, ảnh hưởng tới tính nhất quán dữ liệu,
và phương án thay thế không cần tách (cache, worker, tối ưu query). Kết luận rõ nên hay chưa.
```

## Chọn công nghệ

```
So sánh <A> và <B> (và <C>) cho dự án trên. Tiêu chí: team đã quen chưa, hệ sinh thái thư viện,
hiệu năng cho trường hợp <x>, chi phí, khả năng tuyển người, mức Claude / AI hỗ trợ tốt.
Tra tài liệu chính thức để lấy tình trạng mới nhất (phiên bản, hỗ trợ). Ghi nguồn.
Kết luận theo dạng: "chọn <A> nếu…, chọn <B> nếu…".
```

## Kiểm tra một tính năng khó trước khi cam kết công nghệ

```
Tôi định làm app bằng <Flutter>. App cần <kết nối máy in nhiệt qua Bluetooth / widget màn hình chính / chạy nền định vị>.
Tìm các thư viện đang được duy trì cho tính năng này, ngày release gần nhất, issue mở lớn nhất.
Nếu phải tự viết code native, ước lượng công sức cho iOS và Android. Ghi nguồn cho mọi thông tin.
```

## Thiết kế database

```
Từ user story và quy tắc nghiệp vụ (đính kèm), thiết kế schema <PostgreSQL / MySQL / SQL Server>:
bảng, cột, kiểu, khóa chính / ngoại, unique, index cần cho các truy vấn chính, soft delete hay không.
Vẽ ERD bằng Mermaid. Liệt kê 5 truy vấn hay dùng nhất và index phục vụ chúng.
Chỉ ra chỗ có thể N+1 hoặc phình to theo thời gian.
```

## Thiết kế API

```
Thiết kế REST API cho <tính năng>: method, path, request, response (JSON mẫu), mã lỗi, ai được gọi.
Quy ước: <snake_case / camelCase>, phân trang <cursor / offset>, lỗi theo format <...>.
Mỗi endpoint ghi rõ kiểm quyền gì (đăng nhập, sở hữu dữ liệu, role). Xuất OpenAPI 3.1 YAML.
```

## Viết ADR

```
Ghi lại quyết định kiến trúc theo mẫu templates/ADR.md:
quyết định: <...>, các phương án đã cân nhắc: <...>, lý do chọn: <...>.
Ngắn, ≤ 1 trang. Nêu rõ hệ quả xấu chấp nhận được và điều kiện để xem xét lại.
```
