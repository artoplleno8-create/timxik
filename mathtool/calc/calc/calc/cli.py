import argparse

from calc import series as series_mod
from calc import integration as integration_mod

def build_parser():
    parser= argparse.ArgumentParser(
        prog='mathtool',
        description="mathtool-расчеты над уравнениями"
                    'и числовыми последовательностями',
        allow_abbrev=False,            
    )

    subs= parser.add_subparsers(dest='command')

    
    p_solve=subs.add_parser(
        'solve', help='решение уравнения', allow_abbrev=False,
    )
    p_solve.add_argument('-a', type=int, help='коэффициент A')
    p_solve.add_argument('-b', type=int, help='коэффициент B')
    p_solve.add_argument('-c', type=int, help='коэффициент C')
    p_stats=subs.add_parser(
        'stats', help='показатели последовательности', allow_abbrev=False
    )
    p_stats.add_argument('--input', help='имя файла с числами')

    p_series=subs.add_parser(
        'series', help='сумма ряда', allow_abbrev=False
    )
    p_series.add_argument(
        '--func', required=True,
        choices=sorted(series_mod.FORMULAS),
        help='какой ряд суммировать',
    )
    group=p_series.add_mutually_exclusive_group(required=True)
    group.add_argument('--terms', type=int,
                       help='сколько слагаемых сложить')
    group.add_argument('--eps', type=float,
                       help='до какой величины слагаемого считать')

    p=int=subs.add_parser(
        'integrate', help='численное интегрирование', allow_abbrev=False
    )
    p=int.add_argument(
        '--func', required=True,
        choices=sorted(integration_mod.FUNCTION),\
        help='какую функцию интегрировать',
    )
    p=int.add_argument('--from', dest='start', type=float, required=True,
                       help='нижний предел интегрирования')
    p=int.add_argument('--to', type=float, required=True,
                       help='верхний предел интегрирования')
    p=int.add_argument('--steps', type=float, required=True,
                       help='число прямоугольников')

    return parser