# Kiểm thử <project> — <dd/mm/yyyy HH:mm> — <nhanh / full / release>

Nhánh: <branch> · Commit: <sha> · Phạm vi: <n tính năng, m file>
Kết luận: <✅ Merge được / ❌ Chưa merge — x Fail, y Rủi ro>

## Checklist

- [ ] Lint / analyze / typecheck
- [ ] Unit / widget test
- [ ] Regression
- [ ] 5 nhóm case cho tính năng mới
- [ ] Security (kiểm quyền, IDOR, secrets)
- [ ] Chống bot / tấn công AI
- [ ] Performance / memory
- [ ] UI/UX / accessibility
- [ ] Store (App Store / Google Play)

## Tóm tắt

| Hạng mục | ✅ Pass | ❌ Fail | ⚠️ Rủi ro | ⏭️ Chưa chạy |
| --- | --- | --- | --- | --- |
| <...> | | | | |

## Phải sửa trước khi merge

| ID | Test case | Input | Output thực tế | Cách sửa |
| --- | --- | --- | --- | --- |

## Test case chi tiết

Kết quả: `✅ Pass` · `❌ Fail` · `⚠️ Rủi ro` · `⏭️ Chưa chạy`. Dòng ❌ / ⚠️ bắt buộc có cách sửa (`file:dòng` + 1–3 câu).

| ID | Nhóm | Test case | Input | Output mong đợi | Output thực tế | Kết quả | Cách sửa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CASE-1 | giá trị biên | <...> | <...> | <...> | <...> | ❌ Fail | <file:dòng — ...> |

## Chi tiết cách sửa

### <ID>

<đoạn code / patch gợi ý>

## Chưa chạy được

| Hạng mục | Lý do | Cách chạy tay |
| --- | --- | --- |
