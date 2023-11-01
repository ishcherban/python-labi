import math

def z(m):
    return math.sqrt(m) + 10

def average(x, y):
    result = 0
    for i in range(x, y + 1):
        result += i
    return result / (y - x + 1)
