import ast
from pathlib import Path
from .ast_analyzer import issue


class CodeQualityChecker:
    def metrics(self, code):
        tree = ast.parse(code)
        functions = []
        for f in ast.walk(tree):
            if isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef)):
                nodes = list(ast.walk(f))
                complexity = 1 + sum(isinstance(n, (ast.If, ast.For, ast.AsyncFor, ast.While, ast.ExceptHandler, ast.IfExp)) for n in nodes)
                complexity += sum(len(n.values) - 1 for n in nodes if isinstance(n, ast.BoolOp))
                def depth(node, level=0):
                    branch = isinstance(node, (ast.If, ast.For, ast.While, ast.Try, ast.With))
                    level += int(branch)
                    return max([level] + [depth(c, level) for c in ast.iter_child_nodes(node)])
                functions.append(dict(name=f.name, line=f.lineno, length=f.end_lineno-f.lineno+1,
                                      complexity=complexity, nesting=depth(f)))
        return dict(functions=functions, dependencies=sum(isinstance(n, (ast.Import, ast.ImportFrom)) for n in ast.walk(tree)))

    def check(self, filepath):
        metrics = self.metrics(Path(filepath).read_text(encoding='utf-8'))
        return [dict(type='code-quality', rule_id='code-quality', lineno=f['line'], col_offset=0,
                     message=f"Function {f['name']}: complexity={f['complexity']}, length={f['length']}, nesting={f['nesting']}")
                for f in metrics['functions'] if f['complexity'] > 10 or f['length'] > 50 or f['nesting'] > 4]
