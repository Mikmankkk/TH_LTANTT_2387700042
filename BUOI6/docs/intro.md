---
sidebar_position: 1
title: Báo cáo thực hành 6
---

# Bảo mật với DevSecOps

**Sinh viên: Võ Hoàng Minh Mẫn — MSSV: 2387700042.**

Bài thực hành triển khai hai pipeline theo lab-06.docx: ví dụ bốn job và dự án Docusaurus với build artifact, triển khai Pages. Mã nguồn được nộp trong thư mục BUOI6 trên GitHub.

## Pipeline cơ bản

`examples/basic.gitlab-ci.yml` gồm build-job, test-job1, test-job2 (chờ 20 giây) và deploy-prod. Hai job test cùng stage nên có thể chạy song song nếu runner đủ tài nguyên. Deploy chờ toàn bộ test thành công.

## Pipeline Docusaurus

File `.gitlab-ci.yml` ở gốc repository include cấu hình trong BUOI6. Các job test, security và dependency-audit phải thành công trước build. Build tạo `build/` và checksum. Job Pages nhận artifact, chuyển sang `public/` rồi xuất bản trên nhánh mặc định.

## Các chốt bảo mật

- SAST dùng Semgrep với bộ luật JavaScript, không cho phép lỗi bị bỏ qua.
- Gitleaks quét bí mật trong phạm vi BUOI6; không lưu token trong mã nguồn.
- `node scripts/audit.mjs` kiểm tra dependency trong lockfile, chặn advisory high/critical ngoài ngoại lệ có phiên bản và thời hạn cụ thể. Còn advisory `GHSA-vfj7-8cjw-p6xm` của braces 3.0.3 chưa có bản vá; ngoại lệ build có hạn đến 21/11/2026 được ghi trong `security-exceptions.json`. Không tuyên bố audit sạch.
- Script kiểm tra bổ sung chặn dynamic evaluation, private key, credential có định dạng phổ biến và Dockerfile chạy root; đây chỉ là lớp bổ sung, không thay thế scanner chuyên dụng.
- Chỉ job triển khai có quyền Pages và OIDC trên GitHub. Không đưa secret vào pull request từ fork.
- Hash SHA-256 giúp kiểm tra artifact; hash không phải chữ ký số. Chưa tuyên bố đã bật MFA, branch protection hoặc ký commit nếu chưa có bằng chứng từ hệ thống.

## Phạm vi xác minh

README chứa log, ảnh CMD và trạng thái dịch vụ được quan sát khi chạy bài. Cấu hình GitLab không đồng nghĩa đã có pipeline GitLab chạy thành công; cần tài khoản GitLab có quyền tạo dự án và runner khả dụng.

## Tài liệu

- [GitLab CI/CD YAML](https://docs.gitlab.com/ci/yaml/)
- [GitLab Pages](https://docs.gitlab.com/user/project/pages/getting_started/pages_from_scratch/)
- [Docusaurus deployment](https://docusaurus.io/docs/deployment)
