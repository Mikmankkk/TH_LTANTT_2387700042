import sys
import threading
from collections import deque


class SecurityBehaviorChecker:
    """Observe actual Python audit events; installing a hook is explicit."""
    def __init__(self):
        self.events = deque(maxlen=200)
        self.active = False
        self.thread_id = None
        self._installed = False

    def start(self):
        self.active = True
        self.thread_id = threading.get_ident()
        if not self._installed:
            sys.addaudithook(self._hook)
            self._installed = True
        return self

    def stop(self):
        self.active = False

    def _hook(self, event, args):
        if self.active and threading.get_ident() == self.thread_id and event in ('exec', 'os.system', 'subprocess.Popen', 'socket.connect'):
            self.events.append({'event': event, 'message': 'Observed runtime event; context review required.'})

    def suspicious_calls(self):
        return list(self.events)
