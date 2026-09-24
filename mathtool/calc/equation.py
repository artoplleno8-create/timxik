import math

MAX_COEFFICIENTS = 10000

def validate_coefficients(coefficients):
    for name,value in coefficients.items():
        if abs(value)>MAX_COEFFICIENTS:
            raise ValueError(f'коэффициент {name} вне допустимого диапозона')

def solve_quadratic(a,b,c):
    if a==0 and b==0:
        raise ValueError('это не уравнение')
    if a==0:
        d=b*b-4*a*c
        if d>0:
            x1=(-b+math.sqrt(d))/(2*a)
            x2=(-b-math.sqrt(d))/(2*a)
            return 'квадратное' , d , [x1,x2]
        if d==0:
            return 'квадратное',d, [-b/(2*a)]
        return 'квадратное',d, []
    