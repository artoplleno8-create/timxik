import sys

from cli import build_parser
from calc import equation, stats, series, integration

def handle_solve(args):
    if args.a is None and args.b is None and args.c is None:
            try:
                a=int(input('Введите A:'))
                b=int(input('Введите B:'))
                c=int(input('Введите C:'))
            except ValueError:
                 raise ValueError('коэффициент не является целым числом')
    elif args.a is None or args.b is None or args.c is None:
         raise ValueError('укажите все три коэффициента либо ни одного')
    else:
         a,b,c=args.a, args.b, args.c
    equation.validate_coefficients({'A':a,'B':b,'C':c})
    kind,d,roots=equation.solve(a,b,c)
    print(f'Уравнение {kind}')
    if d is None:
         print(f'x={roots[0]:.3f}')
    else:
         print(f'Дискриминант: {d}')
         if len(roots)==2:
              print(f'x1={roots[0]:.3f}')
              print(f'x2={roots[1]:.3f}')
         elif len(roots)==1:
              print(f'x={roots[0]:.3f}')
         else:
              print('Действительных корней нет')
    return 0

def _read_numbers(args):
     if args.input:
          with open(args.input, encoding='utf-8-sig') as handle:
               lines=handle.readlines()
     else:
          lines=sys.stdin.readlines()

     values=[]
     for line in lines:
          for word in line.split():
               try:
                    values.append(float(word))
               except ValueError:
                    raise ValueError(f'{word} не является числом')
     return values

def handle_stats(args):
     values=_read_numbers(args)
     stats.validate(values)

     for label, func, form in stats.REPORT:
          value= func(values)
          if value is None:
               print(f'{label}: НЕ СУЩЕСТВУЕТ')
          else:
               print(f'{label}:{value:{form}}')
     return 0

def handle_series(args):
     term, formula= series.FORMULAS[args.func]

     if args.terms is not None:
          series.validate_terms(args.terms)
          print(formula)
          result= series.sum_by_terms(term, args.terms)
          print(f'Слагаемых: {args.terms}')
     else:
          series.validate_eps(args.eps)
          print(formula)
          result, count= series.sum_by_eps(term, args.eps)
          print(f'Слагаемых: {count}')

     print(f'Сумма ряда: {result:.4f}')
     return 0

def handle_integrate(args):
     func, formula, low, high, inclusive= integration.FUNCTION[args.func]
     integration.validate_bounds(args.start, args.to, low, high, inclusive)
     integration.validate_steps(args.steps)

     print(formula)
     value= integration.integrate(func, args.start, args.to, args.steps)
     print(f'Значение интеграла: {value:.4f}')
     return 0

HANDLERS={
     'solve': handle_solve,
     'stats': handle_stats,
     'series': handle_series,
     'integrate': handle_integrate,
}

def main(argv):
     parser= build_parser()
     args= parser.parse_args(argv)

     if args.command is None:
          parser.print_help()
          return 0

     try:
          return HANDLERS[args.command](args)
     except (ValueError, OSError) as error:
          print(f'Ошибка: {error}', file=sys.stderr)
          return 1




if __name__=='__main__':
     sys.exit(main(sys.argv[1:]))
