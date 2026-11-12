# Roadmap: <tên dự án>

Cập nhật: <dd/mm/yyyy> · Mục tiêu MVP: <ngày phát hành dự kiến>

<!--
Mỗi task đủ nhỏ để làm và test xong trong 1 phiên (khoảng 1–3 giờ), đi theo vertical slice (DB + API + UI của một tính năng).
Ước lượng: S ≤ 2 giờ, M ≤ 1 ngày, L ≤ 3 ngày; lớn hơn L thì chia nhỏ.
Claude Code đọc file này khi nhận task: "Làm T-12 trong docs/ROADMAP.md".
-->

## M0 — Skeleton

- [ ] **T-01** Repo, CLAUDE.md, `.claude/settings.json`, CI chạy lint + test · layer: all · S
  - AC: PR mở ra thì CI chạy và xanh
- [ ] **T-02** Docker Compose (API + DB), health check `/healthz` · API/DB · S · phụ thuộc T-01
- [ ] **T-03** App gọi được `/healthz`, hiện trạng thái · App · S · phụ thuộc T-02

## M1 — Auth và user

- [ ] **T-10** <...> · <layer> · <S/M/L> · phụ thuộc <...> · story <US-01>
  - AC: <...>

## M2 — Tính năng cốt lõi

- [ ] **T-20** <...>

## M3 — Các tính năng MUST còn lại

## M4 — Hoàn thiện

- [ ] Đủ trạng thái loading / rỗng / lỗi mọi màn
- [ ] Analytics event, crash report
- [ ] Rà bảo mật, rà store theo [checklist-release.md](checklist-release.md)

## M5 — Phát hành

- [ ] Build release, store listing, privacy policy, deploy production

## Sau MVP (chưa làm)

| Ý tưởng | Nguồn (review, khách, số liệu) | Ưu tiên |
| --- | --- | --- |
| <...> | <...> | <...> |
