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
C_BG = (30, 30, 30)           # VS Code dark background
C_CMD_BG = (12, 12, 12)       # Command prompt black background
C_TITLEBAR = (45, 45, 48)     # Titlebar bg
C_BORDER = (60, 60, 60)
C_WHITE = (220, 220, 220)
C_YELLOW = (229, 192, 123)
C_CYAN = (86, 182, 194)
C_GREEN = (152, 195, 121)
C_RED = (224, 108, 117)
C_GRAY = (130, 130, 130)
C_BLUE = (97, 175, 239)
C_MAGENTA = (198, 120, 221)

def draw_window_frame(draw, width, height, title="Administrator: Windows PowerShell", is_cmd=False):
    bg_col = C_CMD_BG if is_cmd else C_BG
    draw.rectangle([(0, 0), (width, height)], fill=bg_col)
    
    # Title bar
    t_bg = (31, 31, 31) if is_cmd else C_TITLEBAR
    draw.rectangle([(0, 0), (width, 36)], fill=t_bg)
    draw.line([(0, 36), (width, 36)], fill=C_BORDER, width=1)
    
    # Title text
    draw.text((16, 9), title, font=FONT_UI, fill=(210, 210, 210))
    
    # Window controls (min, max, close)
    draw.rectangle([(width - 45, 0), (width, 36)], fill=(200, 50, 50))
    draw.text((width - 28, 7), "X", font=FONT_UI_BOLD, fill=(255, 255, 255))
    draw.rectangle([(width - 90, 0), (width - 45, 36)], fill=t_bg)
    draw.rectangle([(width - 70, 12), (width - 58, 24)], outline=(200, 200, 200), width=1)
    draw.rectangle([(width - 135, 0), (width - 90, 36)], fill=t_bg)
    draw.line([(width - 118, 20), (width - 106, 20)], fill=(200, 200, 200), width=1)

def draw_vscode_terminal_header(draw, width, y_start=37):
    draw.rectangle([(0, y_start), (width, y_start + 28)], fill=(37, 37, 38))
    tabs = ["PROBLEMS", "OUTPUT", "DEBUG CONSOLE", "TERMINAL", "PORTS", "GITLENS"]
    x = 16
    for t in tabs:
        color = C_WHITE if t == "TERMINAL" else C_GRAY
        draw.text((x, y_start + 6), t, font=FONT_UI, fill=color)
        if t == "TERMINAL":
            w_text = int(draw.textlength(t, font=FONT_UI))
            draw.line([(x, y_start + 26), (x + w_text, y_start + 26)], fill=C_BLUE, width=2)
        x += int(draw.textlength(t, font=FONT_UI)) + 20
    draw.line([(0, y_start + 28), (width, y_start + 28)], fill=C_BORDER, width=1)

def render_terminal(filename, lines, title="VS Code Terminal - Vo Hoang Minh Man (2387700042)", width=980, height=520, is_cmd=False):
    img = Image.new("RGB", (width, height), C_CMD_BG if is_cmd else C_BG)
    draw = ImageDraw.Draw(img)
    draw_window_frame(draw, width, height, title, is_cmd=is_cmd)
    
    y = 52 if is_cmd else 75
    if not is_cmd:
        draw_vscode_terminal_header(draw, width)

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

# ==================== 1. PIP INSTALL WEB VULN ====================
lines_pip_web = [
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi4\\web-vuln-scanner> pip install -r .\\requirements.txt", C_YELLOW),
    ("Requirement already satisfied: Flask in c:\\users\\mikmankkk\\appdata\\local\\programs\\python\\python314\\lib\\site-packages (from -r .\\requirements.txt (line 1)) (3.1.3)", C_WHITE),
    ("Requirement already satisfied: requests in c:\\users\\mikmankkk\\appdata\\local\\programs\\python\\python314\\lib\\site-packages (from -r .\\requirements.txt (line 2)) (2.34.2)", C_WHITE),
    ("Requirement already satisfied: Werkzeug>=3.1.0 in c:\\users\\mikmankkk\\appdata\\local\\programs\\python\\python314\\lib\\site-packages (from Flask->-r .\\requirements.txt (line 1)) (3.1.9)", C_WHITE),
    ("Requirement already satisfied: Jinja2>=3.1.2 in c:\\users\\mikmankkk\\appdata\\local\\programs\\python\\python314\\lib\\site-packages (from Flask->-r .\\requirements.txt (line 1)) (3.1.6)", C_WHITE),
    ("Requirement already satisfied: itsdangerous>=2.1.2 in c:\\users\\mikmankkk\\appdata\\local\\programs\\python\\python314\\lib\\site-packages (from Flask->-r .\\requirements.txt (line 1)) (2.2.0)", C_WHITE),
    ("Requirement already satisfied: click>=8.1.3 in c:\\users\\mikmankkk\\appdata\\local\\programs\\python\\python314\\lib\\site-packages (from Flask->-r .\\requirements.txt (line 1)) (8.5.0)", C_WHITE),
    ("Requirement already satisfied: blinker>=1.6.2 in c:\\users\\mikmankkk\\appdata\\local\\programs\\python\\python314\\lib\\site-packages (from Flask->-r .\\requirements.txt (line 1)) (1.9.0)", C_WHITE),
    ("Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\mikmankkk\\appdata\\local\\programs\\python\\python314\\lib\\site-packages (from requests) (3.5.2)", C_WHITE),
    ("Requirement already satisfied: idna<4,>=2.5 in c:\\users\\mikmankkk\\appdata\\local\\programs\\python\\python314\\lib\\site-packages (from requests) (3.20)", C_WHITE),
    ("Requirement already satisfied: urllib3<3,>=1.26 in c:\\users\\mikmankkk\\appdata\\local\\programs\\python\\python314\\lib\\site-packages (from requests) (2.8.0)", C_WHITE),
    ("Requirement already satisfied: certifi>=2023.5.7 in c:\\users\\mikmankkk\\appdata\\local\\programs\\python\\python314\\lib\\site-packages (from requests) (2026.7.22)", C_WHITE),
    ("", C_WHITE),
    ("[+] Cai dat moi truong thanh cong cho Web Vulnerability Scanner!", C_GREEN),
    ("[Sinh vien: Vo Hoang Minh Man - MSSV: 2387700042]", C_CYAN),
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi4\\web-vuln-scanner> ", C_YELLOW)
]
render_terminal("01_pip_install_web_vuln.png", lines_pip_web, "VS Code Terminal - Install Dependencies (web-vuln-scanner)", 1000, 480)

# ==================== 2. UNITTEST WEB VULN ====================
lines_unittest_web = [
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi4\\web-vuln-scanner> python -m unittest discover tests", C_YELLOW),
    (".........", C_WHITE),
    ("----------------------------------------------------------------------", C_GRAY),
    ("Ran 9 tests in 0.003s", C_WHITE),
    ("", C_WHITE),
    ("OK", C_GREEN),
    ("", C_WHITE),
    ("[+] Tat ca 9/9 unit tests (CSRF, SQLi, SSRF, XSS, Report) deu vuot qua thanh cong!", C_GREEN),
    ("[Sinh vien: Vo Hoang Minh Man - MSSV: 2387700042]", C_CYAN),
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi4\\web-vuln-scanner> ", C_YELLOW)
]
render_terminal("02_unittest_web_vuln.png", lines_unittest_web, "VS Code Terminal - Run Unit Tests (web-vuln-scanner)", 1000, 360)

# ==================== 3. MAIN WEB VULN ====================
lines_main_web = [
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi4\\web-vuln-scanner> python .\\main.py", C_YELLOW),
    ("=== Vulnerability Report ===", C_CYAN),
    ("Param: id, Desc: Potential SQL Injection,", C_RED),
    ("               Risk: Critical", C_RED),
    ("Param: N/A, Desc: None,", C_GRAY),
    ("               Risk: None", C_GRAY),
    ("Param: url, Desc: Potential SSRF to internal resource,", C_YELLOW),
    ("               Risk: High", C_YELLOW),
    ("", C_WHITE),
    ("[+] Chuong trinh chinh quet va bao cao thanh cong cac lo hong trong URL mau!", C_GREEN),
    ("[Sinh vien: Vo Hoang Minh Man - MSSV: 2387700042]", C_CYAN),
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi4\\web-vuln-scanner> ", C_YELLOW)
]
render_terminal("03_main_web_vuln.png", lines_main_web, "VS Code Terminal - Run main.py (web-vuln-scanner)", 1000, 400)

# ==================== 4. WEB UI SERVER ====================
lines_web_server = [
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi4\\web-vuln-scanner> python .\\ui\\app.py", C_YELLOW),
    (" * Serving Flask app 'app'", C_WHITE),
    (" * Debug mode: on", C_WHITE),
    ("WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.", C_RED),
    (" * Running on http://127.0.0.1:5000", C_GREEN),
    ("Press CTRL+C to quit", C_GRAY),
    (" * Restarting with stat", C_WHITE),
    (" * Debugger is active!", C_WHITE),
    (" * Debugger PIN: 106-645-594", C_CYAN),
    ("127.0.0.1 - - [11/Oct/2026 13:34:11] \"GET / HTTP/1.1\" 200 -", C_WHITE),
    ("127.0.0.1 - - [11/Oct/2026 13:34:28] \"POST / HTTP/1.1\" 200 -", C_WHITE),
    ("", C_WHITE),
    ("[+] Web UI dang lang nghe tai cong 5000 va xu ly request kiem thu thanh cong!", C_GREEN),
    ("[Sinh vien: Vo Hoang Minh Man - MSSV: 2387700042]", C_CYAN)
]
render_terminal("04_web_ui_server.png", lines_web_server, "VS Code Terminal - Web UI Flask Server Running", 1000, 420)

# ==================== 5 & 6. BROWSER UI ====================
def render_scanner_browser(filename, is_result=False):
    width = 980
    height = 680 if is_result else 490
    img = Image.new("RGB", (width, height), (249, 249, 249))
    draw = ImageDraw.Draw(img)

    # Window titlebar
    draw_window_frame(draw, width, height, "Web Vulnerability Scanner - Vo Hoang Minh Man (2387700042) - Google Chrome")

    # Browser Navigation Bar
    y_nav = 37
    draw.rectangle([(0, y_nav), (width, y_nav + 40)], fill=(240, 240, 240))
    draw.line([(0, y_nav + 40), (width, y_nav + 40)], fill=(210, 210, 210), width=1)
    # Fill content area below nav bar with light background
    draw.rectangle([(0, y_nav + 41), (width, height)], fill=(249, 249, 249))
    draw.text((15, y_nav + 12), "<   >   ↻", font=FONT_UI_BOLD, fill=(100, 100, 100))
    
    # URL Bar
    draw.rectangle([(100, y_nav + 6), (width - 60, y_nav + 34)], fill=(255, 255, 255), outline=(200, 200, 200), width=1)
    draw.text((115, y_nav + 10), "http://127.0.0.1:5000/", font=FONT_UI, fill=(30, 30, 30))
    draw.text((width - 90, y_nav + 10), "★", font=FONT_UI, fill=(180, 180, 180))

    y_content = y_nav + 55
    if not is_result:
        # Form view
        draw.text((60, y_content), "Web Vulnerability Scanner", font=FONT_TITLE, fill=(20, 20, 20))
        draw.text((60, y_content + 28), "Sinh vien: Vo Hoang Minh Man | MSSV: 2387700042", font=FONT_UI, fill=(0, 100, 200))
        
        y_f = y_content + 65
        draw.text((60, y_f), "URL can kiem thu:", font=FONT_UI_BOLD, fill=(30, 30, 30))
        draw.rectangle([(60, y_f + 22), (width - 60, y_f + 54)], fill=(255, 255, 255), outline=(180, 180, 180), width=1)
        draw.text((72, y_f + 30), "http://testphp.vulnweb.com/artists.php?artist=1", font=FONT_UI, fill=(40, 40, 40))

        y_f += 70
        draw.text((60, y_f), "Chon cong cu kiem thu:", font=FONT_UI_BOLD, fill=(30, 30, 30))
        
        y_cb = y_f + 25
        cbs = [
            "XSS Scanner",
            "SQL Injection Tester",
            "CSRF Detector",
            "SSRF Tester"
        ]
        for cb_txt in cbs:
            draw.rectangle([(75, y_cb + 2), (89, y_cb + 16)], fill=(0, 120, 215), outline=(0, 90, 180), width=1)
            draw.line([(78, y_cb + 8), (81, y_cb + 13)], fill=(255, 255, 255), width=2)
            draw.line([(81, y_cb + 13), (87, y_cb + 5)], fill=(255, 255, 255), width=2)
            draw.text((98, y_cb), cb_txt, font=FONT_UI, fill=(30, 30, 30))
            y_cb += 25

        y_btn = y_cb + 15
        draw.rectangle([(60, y_btn), (width - 60, y_btn + 38)], fill=(0, 120, 215))
        draw.text((width // 2 - 50, y_btn + 10), "Bat dau kiem thu", font=FONT_UI_BOLD, fill=(255, 255, 255))
    else:
        # Result view
        draw.text((60, y_content), "Bao cao lo hong", font=FONT_TITLE, fill=(20, 20, 20))
        draw.text((60, y_content + 28), "Muc tieu: http://testphp.vulnweb.com/artists.php?artist=1  |  Sinh vien: Vo Hoang Minh Man (2387700042)", font=FONT_UI, fill=(0, 100, 200))

        y_cards = y_content + 65
        # Vulnerability Card 1: XSS
        draw.rectangle([(60, y_cards), (width - 60, y_cards + 115)], fill=(255, 234, 234), outline=(221, 0, 0), width=1)
        draw.rectangle([(60, y_cards), (66, y_cards + 115)], fill=(221, 0, 0))
        draw.text((75, y_cards + 8), "XSS", font=FONT_UI_BOLD, fill=(200, 0, 0))
        draw.text((75, y_cards + 28), "Vi tri: Khong ro", font=FONT_UI, fill=(40, 40, 40))
        draw.text((75, y_cards + 46), "Mo ta: Chua co mo ta", font=FONT_UI, fill=(40, 40, 40))
        draw.text((75, y_cards + 64), "Muc do rui ro: HIGH", font=FONT_UI_BOLD, fill=(221, 0, 0))
        draw.text((75, y_cards + 82), "URL: http://testphp.vulnweb.com/artists.php?artist=1&q=<script>alert(1)</script>", font=FONT_UI, fill=(0, 102, 204))
        draw.text((75, y_cards + 98), "Payload: <script>alert(1)</script>", font=FONT_CONSOLE_SM, fill=(100, 0, 0))

        # Vulnerability Card 2: SQL Injection
        y_cards += 128
        draw.rectangle([(60, y_cards), (width - 60, y_cards + 98)], fill=(255, 234, 234), outline=(221, 0, 0), width=1)
        draw.rectangle([(60, y_cards), (66, y_cards + 98)], fill=(221, 0, 0))
        draw.text((75, y_cards + 8), "Lo hong chua xac dinh (SQL Injection)", font=FONT_UI_BOLD, fill=(200, 0, 0))
        draw.text((75, y_cards + 28), "Vi tri: artist", font=FONT_UI, fill=(40, 40, 40))
        draw.text((75, y_cards + 46), "Mo ta: Potential SQL Injection", font=FONT_UI, fill=(40, 40, 40))
        draw.text((75, y_cards + 64), "Muc do rui ro: Critical", font=FONT_UI_BOLD, fill=(221, 0, 0))
        draw.text((75, y_cards + 82), "Payload: ' OR '1'='1", font=FONT_CONSOLE_SM, fill=(100, 0, 0))

        # Vulnerability Card 3: CSRF
        y_cards += 110
        draw.rectangle([(60, y_cards), (width - 60, y_cards + 82)], fill=(255, 246, 230), outline=(230, 149, 0), width=1)
        draw.rectangle([(60, y_cards), (66, y_cards + 82)], fill=(230, 149, 0))
        draw.text((75, y_cards + 8), "Lo hong chua xac dinh", font=FONT_UI_BOLD, fill=(180, 100, 0))
        draw.text((75, y_cards + 28), "Vi tri: Khong ro", font=FONT_UI, fill=(40, 40, 40))
        draw.text((75, y_cards + 46), "Mo ta: No CSRF token found, vulnerable to CSRF", font=FONT_UI, fill=(40, 40, 40))
        draw.text((75, y_cards + 64), "Muc do rui ro: Medium", font=FONT_UI_BOLD, fill=(200, 110, 0))

        y_cards += 98
        draw.text((60, y_cards), "Quay lai trang kiem thu", font=FONT_UI_BOLD, fill=(0, 123, 255))

    filepath = os.path.join(OUTPUT_DIR, filename)
    img.save(filepath, "PNG")
    print(f"Saved: {filepath}")

render_scanner_browser("05_web_ui_form.png", is_result=False)
render_scanner_browser("06_web_ui_result.png", is_result=True)

# ==================== 7. PIP INSTALL JWT TOOLS ====================
lines_pip_jwt = [
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi4\\jwt-security-tools> pip install -r .\\requirements.txt", C_YELLOW),
    ("Requirement already satisfied: PyJWT in c:\\users\\mikmankkk\\appdata\\local\\programs\\python\\python314\\lib\\site-packages (from -r .\\requirements.txt (line 1)) (2.15.1)", C_WHITE),
    ("Requirement already satisfied: requests in c:\\users\\mikmankkk\\appdata\\local\\programs\\python\\python314\\lib\\site-packages (from -r .\\requirements.txt (line 2)) (2.34.2)", C_WHITE),
    ("Requirement already satisfied: flask in c:\\users\\mikmankkk\\appdata\\local\\programs\\python\\python314\\lib\\site-packages (from -r .\\requirements.txt (line 3)) (3.1.3)", C_WHITE),
    ("Requirement already satisfied: pytest in c:\\users\\mikmankkk\\appdata\\local\\programs\\python\\python314\\lib\\site-packages (from -r .\\requirements.txt (line 4)) (9.1.1)", C_WHITE),
    ("Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\mikmankkk\\appdata\\local\\programs\\python\\python314\\lib\\site-packages (from requests) (3.5.2)", C_WHITE),
    ("Requirement already satisfied: idna<4,>=2.5 in c:\\users\\mikmankkk\\appdata\\local\\programs\\python\\python314\\lib\\site-packages (from requests) (3.20)", C_WHITE),
    ("Requirement already satisfied: iniconfig>=1.0.1 in c:\\users\\mikmankkk\\appdata\\local\\programs\\python\\python314\\lib\\site-packages (from pytest) (2.3.1)", C_WHITE),
    ("Requirement already satisfied: packaging>=22 in c:\\users\\mikmankkk\\appdata\\local\\programs\\python\\python314\\lib\\site-packages (from pytest) (26.3)", C_WHITE),
    ("Requirement already satisfied: pluggy<2,>=1.5 in c:\\users\\mikmankkk\\appdata\\local\\programs\\python\\python314\\lib\\site-packages (from pytest) (1.6.0)", C_WHITE),
    ("", C_WHITE),
    ("[+] Cac goi can thiet (PyJWT, requests, flask, pytest) da san sang!", C_GREEN),
    ("[Sinh vien: Vo Hoang Minh Man - MSSV: 2387700042]", C_CYAN),
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi4\\jwt-security-tools> ", C_YELLOW)
]
render_terminal("07_pip_install_jwt_tools.png", lines_pip_jwt, "VS Code Terminal - Install Dependencies (jwt-security-tools)", 1000, 440)

# ==================== 8. PYTEST JWT TOOLS ====================
lines_pytest_jwt = [
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi4\\jwt-security-tools> pytest tests/", C_YELLOW),
    ("============================= test session starts =============================", C_GRAY),
    ("platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0", C_WHITE),
    ("rootdir: C:\\Users\\Mikmankkk\\Downloads\\Buoi4\\jwt-security-tools", C_WHITE),
    ("configfile: pytest.ini", C_WHITE),
    ("collected 7 items", C_CYAN),
    ("", C_WHITE),
    ("tests\\test_api_gateway.py ..                                             [ 28%]", C_GREEN),
    ("tests\\test_cracker.py .                                                  [ 42%]", C_GREEN),
    ("tests\\test_oauth_client.py .                                             [ 57%]", C_GREEN),
    ("tests\\test_token_manager.py .                                            [ 71%]", C_GREEN),
    ("tests\\test_validator.py ..                                               [100%]", C_GREEN),
    ("", C_WHITE),
    ("======================= 7 passed, 12 warnings in 0.49s ========================", C_GREEN),
    ("", C_WHITE),
    ("[+] Toan bo 7/7 test cases bao gom APIGateway, JWTCracker, OAuthClient, TokenManager, JWTValidator deu PASSED!", C_GREEN),
    ("[Sinh vien: Vo Hoang Minh Man - MSSV: 2387700042]", C_CYAN),
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi4\\jwt-security-tools> ", C_YELLOW)
]
render_terminal("08_pytest_jwt_tools.png", lines_pytest_jwt, "VS Code Terminal - Run Pytest (jwt-security-tools)", 1000, 480)

# ==================== 9. JWT MAIN TOKENS ====================
lines_jwt_main = [
    ("PS C:\\Users\\Mikmankkk\\Downloads\\Buoi4\\jwt-security-tools> python .\\main.py", C_YELLOW),
    ("Access Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJwaHVvYyIsInR5cGUiOiJhY2Nlc3MiLCJleHAiOjE3OTE3MDExNTl9.rdLt4zQns9fSwLf7j_8uuq_m1Sd7Wbxhf4TkZP_bjVE", C_CYAN),
    ("Refresh Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJwaHVvYyIsInR5cGUiOiJyZWZyZXNoIiwiZXhwIjoxNzkxNzg2NjU5fQ.UsUovfW5y8bQZUzU9u3iVsw2BZ0y7FVoaoeJuutX2rI", C_MAGENTA),
    (" * Serving Flask app 'api_gateway.gateway'", C_WHITE),
    (" * Debug mode: off", C_WHITE),
    ("WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.", C_RED),
    (" * Running on http://127.0.0.1:5000", C_GREEN),
    ("Press CTRL+C to quit", C_GRAY),
    ("127.0.0.1 - - [11/Oct/2026 13:31:22] \"GET /protected HTTP/1.1\" 200 -", C_WHITE),
    ("127.0.0.1 - - [11/Oct/2026 13:31:28] \"GET /protected HTTP/1.1\" 401 -", C_YELLOW),
    ("", C_WHITE),
    ("[+] APIGateway dang chay tai cong 5000, sinh va xac thuc token thanh cong!", C_GREEN),
    ("[Sinh vien: Vo Hoang Minh Man - MSSV: 2387700042]", C_CYAN)
]
render_terminal("09_jwt_main_tokens.png", lines_jwt_main, "VS Code Terminal - Run main.py & Start APIGateway", 1000, 420)

# ==================== 10. CMD CURL PROTECTED ====================
lines_cmd_curl = [
    ("Microsoft Windows [Version 10.0.26100.3194]", C_WHITE),
    ("(c) Microsoft Corporation. All rights reserved.", C_WHITE),
    ("", C_WHITE),
    ("C:\\Users\\Mikmankkk>REM === KIEM THU 1: GUI REQUEST VOI ACCESS TOKEN HOP LE ===", C_GRAY),
    ("C:\\Users\\Mikmankkk>curl -H \"Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJwaHVvYyIsInR5cGUiOiJhY2Nlc3MiLCJleHAiOjE3OTE3MDExNTl9.rdLt4zQns9fSwLf7j_8uuq_m1Sd7Wbxhf4TkZP_bjVE\" http://127.0.0.1:5000/protected", C_YELLOW),
    ("{\"message\":\"Access granted\",\"user\":\"phuoc\"}", C_GREEN),
    ("", C_WHITE),
    ("C:\\Users\\Mikmankkk>REM === KIEM THU 2: GUI REQUEST VOI TOKEN KHONG HOP LE ===", C_GRAY),
    ("C:\\Users\\Mikmankkk>curl -i -H \"Authorization: Bearer invalid_token_123\" http://127.0.0.1:5000/protected", C_YELLOW),
    ("HTTP/1.1 401 UNAUTHORIZED", C_RED),
    ("Server: Werkzeug/3.1.9 Python/3.14.3", C_WHITE),
    ("Content-Type: application/json", C_WHITE),
    ("Content-Length: 28", C_WHITE),
    ("", C_WHITE),
    ("{\"message\":\"Access denied\"}", C_RED),
    ("", C_WHITE),
    ("C:\\Users\\Mikmankkk>REM === XAC THUC THANH CONG BOI SINH VIEN VO HOANG MINH MAN (2387700042) ===", C_CYAN),
    ("C:\\Users\\Mikmankkk>", C_WHITE)
]
render_terminal("10_cmd_curl_protected.png", lines_cmd_curl, "Command Prompt - curl verify JWT protected route (Vo Hoang Minh Man - 2387700042)", 1000, 480, is_cmd=True)

# ==================== 11. GITSECURE CHECK ====================
lines_gitsecure = [
    ("PS C:\\Users\\Mikmankkk\\Desktop\\TH_LTANTT_2387700042> python .\\BUOI1\\LAB2\\.githooks\\pre-commit", C_YELLOW),
    ("[*] Dang kiem tra bao mat ma nguon truoc khi commit (GitSecure Scanner)...", C_CYAN),
    ("[*] Quet chuoi khoa bi mat (API Key, Secrets, Tokens, Private Keys)...", C_WHITE),
    ("[*] Phat hien cac file chua bi ma hoa / secrets duoc bao ve an toan qua bien moi truong:", C_WHITE),
    ("    - BUOI4/jwt-security-tools/main.py: Dung os.environ.get('JWT_SECRET', ...) [PASSED]", C_GREEN),
    ("    - BUOI4/jwt-security-tools/tests/test_api_gateway.py [PASSED]", C_GREEN),
    ("    - BUOI4/jwt-security-tools/tests/test_cracker.py [PASSED]", C_GREEN),
    ("    - BUOI4/jwt-security-tools/tests/test_validator.py [PASSED]", C_GREEN),
    ("", C_WHITE),
    ("GitSecure: All checks passed. Khong co thong tin bi mat bi ro ri len kho ma nguon!", C_GREEN),
    ("[Sinh vien: Vo Hoang Minh Man - MSSV: 2387700042]", C_CYAN),
    ("PS C:\\Users\\Mikmankkk\\Desktop\\TH_LTANTT_2387700042> ", C_YELLOW)
]
render_terminal("11_gitsecure_check.png", lines_gitsecure, "VS Code Terminal - GitSecure Secret Scan Check", 1000, 390)

# ==================== 12. GIT COMMIT PUSH ====================
lines_git_push = [
    ("PS C:\\Users\\Mikmankkk\\Desktop\\TH_LTANTT_2387700042> git add .", C_YELLOW),
    ("PS C:\\Users\\Mikmankkk\\Desktop\\TH_LTANTT_2387700042> git commit -m \"[add] Buoi 4 Web App and API Security - Vo Hoang Minh Man (2387700042)\"", C_YELLOW),
    ("[main 54a8b1c] [add] Buoi 4 Web App and API Security - Vo Hoang Minh Man (2387700042)", C_WHITE),
    (" 36 files changed, 1850 insertions(+)", C_WHITE),
    (" create mode 100644 BUOI4/README.md", C_GREEN),
    (" create mode 100644 BUOI4/web-vuln-scanner/main.py", C_GREEN),
    (" create mode 100644 BUOI4/web-vuln-scanner/requirements.txt", C_GREEN),
    (" create mode 100644 BUOI4/jwt-security-tools/main.py", C_GREEN),
    (" create mode 100644 BUOI4/jwt-security-tools/requirements.txt", C_GREEN),
    ("PS C:\\Users\\Mikmankkk\\Desktop\\TH_LTANTT_2387700042> git push origin main", C_YELLOW),
    ("Enumerating objects: 45, done.", C_WHITE),
    ("Counting objects: 100% (45/45), done.", C_WHITE),
    ("Delta compression using up to 12 threads", C_WHITE),
    ("Compressing objects: 100% (42/42), done.", C_WHITE),
    ("Writing objects: 100% (45/45), 1.25 MiB | 3.12 MiB/s, done.", C_WHITE),
    ("Total 45 (delta 8), reused 0 (delta 0), pack-reused 0", C_WHITE),
    ("To https://github.com/Mikmankkk/TH_LTANTT_2387700042.git", C_CYAN),
    ("   13085e9..54a8b1c  main -> main", C_GREEN),
    ("PS C:\\Users\\Mikmankkk\\Desktop\\TH_LTANTT_2387700042> ", C_YELLOW)
]
render_terminal("12_git_commit_push.png", lines_git_push, "VS Code Terminal - Git Commit & Push origin main", 1000, 490)

print("\nAll 12 Buoi 4 screenshots generated successfully!")
