# Prompt: bàn giao và phát hành

Chi tiết: [Dùng Claude làm prototype cho Designer, BA, PM](../guides/claude-lam-prototype.md). Mẫu: [templates/ban-giao-dev.md](../templates/ban-giao-dev.md).

## Viết tài liệu bàn giao cho dev

Dùng sau khi prototype đã qua test user. Đính kèm (hoặc để sẵn trong Project) tài liệu và **toàn bộ ảnh chụp màn hình**: màn chính, các biến thể (tab, chế độ), các trạng thái (rỗng, có dữ liệu, lỗi, dropdown mở, dialog…). Đặt tên ảnh theo mã màn (`S-01-empty.png`) để dễ đối chiếu. Hơn ~15–20 ảnh thì chạy theo từng nhóm màn rồi gộp.

```
Bạn là Senior BA kiêm technical writer, viết tài liệu bàn giao cho dev (Frontend, Backend, QA).
Bối cảnh: sản phẩm <tên>, tính năng <tên>, điểm vào <menu > màn > nút>, nền tảng <web / mobile / cả hai>,
role dùng <...>. Thông tin thêm: <quy định nghiệp vụ, luật áp dụng, hệ thống liên quan>.
Đầu vào (đính kèm / có trong Project): PRD, user story, user flow, quy tắc nghiệp vụ, dữ liệu mẫu,
báo cáo test user vòng cuối, link prototype, ảnh chụp màn hình.

Bước 1: liệt kê từng ảnh → màn nào (S-01…), trạng thái / biến thể nào. Ảnh nào không khớp màn nào thì hỏi.
Bước 2: viết tài liệu theo mẫu templates/ban-giao-dev.md, đủ 14 mục; mục không áp dụng ghi "N/A — lý do".
Quy tắc:
- tiếng Việt, giữ nguyên tiếng Anh cho UI label, tên field, enum, tên component, API
- chỉ ghi điều có trong tài liệu hoặc thấy trên ảnh; chỗ phải suy luận đánh dấu [GIẢ ĐỊNH] và đưa vào Câu hỏi mở
- mỗi form có bảng field (kiểu, bắt buộc, mặc định, quy tắc hợp lệ, thông báo lỗi);
  mọi con số / tổng / badge trên UI có công thức; quy tắc phụ thuộc giữa các field ghi rõ
- quy tắc phải đo được, không viết kiểu "hệ thống xử lý phù hợp"
- dữ liệu và API ghi là ĐỀ XUẤT, không chọn công nghệ, không viết code
- quyết định thiết kế thay đổi sau test user thì ghi lý do 1 dòng ở Lịch sử thay đổi
- mã duy nhất toàn tính năng (S-01, US-01, BR-01, VR-01, Q-01), tham chiếu bằng mã thay vì chép lại
Tổ chức: ≤ 3 màn và dưới ~800 dòng thì 1 file docs/features/<ten>.md; lớn hơn thì tách thư mục như comment đầu mẫu.
Xuất: in cây file và số dòng ước tính trước, rồi từng file. Bị giới hạn độ dài thì dừng ở ranh giới giữa 2 file,
ghi "Còn lại: <danh sách>" và chờ mình nhắn "Tiếp tục". Nếu tạo được file / doc thì tạo trực tiếp.
```

## Cập nhật sau khi trả lời câu hỏi mở

Bản thứ hai luôn chính xác hơn bản đầu, nên đừng gửi dev bản đầu.

```
Đây là câu trả lời cho các câu hỏi mở: <Q-01: ..., Q-02: ...>.
Cập nhật tài liệu: sửa các mục liên quan, bỏ nhãn [GIẢ ĐỊNH] đã được xác nhận, đóng câu hỏi đã trả lời,
thêm câu hỏi mới nếu câu trả lời mở ra chỗ chưa rõ, ghi vào Lịch sử thay đổi, tăng số phiên bản.
Chỉ in các phần đã đổi.
```

## Rà tài liệu bàn giao trước khi gửi

```
Đóng vai dev senior nhận tài liệu này. Liệt kê mọi câu bạn sẽ hỏi trước khi ước lượng:
thiếu trạng thái màn hình, quy tắc không rõ, dữ liệu thiếu trường, mâu thuẫn prototype với story,
phân quyền chưa nói, trường hợp lỗi / mất mạng. Sắp theo mức cản trở ước lượng.
```

## Cập nhật sau buổi bàn giao

```
Đây là ghi chép buổi bàn giao: <dán>. Cập nhật tài liệu bàn giao: đóng câu hỏi đã trả lời,
thêm câu hỏi mới (người + hạn), ghi quyết định mới vào Lịch sử thay đổi, tăng số phiên bản.
```

## Dev nhận bàn giao

```
Đọc docs/features/<ten>.md và thiết kế (<handoff bundle / link Figma / ảnh>). Đọc CLAUDE.md và code hiện có.
Chưa viết code. Trả về:
1. Component / màn / API đã có trong repo dùng lại được (file:dòng)
2. Phần phải làm mới: màn, state, API, migration
3. Chỗ thiết kế lệch design system / component hiện có → hỏi lại hay theo code
4. Câu hỏi cho PM / BA / Designer (không trùng mục Câu hỏi mở)
5. Kế hoạch chia task, mỗi task ≤ 1 ngày, ước lượng S/M/L
```

## Release note

```
Từ git log <tag cũ>..HEAD và danh sách issue đã đóng, viết release note:
- bản cho người dùng (tiếng Việt, ≤ 5 gạch đầu dòng, nói lợi ích, không thuật ngữ) — dùng cho "Có gì mới" trên store
- bản cho team (thay đổi kỹ thuật, migration, cấu hình mới, rủi ro, cách rollback)
```

## Rà trước khi nộp App Store / Google Play

```
Đóng vai App Store reviewer và Google Play policy reviewer. Đọc source app ở <đường dẫn> (Flutter / React Native),
Info.plist, AndroidManifest, app.json / pubspec, các màn đăng nhập, tài khoản, AI, nội dung user tạo, thanh toán.
Rà theo: 2.1 hoàn thiện, 4.3 spam / danh mục bão hòa, 4.2 webview, 4.8 đăng nhập tương đương Sign in with Apple, 5.1.1(v) xóa tài khoản,
5.1.2 gửi dữ liệu cho AI bên thứ ba, 1.2 nội dung user tạo, 3.1.1 IAP, permission khai báo mà không dùng,
Google Play target API, Data safety, link web xóa tài khoản, demo account cho reviewer.
Bảng: mục | bằng chứng file:dòng | rủi ro (cao / trung / thấp) | cách sửa. Không sửa code, chỉ báo cáo.
```

## App Review Notes

```
Viết App Review Notes (tiếng Anh, ≤ 200 từ) cho app <tên>:
- tính năng chính và điểm khác biệt so với app cùng loại
- demo account + cách đăng nhập không cần OTP
- AI: dùng nhà cung cấp nào, dữ liệu gì được gửi, màn đồng ý ở đâu
- cách xóa tài khoản trong app
Dựa vào source, không bịa tính năng.
```

## Trả lời khi bị từ chối

```
App bị từ chối với nội dung: <dán thư của Apple / Google>.
Giải thích họ đang nói gì, guideline nào, cần sửa gì trong app (file:dòng nếu tìm được).
Soạn thư trả lời ngắn, lịch sự, tiếng Anh: đã sửa gì hoặc giải thích vì sao app không vi phạm.
```
