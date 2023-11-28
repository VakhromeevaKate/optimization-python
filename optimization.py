# Реализовать на С или python поиск минимального значения для каждой из 5 заданных двумерных функций f(x,y) на квадрате 0 ⩽ x,y ⩽ 10:
# (a) fa(x,y)=(x−3)2+y2+1
# (b) fb(x,y)=(x+1)2+(2y−8)2+1
# (c) fc(x,y)=x2+xy+y2−16x−17y+94
# (d) fd(x,y)=((x−7)2+(y−8)2)·((x−8)2+(y−7)2)+4
# (e) fe(x,y)=(4xy−19)2·(cos2πx+cos2πy)−x−y+24
# Решение вычислить с точностью ε = 10−6.
# В качестве начальной точки взять (x0, y0) = (1, 2).
# Найти точку минимума (x∗,y∗), значение функции f(x∗,y∗) и количество итераций (вычислений функции) n, которое потребовалось на достижение требуемой точности выбранным методом.

import math

epsilon = 1e-6

# 0 ⩽ x,y ⩽ 10:
x0 = 1
y0 = 2

def firstFunction(x, y):
    return (x - 3)^2 + y^2 + 1

def secondFunction(x, y):
    return (x + 1)*(x + 1) + (2*y - 8)*(2*y - 8) + 1

def thirdFunction(x, y):
    return x * x + (x * y) + y * y - (16 * x) - (17 * y) + 94

def fourthFunction(x, y):
    return ((x - 7) * (x - 7) + (y - 8) * (y - 8)) * ((x - 8) * (x - 8) + (y - 7) * (y - 7)) + 4

def fifthFunction(x, y):
    return (4 * x * y - 19) * (4 * x * y - 19) * (math.cos(2 * x * math.pi) + math.cos(2 * y * math.pi)) - x - y+24

# print(fifthFunction(x0, y0))

