const pages = process.env.CI_PAGES_URL && new URL(process.env.CI_PAGES_URL);
module.exports = {
  title: 'BUỔI 6 · DevSecOps',
  tagline: 'Bảo mật xuyên suốt vòng đời phần mềm',
  url: pages ? pages.origin : 'https://mikmankkk.github.io',
  baseUrl: pages ? `${pages.pathname.replace(/\/$/, '')}/` : '/TH_LTANTT_2387700042/',
  organizationName: 'Mikmankkk',
  projectName: 'TH_LTANTT_2387700042',
  trailingSlash: true,
  onBrokenLinks: 'throw',
  i18n: { defaultLocale: 'vi', locales: ['vi'] },
  presets: [['classic', { docs: { sidebarPath: './sidebars.js' }, blog: false, theme: { customCss: './src/css/custom.css' } }]],
  themeConfig: {
    navbar: { title: '2387700042 / LAB 06', items: [ { to: '/docs/intro', label: 'Báo cáo', position: 'left' }, { href: 'https://github.com/Mikmankkk/TH_LTANTT_2387700042/tree/main/BUOI6', label: 'GitHub', position: 'right' } ] },
    footer: { style: 'dark', copyright: 'Võ Hoàng Minh Mẫn · MSSV 2387700042 · Lập trình an toàn thông tin' }
  }
};
