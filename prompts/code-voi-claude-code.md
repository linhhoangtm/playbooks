# Prompt: code với Claude Code

Đặt `CLAUDE.md` ở gốc repo trước (mẫu: [templates/CLAUDE.md](../templates/CLAUDE.md)) để không phải lặp lại quy ước trong mỗi prompt.

## Hiểu codebase

```
Đọc repo này và tóm tắt: cấu trúc thư mục, luồng chạy chính từ <entry point>, cách quản lý state / DI,
cách gọi API, cách test. Chỉ ra 5 chỗ khó hiểu hoặc rủi ro nhất. Chưa sửa gì.
```

## Lên kế hoạch trước khi code

```
Tính năng: <mô tả hoặc link docs/features/<ten>.md>.
Chưa viết code. Trả về:
1. File / component / API có sẵn dùng lại được (file:dòng)
2. Phần phải làm mới: màn, state, API, migration
3. Rủi ro và chỗ cần hỏi lại
4. Kế hoạch chia bước, mỗi bước chạy được và test được độc lập
Chờ mình duyệt.
```

## Code từng bước

```
Làm bước <n> trong kế hoạch. Theo quy ước trong CLAUDE.md.
Xong thì chạy <lệnh lint> và <lệnh test liên quan>, báo kết quả và danh sách file đã đổi.
Không commit. Không thêm dependency khi chưa hỏi.
```

## Debug

```
Lỗi: <mô tả, log / stack trace>. Tái hiện: <các bước>. Mong đợi: <...>. Thực tế: <...>.
Tìm nguyên nhân gốc trước, giải thích bằng file:dòng. Đề xuất cách sửa nhỏ nhất.
Viết 1 test tái hiện lỗi (fail trước khi sửa, pass sau khi sửa). Không sửa chỗ không liên quan.
```

## Refactor

```
Refactor <file / module> để <mục tiêu: tách nhỏ, bỏ trùng lặp, dễ test>.
Không đổi hành vi. Chạy test trước và sau, kết quả phải giống nhau.
Nếu chưa có test cho phần này, viết test bao hành vi hiện tại trước khi refactor.
```

## Review code

```
Review thay đổi trên nhánh hiện tại so với <main> (git diff). Tìm theo thứ tự ưu tiên:
lỗi logic, thiếu kiểm quyền, lỗ hổng bảo mật, lỗi xử lý null / lỗi mạng, rò rỉ bộ nhớ, N+1, thiếu test, đặt tên.
Mỗi mục: file:dòng | mức (phải sửa / nên sửa / tùy) | vì sao | cách sửa. Không liệt kê chuyện format.
```

## Viết commit message / PR

```
Viết commit message cho thay đổi hiện tại: dòng đầu ≤ 72 ký tự, nói làm gì và vì sao.
Rồi viết mô tả PR: bối cảnh, thay đổi chính, cách test, ảnh chụp (nếu UI), rủi ro.
```

## Cập nhật CLAUDE.md sau khi sửa sai

```
Bạn vừa làm sai <mô tả>. Thêm 1 dòng quy tắc ngắn vào CLAUDE.md để lần sau không lặp lại.
Chỉ thêm quy tắc, không viết lại file.
```
