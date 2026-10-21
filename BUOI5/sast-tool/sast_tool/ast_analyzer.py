import ast


def issue(node, rule, message):
    return dict(type=rule, rule_id=rule, message=message,
                lineno=node.lineno, col_offset=node.col_offset)


class ASTAnalyzer:
    def analyze(self, code):
        tree = ast.parse(code)
        aliases = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                aliases.update({a.asname or a.name: a.name for a in node.names})
            elif isinstance(node, ast.ImportFrom):
                aliases.update({a.asname or a.name: f'{node.module}.{a.name}' for a in node.names})
        results = []
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            name = ast.unparse(node.func)
            first, *rest = name.split('.')
            name = '.'.join([aliases.get(first, first), *rest])
            if name in ('eval', 'exec', 'builtins.eval', 'builtins.exec', 'os.system', 'pickle.loads', 'pickle.load'):
                results.append(issue(node, 'dangerous-call', f'Potentially unsafe call: {name}'))
            if name in ('subprocess.run', 'subprocess.Popen', 'subprocess.call'):
                if any(k.arg == 'shell' and isinstance(k.value, ast.Constant) and k.value.value is True for k in node.keywords):
                    results.append(issue(node, 'shell-true', 'Subprocess executes through a shell.'))
        return results
