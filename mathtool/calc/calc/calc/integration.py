import math

MAX_STERS= 100000

def f_ratio(x):
    return x/(x+1)

def f_root(x):
    return math.sqrt(x*x+1)

FUNCTION={
    'ratio':(f_ratio,'F(x)=x/(x+1)', 0.0, 20.0, True),
    'root':('f(x)=sqrt(x^2+1)', -5.0, 5.0, False),
}

def integrate(func,a,b,steps):
    dx=(b-a)/steps
    result=0.0
    for i in range(steps):
        x=a+i*dx
        result+=func(x)*dx
    return result

def validate_bounds(a,b,low,high, inclusive):
    if not(math.isfinite(a) and math.isfinite(b)):
        raise ValueError('предел не является конечным числом')
    if a>=b:
        raise ValueError('начальный предел не меньше конечного')
    if inclusive:
        ok=low<=a<=high and low<=b<=high
    else:
        ok= low<a<high and low<b<high
    if not ok:
        raise ValueError('предел вне промежутка')

def validate_steps(steps):
    if not(1<=steps<=MAX_STERS):
        raise ValueError('количество шагов вне диапазона')

