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
import numpy as np
import matplotlib.pyplot as plot

globalEpsilon = 1e-6
radius = 8                                 # working plane radius
centre = (1, 2)                            # centre of the working circle
arrShape = 100                             # number of points processed / 360
step = radius / arrShape                   # step between two points

# 0 ⩽ x,y ⩽ 10:
# x0 = 1
# y0 = 2

def firstFunction(x, y):
    return (x - 3) * (x - 3)  + y * y + 1

def secondFunction(x, y):
    return (x + 1)*(x + 1) + (2*y - 8)*(2*y - 8) + 1

def thirdFunction(x, y):
    return x * x + (x * y) + y * y - (16 * x) - (17 * y) + 94

def fourthFunction(x, y):
    return ((x - 7) * (x - 7) + (y - 8) * (y - 8)) * ((x - 8) * (x - 8) + (y - 7) * (y - 7)) + 4

def fifthFunction(x, y):
    return (4 * x * y - 19) * (4 * x * y - 19) * (math.cos(2 * x * math.pi) + math.cos(2 * y * math.pi)) - x - y+24

def rotateVector(length, a):
    return length * np.cos(a), length * np.sin(a)

def derivativeY(epsilon, arg, customFunction):
    return (customFunction(arg, epsilon + globalEpsilon) - customFunction(arg, epsilon)) / globalEpsilon

def derivativeX(epsilon, arg, customFunction):
    return (customFunction(globalEpsilon + epsilon, arg) - customFunction(epsilon, arg)) / globalEpsilon

def gradient(x, y, customFunction):
    return derivativeX(x, y, customFunction) + derivativeY(y, x, customFunction)

def calculateFlipPoints(customFunction):
    flip_points = np.array([0, 0])
    points = np.zeros((360, arrShape), dtype=bool)
    cx, cy = centre

    for i in range(arrShape):
        for alpha in range(360):
            x, y = rotateVector(step, alpha)
            x = x * i + cx
            y = y * i + cy
            points[alpha][i] = derivativeX(x, y, customFunction) + derivativeY(y, x, customFunction) > 0
            if not points[alpha][i - 1] and points[alpha][i]:
                flip_points = np.vstack((flip_points, np.array([alpha, i - 1])))

    return flip_points

def pickEstimates(positions, customFunction):
    vx, vy = rotateVector(step, positions[1][0])
    cx, cy = centre
    best_x, best_y = cx + vx * positions[1][1], cy + vy * positions[1][1]

    for index in range(2, len(positions)):
        vx, vy = rotateVector(step, positions[index][0])
        x, y = cx + vx * positions[index][1], cy + vy * positions[index][1]
        if customFunction(best_x, best_y) > customFunction(x, y):
            best_x = x
            best_y = y

    for index in range(360):
        vx, vy = rotateVector(step, index)
        x, y = cx + vx * (arrShape - 1), cy + vy * (arrShape - 1)
        if customFunction(best_x, best_y) > customFunction(x, y):
            best_x = x
            best_y = y

    return best_x, best_y

def gradientDescent(best_estimates, is_x, customFunction):
    derivative = derivativeX if is_x else derivativeY
    best_x, best_y = best_estimates
    descent_step = step
    value = derivative(best_y, best_x, customFunction)

    while abs(value) > globalEpsilon:
        descent_step *= 0.95
        best_y = best_y - descent_step \
            if derivative(best_y, best_x, customFunction) > 0 else best_y + descent_step
        value = derivative(best_y, best_x, customFunction)

    return best_y, best_x

def findMinimum(customFunction):
    return gradientDescent(gradientDescent(pickEstimates(calculateFlipPoints(customFunction), customFunction), False, customFunction), True, customFunction)

def getGrid(grid_step, customFunction):
    samples = np.arange(-radius, radius, grid_step)
    x, y = np.meshgrid(samples, samples)
    return x, y, customFunction(x, y)

def drawChart(point, grid):
    point_x, point_y, point_z = point
    grid_x, grid_y, grid_z = grid
    plot.rcParams.update({
        'figure.figsize': (4, 4),
        'figure.dpi': 200,
        'xtick.labelsize': 4,
        'ytick.labelsize': 4
    })
    ax = plot.figure().add_subplot(111, projection='3d')
    ax.scatter(point_x, point_y, point_z, color='red')
    ax.plot_surface(grid_x, grid_y, grid_z, rstride=5, cstride=5, alpha=0.7)
    plot.show()

myFunction = firstFunction
#minX, minY = findMinimum(myFunction)
#minimum = (minX, minY, myFunction(minX, minY))
#print("first function min = %2f", minimum)
# drawChart(minimum, getGrid(0.05, myFunction))

#myFunction = secondFunction
#minX, minY = findMinimum(myFunction)
#minimum = (minX, minY, myFunction(minX, minY))
#print("second function min = ", minimum)
# drawChart(minimum, getGrid(0.05, myFunction))

#myFunction = thirdFunction
#minX, minY = findMinimum(myFunction)
#minimum = (minX, minY, myFunction(minX, minY))
#print("third function min = ", minimum)
# drawChart(minimum, getGrid(0.05, myFunction))

#myFunction = fourthFunction
#myPoints = calculateFlipPoints(myFunction)
#print(myPoints)
#positions = rotateVector(myPoints)
#minX, minY = findMinimum(myFunction)
#minimum = (minX, minY, myFunction(minX, minY))
#print("fourth function min = ", minimum)
# drawChart(minimum, getGrid(0.05, myFunction))

# myFunction = fifthFunction
minX, minY = findMinimum(myFunction)
minimum = (minX, minY, myFunction(minX, minY))
print("fifthFunction function min = ", minimum)
# drawChart(minimum, getGrid(0.05, myFunction))

