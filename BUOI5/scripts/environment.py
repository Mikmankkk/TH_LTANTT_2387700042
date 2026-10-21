import datetime
import importlib.metadata
import json
import os
import platform
import sys
from pathlib import Path

info = dict(student='VO HOANG MINH MAN', mssv='2387700042',
            timestamp=datetime.datetime.now().astimezone().isoformat(),
            computer=platform.node(), windows=platform.platform(), python=sys.version,
            executable=sys.executable, cwd=os.getcwd(),
            packages={p: importlib.metadata.version(p) for p in ('Flask', 'psutil', 'pytest', 'jsonschema')})
text = json.dumps(info, indent=2)
print(text)
(Path(__file__).resolve().parents[1] / 'reports/environment.json').write_text(text, encoding='utf-8')
