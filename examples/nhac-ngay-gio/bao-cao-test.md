# Kiểm thử app gia phả — 02/12/2026 14:30 — nhanh

Nhánh: `feature/nhac-ngay-gio` · Commit: `a1b2c3d` · Phạm vi: 1 tính năng, 14 file
Kết luận: ❌ Chưa merge — 1 Fail, 1 Rủi ro

## Checklist

- [x] Lint / analyze / typecheck
- [x] Unit / widget test
- [x] Regression
- [x] 5 nhóm case cho tính năng mới (+ nhóm lỗi hệ thống / đồng thời)
- [x] Security (kiểm quyền, IDOR, secrets)
- [ ] Chống bot / tấn công AI — không áp dụng (tính năng không có AI, không có endpoint công khai mới)
- [ ] Performance / memory — chưa chạy (mức "nhanh")
- [x] UI/UX / accessibility
- [ ] Store — chưa chạy (mức "nhanh")

## Tóm tắt

| Hạng mục | ✅ Pass | ❌ Fail | ⚠️ Rủi ro | ⏭️ Chưa chạy |
| --- | --- | --- | --- | --- |
| Lint, analyze | 2 | 0 | 0 | 0 |
| Test case tính năng | 10 | 1 | 0 | 0 |
| Security | 3 | 0 | 1 | 0 |
| UI/UX | 4 | 0 | 0 | 0 |

## Phải sửa trước khi merge

| ID | Test case | Input | Output thực tế | Cách sửa |
| --- | --- | --- | --- | --- |
| TC-05 | Mất 30 tháng Chạp, năm tháng Chạp thiếu (BR-02) | Ngày mất 30/12 âm, năm âm 2027 | API trả 500 `invalid lunar date` | `server/internal/gio/convert.go:42` — lấy `min(ngay, so_ngay_thang)` trước khi đổi lịch |

## Test case chi tiết

Kết quả: `✅ Pass` · `❌ Fail` · `⚠️ Rủi ro` · `⏭️ Chưa chạy`.

| ID | Nhóm | Test case | Input | Output mong đợi | Output thực tế | Kết quả | Cách sửa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TC-01 | happy path | Đổi ngày giỗ năm 2027 | Mất 15/3 âm | 21/04/2027 | 21/04/2027 | ✅ Pass | |
| TC-02 | happy path | Lưu cài đặt nhắc | 7d=on, 1d=on, 08:00 | 201, 2 lịch nhắc | 201, 2 lịch nhắc | ✅ Pass | |
| TC-03 | input sai | Ngày mất 31/2 âm (VR-01) | `lunar_day=31, month=2` | Bỏ qua người này, có cờ `invalid` | Như mong đợi | ✅ Pass | |
| TC-04 | input sai | Giờ nhắc 22:00 (VR-02) | `remind_time=22:00` | 400 | 400 | ✅ Pass | |
| TC-05 | giá trị biên | Tháng thiếu (BR-02) | Mất 30/12 âm, năm 2027 | Giỗ 29/12 âm, có ghi chú | 500 | ❌ Fail | Xem bảng trên |
| TC-06 | giá trị biên | Mất tháng nhuận (BR-03) | Mất 10/4 nhuận | Giỗ 10/4 thường | Như mong đợi | ✅ Pass | |
| TC-07 | giá trị biên | Bật nhắc sau mốc 7 ngày (BR-05) | Giỗ 21/04, bật 18/04 | Chỉ 1 lịch nhắc 20/04 | 1 lịch nhắc | ✅ Pass | |
| TC-08 | không có quyền | User ngoài nhà chung gọi danh sách | Token user khác | 403 | 403 | ✅ Pass | |
| TC-09 | không có quyền | Sửa cài đặt nhắc của người khác | `member_id` khác | 403 | 403 | ✅ Pass | |
| TC-10 | dữ liệu trống | Gia phả chưa có ngày mất | Nhà chung mới | Danh sách rỗng + `missing_count=0` | Như mong đợi | ✅ Pass | |
| TC-11 | lỗi hệ thống / đồng thời | Bấm "Tôi sẽ về" 2 lần | 2 request liền nhau | 1 bản ghi, request 2 trả 409 | Như mong đợi | ✅ Pass | |
| SEC-01 | security | Log khi gửi push | Log server | Không chứa tên người mất | Log có `person_name` ở mức debug | ⚠️ Rủi ro | `server/internal/gio/notify.go:88` — chỉ log `person_id` |

## Chi tiết cách sửa

### TC-05

```go
// server/internal/gio/convert.go
day := deathLunar.Day
if n := lunar.DaysInMonth(year, deathLunar.Month); day > n {
	day = n          // BR-02: tháng thiếu → giỗ ngày cuối tháng
	note = NoteShortMonth
}
```

### SEC-01

Bỏ `person_name` khỏi log, chỉ giữ `person_id` và `space_id`.

## Chưa chạy được

| Hạng mục | Lý do | Cách chạy tay |
| --- | --- | --- |
| Performance, memory, store | Mức "nhanh" không gồm | Chạy mức "full" trước khi release |
| Push đến đúng giờ trên máy thật | Cần thiết bị và đợi đến giờ nhắc | Đặt giờ nhắc +2 phút trên 1 iPhone, 1 Android thật |
