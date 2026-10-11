# TH_LTANTT_2387700042
## BÁO CÁO THỰC HÀNH LẬP TRÌNH AN TOÀN THÔNG TIN

- **Học viên**: **Võ Hoàng Minh Mẫn**
- **MSSV**: **2387700042**
- **Repository**: [https://github.com/Mikmankkk/TH_LTANTT_2387700042](https://github.com/Mikmankkk/TH_LTANTT_2387700042)

---

### 📂 DANH MỤC CÁC BUỔI THỰC HÀNH

#### 1. [BUỔI 1: CƠ SỞ LẬP TRÌNH BẢO MẬT](BUOI1/README.md)
- **Lab 1**: Xác thực & làm sạch dữ liệu đầu vào (Input Validation & Sanitization - Regex, SSRF, SQLi, XSS, Path Traversal).
- **Lab 2**: An toàn mã nguồn với Git Hooks (Pre-commit hook kiểm tra secrets, file permissions, Bandit SAST).
- **Lab 3**: Hệ thống ghi nhật ký ưu tiên bảo mật (Secure Logger - PII Masking, Hash SHA-256, Log Rotation GZip).
- 👉 *Xem chi tiết tại:* [BUOI1/README.md](BUOI1/README.md)

#### 2. [BUỔI 3: BẢO MẬT MẠNG MÁY TÍNH & TRINH SÁT HỆ THỐNG](BUOI3/README.md)
- **Phần 1: SecureChat**: Lập trình Socket bảo mật đa luồng với xác thực chứng chỉ hai chiều (Mutual TLS / mTLS) bằng OpenSSL và mã hóa đầu-cuối E2EE bằng thuật toán AES-256-CBC với PKCS#7 padding.
- **Phần 2: NetRecon**: Phát triển bộ công cụ khám phá và trinh sát mạng đa giao diện (CLI & Web Flask/HTMX):
  - Quét cổng bất đồng bộ AsyncIO có kiểm soát tốc độ (Rate limiting).
  - Nhận diện phiên bản dịch vụ với Nmap (`-sV`).
  - Thu thập biểu ngữ dịch vụ mạng (Banner Grabbing).
  - Lập bản đồ mạng cục bộ qua ARP (`arp -a`).
  - Tra cứu và cảnh báo mã lỗ hổng bảo mật phổ biến (CVE Checker).
  - Lọc mục tiêu theo Whitelist / Blacklist và gửi báo cáo qua Email (SMTP SSL).
- 👉 *Xem chi tiết tại:* [BUOI3/README.md](BUOI3/README.md)

#### 3. [BUỔI 4: BẢO MẬT WEB APP VÀ API](BUOI4/README.md)
- **Phần 1: Web Vulnerability Scanner (`web-vuln-scanner`)**: Phát triển công cụ rà quét lỗ hổng ứng dụng Web toàn diện theo chuẩn OWASP Top 10 (CLI & Web UI Flask):
  - Nhận diện lỗ hổng Cross-Site Scripting (Reflected XSS) thông qua thư viện payload chuẩn hóa.
  - Kiểm thử và phát hiện các biến thể SQL Injection qua Query Parameters.
  - Phân tích và phát hiện biểu mẫu thiếu sót cơ chế Anti-CSRF Token.
  - Kiểm tra và ngăn ngừa nguy cơ Server-Side Request Forgery (SSRF) truy cập tài nguyên mạng nội bộ & Cloud Metadata.
  - Báo cáo phân loại rủi ro (Critical, High, Medium, Low) và giao diện trực quan thân thiện.
- **Phần 2: JWT & OAuth Security Tools (`jwt-security-tools`)**: Bộ giải pháp an toàn xác thực token & API Gateway:
  - Kiểm tra toàn diện tính hợp lệ, chữ ký số và thời hạn hiệu lực của JSON Web Token (`JWTValidator`).
  - Thử nghiệm tấn công vét cạn bẻ khóa bí mật JWT bằng kỹ thuật từ điển đa luồng (`JWTCracker`).
  - Triển khai máy khách tuân thủ chuẩn luồng ủy quyền OAuth 2.0 Authorization Code Flow (`OAuthClient`).
  - Quản lý vòng đời token, tự động cấp phát Access Token ngắn hạn và xoay vòng Refresh Token (`TokenManager`).
  - Xây dựng cổng bảo vệ API Gateway tích hợp xác thực Bearer token cho endpoint nhạy cảm (`APIGateway`).
- 👉 *Xem chi tiết tại:* [BUOI4/README.md](BUOI4/README.md)
