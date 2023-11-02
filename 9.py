import matplotlib.pyplot as plt
import numpy as np
import math

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def mycosh(x, nn): #<-- use your own function here
    sum = 1
    xx = x ** 2
    n = 1
    while n < nn:
        current = xx / factorial(2 * n)
        sum = sum + current
        xx = xx * (x ** 2)
        # if abs(current) < 1e-4: break
        n = n + 1
    return sum

def main():
    x = np.arange(0.01, 1.21, 0.01)
    plt.title(r'Teylor set: $f_i(x)$, cosh$(x)$') # заголовок
    plt.plot(x, [mycosh(xi,1)  for xi in x], label=r'$f_1(x)$')
    plt.plot(x, [mycosh(xi,2)  for xi in x], label=r'$f_2(x)$')
    plt.plot(x, [mycosh(xi,3)  for xi in x], label=r'$f_3(x)$')
    plt.plot(x, [mycosh(xi,4)  for xi in x], label=r'$f_4(x)$')
    plt.plot(x, [mycosh(xi,5)  for xi in x], label=r'$f_5(x)$')
    plt.plot(x, [mycosh(xi,6)  for xi in x], label=r'$f_6(x)$')
    plt.plot(x, [mycosh(xi,7)  for xi in x], label=r'$f_7(x)$')
    plt.plot(x, [mycosh(xi,8)  for xi in x], label=r'$f_8(x)$')
    plt.plot(x, [math.cosh(xi) for xi in x], "r--", lw=3,
         label=r'cosh$(x)$')
    plt.xlabel(r'$x$', fontsize=14)       # ось абсцисс
    plt.ylabel(r'$y=f(x)$', fontsize=14)  # ось ординат
    plt.legend(loc='best', fontsize=12)   # легенда
    plt.grid()                            # показать сетку
    plt.savefig('9.png')                  # сохранить рисунок
    plt.show()                            # показать рисунок

main()
