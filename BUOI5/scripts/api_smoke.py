"""Start the real loopback HTTP server, call every endpoint, then stop it."""
import json
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def request(path, data=None):
    payload = None if data is None else json.dumps(data).encode()
    req = urllib.request.Request('http://127.0.0.1:5000' + path, data=payload,
                                 headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            return response.status, json.load(response)
    except urllib.error.HTTPError as exc:
        return exc.code, json.load(exc)


def main():
    (ROOT / 'reports').mkdir(exist_ok=True)
    # Refuse to test an unrelated service already occupying the lab port.
    import socket
    with socket.socket() as probe:
        if probe.connect_ex(('127.0.0.1', 5000)) == 0:
            raise RuntimeError('Port 5000 is occupied; stop the existing service first')
    with (ROOT / 'reports/api-server.log').open('w', encoding='utf-8') as log:
        server = subprocess.Popen([sys.executable, '-u', 'app.py'], cwd=ROOT / 'dast-tool', stdout=log, stderr=log)
        try:
            for _ in range(60):
                if server.poll() is not None:
                    raise RuntimeError('Flask server failed to start; inspect api-server.log')
                try:
                    request('/api/monitor')
                    break
                except (OSError, urllib.error.URLError):
                    time.sleep(0.2)
            else:
                raise TimeoutError('Flask startup timed out')
            results = []
            cases = [('/api/monitor', None, 200), ('/api/memory', None, 200), ('/api/network', None, 200),
                     ('/api/sandbox', {'command': 'echo Hello Sandbox API'}, 200), ('/api/security', None, 200),
                     ('/api/sandbox', {'command': 'echo x & whoami'}, 400), ('/api/sandbox', {}, 400)]
            for endpoint, data, expected in cases:
                status, body = request(endpoint, data)
                assert status == expected, (endpoint, status, body)
                if endpoint == '/api/sandbox' and expected == 200:
                    assert body['stdout'].strip() == 'Hello Sandbox API'
                if endpoint == '/api/security':
                    assert any(e['event'] == 'subprocess.Popen' for e in body['suspicious_calls'])
                print(f'{"GET" if data is None else "POST"} {endpoint}: HTTP {status} PASS')
                print(json.dumps(body)[:180])
                results.append(dict(endpoint=endpoint, request=data, status=status, body=body))
            (ROOT / 'reports/api-results.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
            print(f'REAL HTTP: {len(results)}/{len(cases)} checks passed; server PID={server.pid}')
        finally:
            server.terminate()
            server.wait(timeout=10)


if __name__ == '__main__':
    main()
