import sys
# модуль для работы с системными функциями
import math
# модуль математических функций

def print_help():
# печатает пользователю инструкцию: какие бывают режимы запуска
    # Вывести справку по использованию программы.
    # строка документации
    print('Использование:')
    print('python mathtool.py                       — показать эту справку')
    print('python mathtool.py --help                — показать эту справку')
    print('python mathtool.py solve                 — ввести A, B, C с клавиатуры')
    print('python mathtool.py solve -a A -b B -c C  — задать A, B, C параметрами')
    print()
    print('Программа решает уравнение A·x² + B·x + C = 0.')
    print('Коэффициенты — целые числа в диапазоне [-10000, 10000].') 

def parse_args(argv):
    # эта функция разбирает аргументы командной строки и определяет режим работы. На вход получает argv — список аргументов без имени скрипта
    if len(argv)==0 or argv[0]=='--help':
        # len(argv) == 0 — ничего не передано - справка
        # argv[0] == '--help' — пользователь явно попросил помощь - справка
        return('help',None)

    if argv[0]!='solve':
        # argv[0] != 'solve' — первое слово не команда solve - ошибка + выход с кодом 1
        print('ОШИБКА: неизвестная команда',file=sys.stderr)
        sys.exit(1)

    if len(argv)==1:
        # len(argv) == 1 — передали только solve -  интерактивный режим
        return('interactive',None)

    elif len(argv)==7:
        # len(argv) == 7 — ожидается шаблон solve -a A -b B -c C, то есть 7 элементов, Проверяются позиции argv[1], argv[3], argv[5] — должны быть -a, -b, -c.
        # возвращаются значения argv[2], argv[4], argv[6] — сами коэффициенты (как строки)
        if argv[1]!='-a' or argv[3]!='-b' or argv[5]!='-c':
            print('ОШИБКА: неизвестный параметр',file=sys.stderr)
            sys.exit(1)
        return('params',(argv[2],argv[4],argv[6]))

    else:
        print('ОШИБКА: неверный набор параметров',file=sys.stderr) #поток ошибок
        sys.exit(1)

def to_int(raw,name):
    # raw-преобразование строки в целое число
    try:
        return int(raw)
    # если int(raw) сработал — возвращаем число
    except ValueError:
        # except — обработка ошибок
        print(f'ОШИБКА: коэффициент {name} не является целым числом',file=sys.stderr)
        # параметр name позволяет вывести понятное сообщение: 'коэффициент A не является целым числом'
        sys.exit(1)

def check_range(A,B,C):
    if abs(A)>10000 or abs(B)>10000 or abs(C)>10000:
        print('ОШИБКА: значение вне допустимого диапазона',file=sys.stderr)
        sys.exit(1)

def get_coefficients(mode,params):
    # получает коэффициенты в зависимости от режима
    # берёт готовые строки из кортежа params
    if mode=='interactive':
        A=to_int(input('Введите значение A:'),'A')
        B=to_int(input('Введите значение B:'),'B')
        C=to_int(input('Введите значение C:'),'C')
    else:
        A=to_int(params[0],'A')
        B=to_int(params[1],'B')
        C=to_int(params[2],'C')

    check_range(A,B,C)
    # проверяет диапазон через check_range
    return A,B,C

def solve(A,B,C):
    if A==0:
        if B!=0:
            print('Уравнение линейное')
            x=-C/B
            print(f'x={x:.3f}')
        else:
            print('ОШИБКА: это не уравнение, неизвестное отсутствует',file=sys.stderr)
            sys.exit(1)
    else:
        print('Уравнение квадратное')
        D=B*B-4*A*C
        print(f'D={D}')
        if D>0:
            x1=(-B+math.sqrt(D))/(2*A)
            x2=(-B-math.sqrt(D))/(2*A)
            print(f'x1={x1:.3f}')
            print(f'x2={x2:.3f}')
        elif D==0:
            x=-B/(2*A)
            print(f'x={x:.3f}')
        else:
            print('Действительных корней нет')

def main():
    mode,params=parse_args(sys.argv[1:])
    # sys.argv[1:] — все аргументы, кроме имени скрипта
    # вызывается parse_args, получаем режим и данные
    if mode=='help':
        # если режим 'help' — выводим справку и выходим с кодом 0 (успех)
        print_help()
        sys.exit(0)

    A,B,C=get_coefficients(mode,params)
    solve(A,B,C)

if __name__=='__main__':
    main()
    # чтобы код можно было и запускать, и импортировать без побочных эффектов

