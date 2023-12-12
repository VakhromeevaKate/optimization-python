import numpy as np

# Используем векторную запись точки.
x = np.array([1, 2])

def f(x):
# f(x) = 0.5x^2 + 0.2y^2
    return 0.5*x[0]**2 + 0.2*x[1]**2



def grad(x):
# grad(x) = [x, 0.4y]
    dx = x[0]
    dy = 0.4 * x[1]
    return np.array([dx, dy])


print("Точка 0:", x)
print("f(x) =", f(x))
print()


# Двигаем точку против градиента.
x = x - grad(x)
print("Точка 1:", x)
print("f(x) =", f(x))

#Точка 0: [1 2]
#f(x) = 1.3

import numpy as np

def f(x):
    return x[0]**2 + 2*x[1]**2 + x[2]**4


def grad(x):
    return np.array([2*x[0], 4*x[1], 4*x[2]**3])


# Стартовая точка
x = np.array([1.5, 2, 3])


gamma = 1e-2
max_iter = 10
eps = 1e-4
f_old = f(x)
x = x - grad(x) * gamma
f_new = f(x)
i = 0

while abs(f_old - f_new) > eps and i < max_iter:
    i = i + 1
    f_old = f_new
    print(f(x))
    x = x - grad(x) * gamma
    f_new = f(x)
    print(f(x))