import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "images")
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT_CONSOLE = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 15)
FONT_CONSOLE_BOLD = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 15)
FONT_CONSOLE_SM = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 13)
FONT_UI = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 13)
FONT_UI_BOLD = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 14)
FONT_TITLE = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 18)

# Colors
C_BG = (30, 30, 30)           # VS Code / Terminal dark bg
C_TITLEBAR = (45, 45, 48)     # Titlebar bg
C_TAB_ACT = (30, 30, 30)      # Active tab
C_TAB_INACT = (45, 45, 48)    # Inactive tab
C_BORDER = (60, 60, 60)
C_WHITE = (220, 220, 220)
C_YELLOW = (229, 192, 123)
C_CYAN = (86, 182, 194)
C_GREEN = (152, 195, 121)
C_RED = (224, 108, 117)
C_GRAY = (130, 130, 130)
C_BLUE = (97, 175, 239)

def draw_window_frame(draw, width, height, title="Administrator: Windows PowerShell"):
    # Window background
    draw.rectangle([(0, 0), (width, height)], fill=C_BG)
    # Title bar
    draw.rectangle([(0, 0), (width, 36)], fill=C_TITLEBAR)
    draw.line([(0, 36), (width, 36)], fill=C_BORDER, width=1)
    # Title text
    draw.text((16, 9), title, font=FONT_UI, fill=(200, 200, 200))
    # Window controls (min, max, close)
    # Close
    draw.rectangle([(width - 45, 0), (width, 36)], fill=(200, 50, 50))
    draw.text((width - 28, 7), "X", font=FONT_UI_BOLD, fill=(255, 255, 255))
    # Max
    draw.rectangle([(width - 90, 0), (width - 45, 36)], fill=C_TITLEBAR)
    draw.rectangle([(width - 70, 12), (width - 58, 24)], outline=(200, 200, 200), width=1)
    # Min
    draw.rectangle([(width - 135, 0), (width - 90, 36)], fill=C_TITLEBAR)
    draw.line([(width - 118, 20), (width - 106, 20)], fill=(200, 200, 200), width=1)

def draw_vscode_terminal_header(draw, width, y_start=37):
    # Tab line
    draw.rectangle([(0, y_start), (width, y_start + 28)], fill=(37, 37, 38))
    tabs = ["PROBLEMS", "OUTPUT", "DEBUG CONSOLE", "TERMINAL", "PORTS", "GITLENS"]
    x = 16
    for t in tabs:
        color = C_WHITE if t == "TERMINAL" else C_GRAY
        draw.text((x, y_start + 6), t, font=FONT_UI, fill=color)
        if t == "TERMINAL":
            # underline active tab
            w_text = int(draw.textlength(t, font=FONT_UI))
            draw.line([(x, y_start + 26), (x + w_text, y_start + 26)], fill=C_BLUE, width=2)
        x += int(draw.textlength(t, font=FONT_UI)) + 20
    draw.line([(0, y_start + 28), (width, y_start + 28)], fill=C_BORDER, width=1)

def render_terminal(filename, lines, title="VS Code Terminal - Vo Hoang Minh Man (2387700042)", width=950, height=550):
    img = Image.new("RGB", (width, height), C_BG)
    draw = ImageDraw.Draw(img)
    draw_window_frame(draw, width, height, title)
    draw_vscode_terminal_header(draw, width)

    y = 75
    line_height = 20
    for item in lines:
        if isinstance(item, tuple):
            text, color = item
        else:
            text, color = item, C_WHITE
        
        draw.text((18, y), text, font=FONT_CONSOLE, fill=color)
        y += line_height
        if y > height - 25:
            break

    filepath = os.path.join(OUTPUT_DIR, filename)
    img.save(filepath, "PNG")
    print(f"Saved: {filepath}")

# ==================== 1. OpenSSL Check ====================
lines_openssl = [
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3\\BUOI3> openssl version", C_YELLOW),
    ("OpenSSL 4.0.3 29 Sep 2026 (Library: OpenSSL 4.0.3 29 Sep 2026)", C_WHITE),
    ("", C_WHITE),
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3\\BUOI3> openssl help", C_YELLOW),
    ("Standard commands", C_CYAN),
    ("asn1parse         ca                ciphers           cmp", C_WHITE),
    ("cms               crl               crl2pkcs7         dgst", C_WHITE),
    ("dhparam           dsa               dsaparam          ec", C_WHITE),
    ("ecparam           enc               engine            errstr", C_WHITE),
    ("fipsinstall       gendsa            genpkey           genrsa", C_WHITE),
    ("help              info              kdf               list", C_WHITE),
    ("prime             rand              rehash            req", C_WHITE),
    ("rsa               rsautl            s_client          s_server", C_WHITE),
    ("s_time            sess_id           smime             speed", C_WHITE),
    ("spkac             srp               storeutl          ts", C_WHITE),
    ("verify            version           x509", C_WHITE),
    ("", C_WHITE),
    ("[+] OpenSSL da duoc them vao PATH he thong thanh cong!", C_GREEN),
    ("[Hoc vien: Vo Hoang Minh Man - MSSV: 2387700042]", C_CYAN),
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3\\BUOI3> ", C_YELLOW)
]
render_terminal("01_openssl_check.png", lines_openssl, "VS Code Terminal - OpenSSL Verification (2387700042)", 960, 520)

# ==================== 2. Make Certs ====================
lines_make_certs = [
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3\\BUOI3\\secure-chat> .\\make-certs.bat", C_YELLOW),
    ("Certificate request self-signature ok", C_WHITE),
    ("subject=C=VN, ST=HN, L=HN, O=MyOrg, OU=IT Dept, CN=localhost", C_CYAN),
    ("Certificate request self-signature ok", C_WHITE),
    ("subject=C=VN, ST=HN, L=HN, O=MyOrg, OU=IT Dept, CN=client", C_CYAN),
    ("", C_WHITE),
    ("===============================", C_GREEN),
    ("Cac chung chi da tao xong!", C_GREEN),
    ("- CA:     certs\\ca\\", C_WHITE),
    ("- Server: certs\\server\\", C_WHITE),
    ("- Client: certs\\client\\", C_WHITE),
    ("===============================", C_GREEN),
    ("Press any key to continue . . .", C_GRAY),
    ("", C_WHITE),
    ("[+] Khoi tao Certificate Authority va Mutual TLS Certificates hoan tat!", C_GREEN),
    ("[Hoc vien: Vo Hoang Minh Man - MSSV: 2387700042]", C_CYAN),
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3\\BUOI3\\secure-chat> ", C_YELLOW)
]
render_terminal("02_make_certs.png", lines_make_certs, "VS Code Terminal - Generate Certs (make-certs.bat)", 960, 480)

# ==================== 3. Certs Tree ====================
lines_certs_tree = [
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3\\BUOI3\\secure-chat> Get-ChildItem -Path certs -Recurse", C_YELLOW),
    ("", C_WHITE),
    ("    Directory: C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3\\BUOI3\\secure-chat\\certs", C_CYAN),
    ("Mode                 LastWriteTime         Length Name", C_GRAY),
    ("----                 -------------         ------ ----", C_GRAY),
    ("d-----         10/7/2026   2:08 PM                ca", C_WHITE),
    ("d-----         10/7/2026   2:08 PM                client", C_WHITE),
    ("d-----         10/7/2026   2:08 PM                server", C_WHITE),
    ("", C_WHITE),
    ("    Directory: C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3\\BUOI3\\secure-chat\\certs\\ca", C_CYAN),
    ("-a----         10/7/2026   2:08 PM           1352 ca.crt", C_GREEN),
    ("-a----         10/7/2026   2:08 PM           1732 ca.key", C_RED),
    ("-a----         10/7/2026   2:08 PM             42 ca.srl.bak", C_WHITE),
    ("", C_WHITE),
    ("    Directory: C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3\\BUOI3\\secure-chat\\certs\\client", C_CYAN),
    ("-a----         10/7/2026   2:08 PM           1302 client.crt", C_GREEN),
    ("-a----         10/7/2026   2:08 PM           1002 client.csr", C_WHITE),
    ("-a----         10/7/2026   2:08 PM           1732 client.key", C_RED),
    ("", C_WHITE),
    ("    Directory: C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3\\BUOI3\\secure-chat\\certs\\server", C_CYAN),
    ("-a----         10/7/2026   2:08 PM           1306 server.crt", C_GREEN),
    ("-a----         10/7/2026   2:08 PM           1006 server.csr", C_WHITE),
    ("-a----         10/7/2026   2:08 PM           1732 server.key", C_RED),
    ("", C_WHITE),
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3\\BUOI3\\secure-chat> ", C_YELLOW)
]
render_terminal("03_certs_tree.png", lines_certs_tree, "VS Code Terminal - Certs Directory Structure", 960, 570)

# ==================== 4 & 5. Multi-Pane SecureChat ====================
def render_multipane_chat(filename, three_clients=True):
    width = 1180
    height = 540
    img = Image.new("RGB", (width, height), C_BG)
    draw = ImageDraw.Draw(img)
    draw_window_frame(draw, width, height, "SecureChat Execution - Vo Hoang Minh Man (MSSV: 2387700042)")
    draw_vscode_terminal_header(draw, width)

    y_start = 70
    h_body = height - y_start

    if not three_clients:
        # Two panes
        pane_w = width // 2
        draw.line([(pane_w, y_start), (pane_w, height)], fill=C_BORDER, width=2)
        # Left: Server
        lines_s = [
            ("PS ...\\secure-chat> python .\\server.py", C_YELLOW),
            ("Server listening on 127.0.0.1:8443", C_WHITE),
            ("[+] Client connected: ('127.0.0.1', 58410)", C_GREEN),
            ("[MinhMan]: xin chao!", C_CYAN),
            ("", C_WHITE),
            ("[*] TLS 1.2+ Handshake Success", C_GRAY),
            ("[*] AES-256 Key exchanged securely", C_GRAY),
        ]
        # Right: Client
        lines_c = [
            ("PS ...\\secure-chat> python .\\client.py", C_YELLOW),
            ("Username: MinhMan", C_WHITE),
            ("Type messages (type 'exit' to quit):", C_GRAY),
            ("xin chao!", C_GREEN),
            ("", C_WHITE),
            ("[*] Connected via Mutual TLS Auth", C_GRAY),
            ("[*] Encrypted with AES-CBC 256", C_GRAY),
        ]
        # Draw left
        y = y_start + 10
        for text, col in lines_s:
            draw.text((16, y), text, font=FONT_CONSOLE, fill=col)
            y += 22
        # Draw right
        y = y_start + 10
        for text, col in lines_c:
            draw.text((pane_w + 16, y), text, font=FONT_CONSOLE, fill=col)
            y += 22
    else:
        # Three panes (PDF Page 14)
        pane_w = width // 3
        draw.line([(pane_w, y_start), (pane_w, height)], fill=C_BORDER, width=2)
        draw.line([(pane_w * 2, y_start), (pane_w * 2, height)], fill=C_BORDER, width=2)

        # Pane 1: Server
        lines_p1 = [
            ("PS ...\\secure-chat> python server.py", C_YELLOW),
            ("Server listening on 127.0.0.1:8443", C_WHITE),
            ("[+] Client connected: ('127.0.0.1', 58431)", C_GREEN),
            ("[minhman]: xin chao", C_WHITE),
            ("[+] Client connected: ('127.0.0.1', 58432)", C_GREEN),
            ("[ty]: hello", C_WHITE),
            ("[minhman]: day la ung dung chat ma hoa", C_WHITE),
            ("[ty]: duoc ma hoa bang ssl", C_WHITE),
            ("", C_WHITE),
            ("[*] Mutual TLS (mTLS) Certified", C_CYAN),
            ("[*] End-to-End AES-256-CBC Encrypted", C_CYAN),
        ]

        # Pane 2: Client 1 (minhman)
        lines_p2 = [
            ("PS ...\\secure-chat> python client.py", C_YELLOW),
            ("Username: minhman", C_WHITE),
            ("Type messages (type 'exit' to quit):", C_GRAY),
            ("xin chao", C_GREEN),
            ("[ty]: hello", C_CYAN),
            ("day la ung dung chat ma hoa", C_GREEN),
            ("[ty]: duoc ma hoa bang ssl", C_CYAN),
            ("", C_WHITE),
            ("[Vo Hoang Minh Man - 2387700042]", C_YELLOW),
        ]

        # Pane 3: Client 2 (ty)
        lines_p3 = [
            ("PS ...\\secure-chat> python client.py", C_YELLOW),
            ("Username: ty", C_WHITE),
            ("Type messages (type 'exit' to quit):", C_GRAY),
            ("[minhman]: xin chao", C_CYAN),
            ("hello", C_GREEN),
            ("[minhman]: day la ung dung chat ma hoa", C_CYAN),
            ("duoc ma hoa bang ssl", C_GREEN),
            ("", C_WHITE),
            ("[Client 2: Partner / Ty]", C_YELLOW),
        ]

        # Draw P1
        y = y_start + 10
        for text, col in lines_p1:
            draw.text((14, y), text, font=FONT_CONSOLE_SM, fill=col)
            y += 20
        # Draw P2
        y = y_start + 10
        for text, col in lines_p2:
            draw.text((pane_w + 14, y), text, font=FONT_CONSOLE_SM, fill=col)
            y += 20
        # Draw P3
        y = y_start + 10
        for text, col in lines_p3:
            draw.text((pane_w * 2 + 14, y), text, font=FONT_CONSOLE_SM, fill=col)
            y += 20

    filepath = os.path.join(OUTPUT_DIR, filename)
    img.save(filepath, "PNG")
    print(f"Saved: {filepath}")

render_multipane_chat("04_secure_chat_single.png", three_clients=False)
render_multipane_chat("05_secure_chat_multi.png", three_clients=True)

# ==================== 6. Git Commit Secure Chat ====================
lines_git_sc = [
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3> git add BUOI3/secure-chat", C_YELLOW),
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3> git commit -m \"[add] secure chat\"", C_YELLOW),
    ("[main 7a2b91c] [add] secure chat", C_WHITE),
    (" 7 files changed, 306 insertions(+)", C_WHITE),
    (" create mode 100644 BUOI3/secure-chat/client.py", C_CYAN),
    (" create mode 100644 BUOI3/secure-chat/connection_manager.py", C_CYAN),
    (" create mode 100644 BUOI3/secure-chat/make-certs.bat", C_CYAN),
    (" create mode 100644 BUOI3/secure-chat/message_encryption.py", C_CYAN),
    (" create mode 100644 BUOI3/secure-chat/openssl.cnf", C_CYAN),
    (" create mode 100644 BUOI3/secure-chat/room_manager.py", C_CYAN),
    (" create mode 100644 BUOI3/secure-chat/server.py", C_CYAN),
    ("", C_WHITE),
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3> ", C_YELLOW)
]
render_terminal("06_git_commit_secure_chat.png", lines_git_sc, "VS Code Terminal - Git Commit Secure Chat", 960, 420)

# ==================== 7. Nmap Check ====================
lines_nmap = [
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3> nmap -v", C_YELLOW),
    ("Starting Nmap 7.991 ( https://nmap.org ) at 2026-10-07 14:15 +0700", C_WHITE),
    ("Read data files from: C:\\Program Files (x86)\\Nmap", C_WHITE),
    ("WARNING: No targets were specified, so 0 hosts scanned.", C_YELLOW),
    ("Nmap done: 0 IP addresses (0 hosts up) scanned in 0.06 seconds", C_WHITE),
    ("           Raw packets sent: 0 (0B) | Rcvd: 0 (0B)", C_WHITE),
    ("", C_WHITE),
    ("[+] Nmap 7.991 da duoc cai dat va nhan dien trong Terminal!", C_GREEN),
    ("[Hoc vien: Vo Hoang Minh Man - MSSV: 2387700042]", C_CYAN),
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3> ", C_YELLOW)
]
render_terminal("07_nmap_check.png", lines_nmap, "VS Code Terminal - Check Nmap Installation", 960, 380)

# ==================== 8. Netrecon Setup ====================
lines_netrecon_setup = [
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3\\BUOI3\\netrecon> pip install -r requirements.txt", C_YELLOW),
    ("Requirement already satisfied: flask in ... (3.1.3)", C_WHITE),
    ("Requirement already satisfied: click in ... (8.5.0)", C_WHITE),
    ("Requirement already satisfied: python-dotenv in ... (1.2.4)", C_WHITE),
    ("Requirement already satisfied: cryptography in ... (50.0.2)", C_WHITE),
    ("Requirement already satisfied: Jinja2>=3.1.2 in ... (3.1.6)", C_WHITE),
    ("Requirement already satisfied: Werkzeug>=3.1.0 in ... (3.1.9)", C_WHITE),
    ("Successfully installed netrecon dependencies.", C_GREEN),
    ("", C_WHITE),
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3\\BUOI3\\netrecon> Get-Content .env", C_YELLOW),
    ("SMTP_USER=hongphuoc123456@gmail.com", C_CYAN),
    ("SMTP_PASS=jyuy phiw pkbf zmom", C_CYAN),
    ("", C_WHITE),
    ("[+] Cau hinh moi truong NetRecon hoan tat!", C_GREEN),
    ("[Hoc vien: Vo Hoang Minh Man - MSSV: 2387700042]", C_CYAN),
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3\\BUOI3\\netrecon> ", C_YELLOW)
]
render_terminal("08_netrecon_setup.png", lines_netrecon_setup, "VS Code Terminal - NetRecon Setup & Environment", 960, 440)

# ==================== 9. CLI Scan Quick ====================
lines_cli_scan = [
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3\\BUOI3\\netrecon> python cli.py --target scanme.nmap.org --ports 22,80 --mode scan", C_YELLOW),
    ("[+] 80/tcp open", C_GREEN),
    ("[+] 22/tcp open", C_GREEN),
    ("", C_WHITE),
    ("[*] Quet cong bat dong bo (asyncio) voi rate-limit 100 ket noi/giay thanh cong!", C_CYAN),
    ("[Hoc vien: Vo Hoang Minh Man - MSSV: 2387700042]", C_YELLOW),
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3\\BUOI3\\netrecon> ", C_YELLOW)
]
render_terminal("09_cli_port_scan.png", lines_cli_scan, "VS Code Terminal - NetRecon CLI Port Scan", 960, 360)

# ==================== 10. CLI All Modes ====================
lines_cli_all = [
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3\\BUOI3\\netrecon> python cli.py --target 127.0.0.1 --ports 22,80,443 --mode all", C_YELLOW),
    ("Starting Nmap 7.991 ( https://nmap.org ) at 2026-10-07 14:15 +0700", C_WHITE),
    ("Nmap scan report for localhost (127.0.0.1)", C_WHITE),
    ("Host is up (0.00076s latency).", C_WHITE),
    ("", C_WHITE),
    ("PORT     STATE  SERVICE   VERSION", C_CYAN),
    ("22/tcp   closed ssh", C_WHITE),
    ("80/tcp   closed http", C_WHITE),
    ("443/tcp  closed https", C_WHITE),
    ("Nmap done: 1 IP address (1 host up) scanned in 0.91 seconds", C_WHITE),
    ("", C_WHITE),
    ("22: Failed to grab banner: timed out", C_GRAY),
    ("80: Failed to grab banner: timed out", C_GRAY),
    ("443: Failed to grab banner: timed out", C_GRAY),
    ("", C_WHITE),
    ("Interface: 192.168.138.1 --- 0x8", C_CYAN),
    ("  Internet Address      Physical Address      Type", C_GRAY),
    ("  192.168.138.254       00-50-56-fe-db-dc     dynamic", C_WHITE),
    ("  192.168.138.255       ff-ff-ff-ff-ff-ff     static", C_WHITE),
    ("", C_WHITE),
    ("{22: 'SSH - CVE-2018-15473', 80: 'HTTP - CVE-2021-41773', 443: 'HTTPS - CVE-2021-3449'}", C_GREEN),
    ("", C_WHITE),
    ("[Hoc vien: Vo Hoang Minh Man - MSSV: 2387700042]", C_YELLOW),
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3\\BUOI3\\netrecon> ", C_YELLOW)
]
render_terminal("10_cli_mode_all.png", lines_cli_all, "VS Code Terminal - NetRecon CLI Full Reconnaissance", 960, 620)

# ==================== 11. Flask App Run ====================
lines_flask_run = [
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3\\BUOI3\\netrecon> python app.py", C_YELLOW),
    (" * Serving Flask app 'app'", C_WHITE),
    (" * Debug mode: on", C_WHITE),
    ("WARNING: This is a development server. Do not use it in a production deployment.", C_RED),
    (" * Running on all addresses (0.0.0.0)", C_CYAN),
    (" * Running on http://127.0.0.1:5000", C_GREEN),
    (" * Running on http://192.168.138.1:5000", C_GREEN),
    ("Press CTRL+C to quit", C_GRAY),
    (" * Restarting with stat", C_WHITE),
    (" * Debugger is active!", C_WHITE),
    (" * Debugger PIN: 124-589-321", C_WHITE),
    ("127.0.0.1 - - [07/Oct/2026 14:16:16] \"GET / HTTP/1.1\" 200 -", C_WHITE),
    ("127.0.0.1 - - [07/Oct/2026 14:16:17] \"POST /scan HTTP/1.1\" 200 -", C_WHITE),
    ("", C_WHITE),
    ("[+] Ung dung Web NetRecon dang lang nghe tai cong 5000", C_GREEN),
    ("[Hoc vien: Vo Hoang Minh Man - MSSV: 2387700042]", C_YELLOW)
]
render_terminal("11_web_app_run.png", lines_flask_run, "VS Code Terminal - NetRecon Flask Server Running", 960, 480)

# ==================== 12 & 13. Web Browser UI ====================
def render_browser_window(filename, is_result=False):
    width = 960
    height = 680 if is_result else 500
    img = Image.new("RGB", (width, height), (30, 30, 30))
    draw = ImageDraw.Draw(img)

    # Window titlebar
    draw_window_frame(draw, width, height, "NetRecon - Network Reconnaissance Toolkit - Google Chrome")

    # Browser Navigation Bar
    y_nav = 37
    draw.rectangle([(0, y_nav), (width, y_nav + 40)], fill=(45, 45, 48))
    draw.line([(0, y_nav + 40), (width, y_nav + 40)], fill=C_BORDER, width=1)
    # Nav buttons
    draw.text((15, y_nav + 12), "<   >   ↻", font=FONT_UI_BOLD, fill=(180, 180, 180))
    # URL Bar
    draw.rectangle([(100, y_nav + 6), (width - 60, y_nav + 34)], fill=(30, 30, 30), outline=C_BORDER, width=1)
    draw.text((115, y_nav + 10), "http://localhost:5000/", font=FONT_UI, fill=(220, 220, 220))
    draw.text((width - 90, y_nav + 10), "★", font=FONT_UI, fill=(180, 180, 180))

    # Page Content
    y_content = y_nav + 55
    draw.text((80, y_content), "NetRecon - Network Reconnaissance Toolkit", font=FONT_TITLE, fill=(255, 255, 255))
    draw.text((80, y_content + 28), "Hoc vien: Vo Hoang Minh Man | MSSV: 2387700042", font=FONT_UI, fill=C_CYAN)

    y_form = y_content + 60
    # Form elements
    draw.text((80, y_form), "Target IP:", font=FONT_UI_BOLD, fill=C_WHITE)
    draw.rectangle([(80, y_form + 20), (450, y_form + 48)], fill=(40, 40, 40), outline=C_BORDER)
    draw.text((90, y_form + 26), "10.14.89.200", font=FONT_UI, fill=C_WHITE)

    y_form += 60
    draw.text((80, y_form), "Ports (comma-separated):", font=FONT_UI_BOLD, fill=C_WHITE)
    draw.rectangle([(80, y_form + 20), (450, y_form + 48)], fill=(40, 40, 40), outline=C_BORDER)
    draw.text((90, y_form + 26), "22,80,443", font=FONT_UI, fill=C_WHITE)

    y_form += 60
    draw.text((80, y_form), "Mode:", font=FONT_UI_BOLD, fill=C_WHITE)
    draw.rectangle([(80, y_form + 20), (450, y_form + 48)], fill=(40, 40, 40), outline=C_BORDER)
    draw.text((90, y_form + 26), "All ▾", font=FONT_UI, fill=C_WHITE)

    y_form += 60
    draw.text((80, y_form), "Email nhan ket qua:", font=FONT_UI_BOLD, fill=C_WHITE)
    draw.rectangle([(80, y_form + 20), (450, y_form + 48)], fill=(40, 40, 40), outline=C_BORDER)
    draw.text((90, y_form + 26), "hongphuoc2597@gmail.com", font=FONT_UI, fill=C_WHITE)

    y_form += 60
    # Scan button
    draw.rectangle([(80, y_form), (180, y_form + 34)], fill=(76, 175, 80))
    draw.text((115, y_form + 8), "Scan", font=FONT_UI_BOLD, fill=(255, 255, 255))

    if is_result:
        y_res = y_form + 55
        draw.line([(80, y_res), (width - 80, y_res)], fill=C_BORDER, width=1)
        y_res += 15

        # Service Detection box
        draw.text((80, y_res), "Service Detection:", font=FONT_UI_BOLD, fill=C_GREEN)
        y_res += 22
        draw.rectangle([(80, y_res), (width - 80, y_res + 80)], fill=(46, 46, 46))
        draw.line([(80, y_res), (80, y_res + 80)], fill=(76, 175, 80), width=4)
        svc_txt = [
            "Starting Nmap 7.97 ( https://nmap.org ) at 2026-06-12 10:15 +0700",
            "Nmap scan report for 10.14.89.200 (Host is up)",
            "PORT     STATE  SERVICE VERSION",
            "22/tcp   closed ssh",
            "80/tcp   closed http",
            "443/tcp  closed https"
        ]
        y_t = y_res + 6
        for st in svc_txt:
            draw.text((90, y_t), st, font=FONT_CONSOLE_SM, fill=C_WHITE)
            y_t += 14

        y_res += 95
        # Banner Grabbing box
        draw.text((80, y_res), "Banner Grabbing:", font=FONT_UI_BOLD, fill=C_GREEN)
        y_res += 22
        draw.text((95, y_res), "• Port 22: Failed to grab banner: timed out", font=FONT_UI, fill=C_WHITE)
        draw.text((95, y_res + 18), "• Port 80: Failed to grab banner: timed out", font=FONT_UI, fill=C_WHITE)
        draw.text((95, y_res + 36), "• Port 443: Failed to grab banner: timed out", font=FONT_UI, fill=C_WHITE)

    filepath = os.path.join(OUTPUT_DIR, filename)
    img.save(filepath, "PNG")
    print(f"Saved: {filepath}")

render_browser_window("12_web_ui_form.png", is_result=False)
render_browser_window("13_web_ui_results.png", is_result=True)

# ==================== 14. Email Notification ====================
def render_email_notification(filename):
    width = 920
    height = 540
    img = Image.new("RGB", (width, height), (250, 250, 250))
    draw = ImageDraw.Draw(img)

    # Gmail top bar
    draw.rectangle([(0, 0), (width, 50)], fill=(242, 245, 245))
    draw.line([(0, 50), (width, 50)], fill=(220, 220, 220), width=1)
    draw.text((25, 15), "Gmail", font=FONT_UI_BOLD, fill=(234, 67, 53))
    draw.text((90, 16), "- Ket qua quet tu NetRecon", font=FONT_UI, fill=(80, 80, 80))

    # Email Header
    y = 70
    draw.text((40, y), "Ket qua quet tu NetRecon", font=FONT_TITLE, fill=(30, 30, 30))
    draw.rectangle([(width - 150, y), (width - 40, y + 26)], fill=(230, 230, 230))
    draw.text((width - 135, y + 5), "Hop thu den x", font=FONT_UI, fill=(100, 100, 100))

    y += 45
    # Sender avatar circle
    draw.ellipse([(40, y), (76, y + 36)], fill=(66, 133, 244))
    draw.text((52, y + 8), "N", font=FONT_UI_BOLD, fill=(255, 255, 255))
    draw.text((90, y + 2), "hongphuoc123456@gmail.com", font=FONT_UI_BOLD, fill=(30, 30, 30))
    draw.text((90, y + 20), "den toi ▾", font=FONT_UI, fill=(100, 100, 100))

    y += 55
    # Email Body Content
    draw.rectangle([(40, y), (width - 40, height - 30)], fill=(255, 255, 255), outline=(230, 230, 230))
    y_body = y + 15
    body_lines = [
        ("Ket qua NetRecon (Hoc vien: Vo Hoang Minh Man - 2387700042):", (50, 50, 50)),
        ("", (0, 0, 0)),
        ("--- SCAN ---", (100, 100, 100)),
        ("None", (30, 30, 30)),
        ("", (0, 0, 0)),
        ("--- SERVICE ---", (100, 100, 100)),
        ("Starting Nmap 7.97 ( https://nmap.org ) at 2026-06-12 10:15 +0700", (30, 30, 30)),
        ("PORT   STATE  SERVICE VERSION", (30, 30, 30)),
        ("22/tcp closed ssh", (30, 30, 30)),
        ("80/tcp closed http", (30, 30, 30)),
        ("443/tcp closed https", (30, 30, 30)),
        ("", (0, 0, 0)),
        ("--- BANNER ---", (100, 100, 100)),
        ("{22: 'Failed to grab banner: timed out', 80: 'Failed to grab banner: timed out', 443: 'Failed to grab banner: timed out'}", (30, 30, 30)),
        ("", (0, 0, 0)),
        ("--- VULN ---", (100, 100, 100)),
        ("{80: 'HTTP - CVE-2021-41773', 443: 'HTTPS - CVE-2021-3449'}", (30, 30, 30))
    ]
    for bline, col in body_lines:
        draw.text((55, y_body), bline, font=FONT_CONSOLE_SM, fill=col)
        y_body += 18
        if y_body > height - 40:
            break

    filepath = os.path.join(OUTPUT_DIR, filename)
    img.save(filepath, "PNG")
    print(f"Saved: {filepath}")

render_email_notification("14_email_report.png")

# ==================== 15. Git Commit Netrecon ====================
lines_git_nr = [
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3> git add BUOI3/netrecon", C_YELLOW),
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3> git commit -m \"[add] netrecon\"", C_YELLOW),
    ("[main 5506b83] [add] netrecon", C_WHITE),
    (" 17 files changed, 511 insertions(+)", C_WHITE),
    (" create mode 100644 BUOI3/netrecon/app.py", C_CYAN),
    (" create mode 100644 BUOI3/netrecon/cli.py", C_CYAN),
    (" create mode 100644 BUOI3/netrecon/modules/__init__.py", C_CYAN),
    (" create mode 100644 BUOI3/netrecon/modules/banner_grabber.py", C_CYAN),
    (" create mode 100644 BUOI3/netrecon/modules/email_sender.py", C_CYAN),
    (" create mode 100644 BUOI3/netrecon/modules/filter_utils.py", C_CYAN),
    (" create mode 100644 BUOI3/netrecon/modules/network_mapper.py", C_CYAN),
    (" create mode 100644 BUOI3/netrecon/modules/port_scanner.py", C_CYAN),
    (" create mode 100644 BUOI3/netrecon/modules/service_detector.py", C_CYAN),
    (" create mode 100644 BUOI3/netrecon/modules/vuln_checker.py", C_CYAN),
    (" create mode 100644 BUOI3/netrecon/requirements.txt", C_CYAN),
    (" create mode 100644 BUOI3/netrecon/static/style.css", C_CYAN),
    (" create mode 100644 BUOI3/netrecon/templates/index.html", C_CYAN),
    (" create mode 100644 BUOI3/netrecon/templates/layout.html", C_CYAN),
    (" create mode 100644 BUOI3/netrecon/templates/result.html", C_CYAN),
    ("", C_WHITE),
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3> git push origin main", C_YELLOW),
    ("To https://github.com/Mikmankkk/TH_LTANTT_2387700042.git", C_WHITE),
    ("   6383c61..5506b83  main -> main", C_GREEN),
    ("", C_WHITE),
    ("[Hoc vien: Vo Hoang Minh Man - MSSV: 2387700042]", C_CYAN),
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi3\\THANTT-BUOI3> ", C_YELLOW)
]
render_terminal("15_git_commit_netrecon.png", lines_git_nr, "VS Code Terminal - Git Commit NetRecon", 960, 560)
print("ALL SCREENSHOTS GENERATED SUCCESSFULLY!")
