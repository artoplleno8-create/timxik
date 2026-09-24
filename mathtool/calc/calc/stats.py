import math

MAX_COUNT=20
MAX_ABS=10000.0

def validate(values):
    if not values:
        raise ValueError('последовательность пуста')
    if len(values)>MAX_COUNT:
        raise ValueError('слишком много чисел')
    for value in values:
        if not math.isfinite(value):
            raise ValueError('число не является конечным')
        if abs(value)>MAX_ABS:
            raise ValueError('число вне допустимого диапозона')

def total(values):
    result=0
    for value in values:
        result+=value
    return result

def mean(values):
    return total(values)/len(values)

def sum_of_squares(values):
    result=0
    for value in values:
        result+=value*value
    return result

def rms(values):
    return math.sqrt(sum_of_squares(values)/len(values))

def min_value(values):
    result=values[0]
    for value in values:
        if value<result:
            result=value
    return result

def max_value(values):
    result=values[0]
    for value in values:
        if value>result:
            result=value
    return result

def  count_positive(values):
    result=0
    for value in values:
        if value>0:
            result+=1
    return result

def count_negative(values):
    result=0
    for value in values:
        if value<0:
            result+=1
    return result

def _sum_squared_deviations(values):
    m=mean(values)
    result=0
    for value in values:
        result+=(value-m)**2
    return result

def variance(values):
    return _sum_squared_deviations(values)/len(values)

def std_deviation(values):
    return math.sqrt(variance(values))

def sample_std(values):
    if len(values)<2:
        return None
    return math.sqrt(_sum_squared_deviations(values)/(len(values)-1))

REPORT=[
    ('Количество',len,"d"),
    ('Сумма',total,'.3f'),
    ('Ср. арифм',mean,'.3f'),
    ('Сумма квадратов',sum_of_squares,'.3f'),
    ('Ср. кв.',rms,'.3f'),
    ('Дисперсия',variance,'.3f'),
    ('СКО',std_deviation,'.3f'),
    ('Станд. откл.',sample_std,'.3f'),
    ('Наименьшее',min_value,'.3f'),
    ('Наибольшее',max_value,'.3f'),
    ('Положительное',count_positive,'d'),
    ('Отрицательное',count_negative,'d'),
]