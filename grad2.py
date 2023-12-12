import math
import numpy as np

# определяем функции, для которых будем считать минимум градиентным спуском:
def first_function(x):
    return (x[0] - 3) * (x[0] - 3)  + x[1] * x[1] + 1

def second_function(x):
    return (x[0] + 1)*(x[0] + 1) + (2*x[1] - 8)*(2*x[1] - 8) + 1

def third_function(x):
    return x[0] * x[0] + (x[0] * x[1]) + x[1] * x[1] - (16 * x[0]) - (17 * x[1]) + 94

def fourth_function(x):
    return ((x[0] - 7) * (x[0] - 7) + (x[1] - 8) * (x[1] - 8)) * ((x[0] - 8) * (x[0] - 8) + (x[1] - 7) * (x[1] - 7)) + 4

def fifth_function(x):
    return (4 * x[0] * x[1] - 19) * (4 * x[0] * x[1] - 19) * (math.cos(2 * x[0] * math.pi) + math.cos(2 * x[1] * math.pi)) - x[0] - x[1] + 24

def gradient(point, custom_function):
    if (custom_function == first_function):
        return gradient_1(point)
    if (custom_function == second_function):
        return gradient_2(point)
    if (custom_function == third_function):
        return gradient_3(point)
    if (custom_function == fourth_function):
        return gradient_4(point)
    if (custom_function == fifth_function):
        return gradient_5(point)

def gradient_1(point):
    dx = 2 * point[0] - 6
    dy = 2 * point[1]
    return np.array([dx, dy])

def gradient_2(point):
    dx = 2 * point[0] + 2
    dy = 8 * point[1] - 32
    return np.array([dx, dy])

def gradient_3(point):
    dx = 2 * point[0] + point[1] - 16
    dy = 2 * point[1] + point[0] - 17
    return np.array([dx, dy])

def gradient_4(point):
    dx = 4 * math.pow(point[0], 3) - 90 * math.pow(point[0], 2) + 4 * point[0] * math.pow(point[1], 2) + 900 * point[0] - 60 * point[0] * point[1] - 30 * math.pow(point[1], 2) + 452 * point[1] - 3390
    dy = 4 * math.pow(point[1], 3) - 90 * math.pow(point[1], 2) + 4 * math.pow(point[0], 2) * point[1] - 900 * point[1] - 60 * point[0] * point[1] - 30 * math.pow(point[0], 2) + 452 * point[0] - 3390
    return np.array([dx, dy])

def gradient_5(point):
    dx = -32 * math.pi * math.pow(point[0], 2) * math.pow(point[1], 2) * math.sin(2 * math.pi * point[0]) + 32 * point[0] * math.pow(point[1], 2) * math.cos(2 * math.pi * point[0]) + 32 * point[0] * math.pow(point[1], 2) * math.cos(2 * math.pi * point[1]) + 304 * math.pi * point[0] * point[1] * math.sin(2 * math.pi * point[0]) - 152 * point[1] * math.cos(2 * math.pi * point[0]) - 152 * point[1] * math.cos(2 * math.pi * point[1]) + 722 * math.pi * math.sin(2 * math.pi * point[0]) - 1
    dy = -32 * math.pi * math.pow(point[0], 2) * math.pow(point[1], 2) * math.sin(2 * math.pi * point[1]) + 32 * math.pow(point[0], 2) * point[1] * math.cos(2 * math.pi * point[0]) + 32 * math.pow(point[0], 2) * point[1] * math.cos(2 * math.pi * point[1]) + 304 * math.pi * point[0] * point[1] * math.sin(2 * math.pi * point[1]) - 152 * point[0] * math.cos(2 * math.pi * point[0]) - 152 * point[0] * math.cos(2 * math.pi * point[1]) + 722 * math.pi * math.sin(2 * math.pi * point[1]) - 1
    return np.array([dx, dy])

def is_point_in_interval(point, interval):
    x, y = point
    left_bound, right_bound = interval
    if x >= left_bound and y >= left_bound and x < right_bound and y < right_bound:
        return True
    return False

def get_point_belongs_interval(point, interval):
    if is_point_in_interval(point, interval):
        return point
    inner_point = point
    left_bound, right_bound = interval
    if inner_point[0] < left_bound:
        inner_point[0] = left_bound
    if inner_point[0] > right_bound:
        inner_point[0] = right_bound
    if inner_point[1] < left_bound:
        inner_point[1] = left_bound
    if inner_point[1] > right_bound:
        inner_point[1] = right_bound
    return inner_point

def gradient_descent(custom_function, start_point, stopping_threshold, gamma):
    point = start_point
    point_min = point
    f_min = custom_function(point)
    f_old = custom_function(point)
    point = point - gradient(point, custom_function) * gamma
    f_new = custom_function(point)
    
    i = 0
    while abs(f_old - f_new) > stopping_threshold:
        i = i + 1
        f_old = f_new
        point = get_point_belongs_interval(point - gradient(point, custom_function) * gamma, [0, 10])
        f_new = custom_function(point)
        if f_new < f_min:
            f_min = f_new
            point_min = point
        #print("x = {point[0]}, y = {point[1]}, f(x) = {f}, min = ({point_min[0]}, {point_min[1]})".format(point = point, f = custom_function(point), point_min = point_min))
    return (point_min, f_min, i)

def print_calculation_data(my_function, name, stopping_threshold, gamma):
    point, f_min, iterator = gradient_descent(
        my_function,
        start_point=np.array([1, 2]),
        stopping_threshold = stopping_threshold,
        gamma = gamma
    )
    print("{name} function min = ({minX}, {minY}), function value = {val} iterations = {i}".format(name = name, minX = point[0], minY = point[1], val = f_min, i = iterator))
    iterator = 0

print_calculation_data(first_function, "First", stopping_threshold=0.000001, gamma=0.001)
print_calculation_data(second_function, "Second", stopping_threshold=0.000001, gamma=0.001)
print_calculation_data(third_function, "Third", stopping_threshold=0.000001, gamma=0.001)
print_calculation_data(fourth_function, "Fourth", stopping_threshold=0.000001, gamma=0.0000001)
print_calculation_data(fifth_function, "Fifth", stopping_threshold=0.000001, gamma=0.0000001)