import subprocess
import tempfile
from pathlib import Path


class VirtualSandbox:
    """Restricted lab runner, not OS isolation. Only supports a harmless echo demo."""
    def run_isolated(self, command, timeout=3):
        if not isinstance(command, str) or not command.startswith('echo ') or len(command) > 160:
            raise ValueError('Only echo <text> is supported by the lab runner')
        text = command[5:]
        if not text or any(c in text for c in '&|<>^%\r\n'):
            raise ValueError('Shell metacharacters are not allowed')
        import sys
        with tempfile.TemporaryDirectory(prefix='buoi5-') as directory:
            script = Path(directory) / 'demo.py'
            script.write_text('import sys\nprint(sys.argv[1])\n', encoding='utf-8')
            result = subprocess.run([sys.executable, '-I', str(script), text], cwd=directory,
                                    capture_output=True, text=True, timeout=timeout, shell=False)
            return result.stdout, result.stderr
