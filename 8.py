import math

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def mycosh(x): #<-- use your own function here
    sum = 1
    xx = x ** 2
    n = 1
    while n < 10:
        current = xx / factorial(2 * n)
        sum = sum + current
        xx = xx * (x ** 2)
        if abs(current) < 1e-4: break
        n = n + 1
    return sum

def main():
    n = 5
    dev = 0
    for i in range(0, n, 1):
        x = 0.1 * (i+1)
        fmy = mycosh(x)
        std = math.cosh(x) #<-- use your own math function
        dif = abs(fmy - std)
        print(f"{i}) mycosh(x={x})={fmy} cosh(x={x})={std} dif={dif}")
        dev += dif ** 2
    dev = math.sqrt(dev / n)
    print(f"dev={dev}")

main()
