import argparse
import json
from pathlib import Path
from .ast_analyzer import ASTAnalyzer
from .vuln_pattern_matcher import VulnPatternMatcher
from .security_rule_engine import SecurityRuleEngine
from .code_quality_checker import CodeQualityChecker
from .sarif_reporter import SarifReporter


def main():
    parser = argparse.ArgumentParser(description='Analyze Python without executing it')
    parser.add_argument('file')
    parser.add_argument('-o', '--output', default='report.sarif')
    parser.add_argument('--rules')
    args = parser.parse_args()
    try:
        code = Path(args.file).read_text(encoding='utf-8')
        quality = CodeQualityChecker()
        issues = SecurityRuleEngine(args.rules).evaluate(ASTAnalyzer().analyze(code), VulnPatternMatcher().match(code), quality.check(args.file))
        SarifReporter().generate_report(issues, args.output, args.file)
        print(json.dumps({'file': args.file, 'issues': issues, 'metrics': quality.metrics(code)}, indent=2))
        print(f'SARIF saved: {args.output}; findings: {len(issues)}')
    except (OSError, SyntaxError, ValueError) as exc:
        parser.exit(2, f'Analysis failed: {exc}\n')


if __name__ == '__main__':
    main()
