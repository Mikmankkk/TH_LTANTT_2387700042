import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';

export default function Home() {
  return <Layout title="Bảo mật với DevSecOps" description="Bài thực hành 6 của Võ Hoàng Minh Mẫn, MSSV 2387700042">
    <main>
      <section className="lab-hero"><div className="container">
        <p className="eyebrow">LẬP TRÌNH AN TOÀN THÔNG TIN / BÀI THỰC HÀNH 06</p>
        <h1>Chạy nhanh.<br/><span>Kiểm soát bảo mật.</span></h1>
        <p className="hero-description">Từ mã nguồn đến triển khai: kiểm tra tự động, quản lý artifact và những chốt bảo mật trong pipeline CI/CD.</p>
        <Link className="button button--primary button--lg" to="/docs/intro">Đọc báo cáo thực hành →</Link>
        <div className="author">Võ Hoàng Minh Mẫn <span> / </span> MSSV 2387700042</div>
      </div></section>
      <section className="container lab-content"><p className="eyebrow">QUY TRÌNH TRIỂN KHAI</p><h2>Mỗi thay đổi đều đi qua kiểm tra.</h2>
        <div className="lab-grid">{[
          ['01', 'Kiểm thử', 'Kiểm tra cấu hình pipeline, điều kiện triển khai và khả năng chặn đầu vào không an toàn.'],
          ['02', 'Bảo mật', 'SAST, dò bí mật và phân tích dependency. Lỗi nghiêm trọng dừng chuỗi triển khai.'],
          ['03', 'Build & artifact', 'Docusaurus tạo trang tĩnh. Artifact giữ lại kết quả và SHA-256 để đối chiếu.'],
          ['04', 'Triển khai', 'Chỉ nhánh mặc định được xuất bản. GitLab Pages và GitHub Actions có cấu hình riêng.']
        ].map(([number,title,text])=><article key={number}><span className="step">{number}</span><h3>{title}</h3><p>{text}</p></article>)}</div>
        <p className="lab-note">Cấu hình GitLab được lưu kèm bài. Trạng thái chạy thực tế và ảnh minh chứng được ghi trong README của repository.</p>
      </section>
    </main>
  </Layout>;
}
