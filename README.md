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
