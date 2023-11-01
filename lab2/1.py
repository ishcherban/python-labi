import math

def z(m):
    return math.sqrt(m) + 10

def average(x, y):
    result = 0
    for i in range(x, y + 1):
        result += i
    return result / (y - x + 1)

print(f'z(15): {z(15)}')
print(f'average from 1 to 15: {average(1,15)}')