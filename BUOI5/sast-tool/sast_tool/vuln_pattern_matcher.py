import ast
import re
from .ast_analyzer import issue


class VulnPatternMatcher:
    def __init__(self, patterns=None):
        self.patterns = patterns or []

    def match(self, code):
        results = []
        for node in ast.walk(ast.parse(code)):
            if isinstance(node, (ast.Assign, ast.AnnAssign)):
                targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str) and node.value.value:
                    if any(isinstance(t, ast.Name) and re.search(r'password|secret|api_key', t.id, re.I) for t in targets):
                        results.append(issue(node, 'hardcoded-secret', 'Hardcoded credential; use an environment variable.'))
            if isinstance(node, ast.Import) and any(a.name == 'pickle' for a in node.names):
                results.append(issue(node, 'unsafe-import', 'Review pickle: never deserialize untrusted input.'))
        for pattern in self.patterns:
            for found in re.finditer(pattern['pattern'], code):
                results.append(dict(type=pattern['id'], rule_id=pattern['id'], message=pattern['message'],
                                    lineno=code.count('\n', 0, found.start()) + 1,
                                    col_offset=found.start() - code.rfind('\n', 0, found.start()) - 1))
        return results
