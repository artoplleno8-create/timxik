import math

MAX_TERMS=10000
MAX_EPS=0.0001
MAX_ITERATIONS=100000

def sign(n):
    return 1 if n%2==1 else -1

def term_sqplus(n):
    return sign(n)/(n*n+1)

def term_third(n):
    return sign(n)/(3*n)

FORMULAS={
    'sqplus': (term_sqplus,
               'S=1/(1^2+1)-1/(2^2+1)+1/(3^2+1)-...'),
    'third': (term_third,
              'S=1/3-1/6+1/9-1/12+...',)
}

def sum_by_terms(term,count):
    result=0
    for n in range(1,cpunt+1):
        result+=term(n)
    return result

def sum_by_eps(term,eps):
    result=0
    n=0
    while True:
        n+=1
        value=term(n)
        if abs(value)<eps:
            return result, n
        if n>MAX_ITERATIONS:
            raise ValueError('точность не достигнута')

def validate_terms(terms):
    if not(1<=terms<=MAX_TERMS):
        raise ValueError('количество слагаемых вне диапозона')

def validate_eps(eps):
    if not(math.isfinite(eps) and 0<eps<=MAX_EPS):
        raise ValueError('точность вне диапозона')

