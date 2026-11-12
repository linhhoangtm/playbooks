# Prompt: bàn giao và phát hành

Chi tiết: [Dùng Claude làm prototype cho Designer, BA, PM](../guides/claude-lam-prototype.md). Mẫu: [templates/ban-giao-dev.md](../templates/ban-giao-dev.md).

## Viết tài liệu bàn giao cho dev

```
Tạo tài liệu bàn giao theo mẫu templates/ban-giao-dev.md, dùng: PRD, user story, user flow,
quy tắc nghiệp vụ, dữ liệu mẫu, báo cáo test user vòng cuối (đính kèm / có trong Project).
- chỉ ghi điều đã có trong tài liệu; chỗ thiếu đưa vào mục Câu hỏi mở, không tự điền
- mục API ghi là ĐỀ XUẤT, không chọn công nghệ, không viết code
- quyết định thiết kế thay đổi sau test user thì ghi lý do 1 dòng
- tối đa 4 trang, chi tiết dài để phụ lục
Tạo dưới dạng doc để cả team bình luận.
```

## Rà tài liệu bàn giao trước khi gửi

```
Đóng vai dev senior nhận tài liệu này. Liệt kê mọi câu bạn sẽ hỏi trước khi ước lượng:
thiếu trạng thái màn hình, quy tắc không rõ, dữ liệu thiếu trường, mâu thuẫn prototype với story,
phân quyền chưa nói, trường hợp lỗi / mất mạng. Sắp theo mức cản trở ước lượng.
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
