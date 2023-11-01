def func(arr):
    tmp = None
    for i in arr:
        if i < 0 and (tmp == None or i > tmp):
            tmp = i 
    return tmp

n = int(input('Введіть розмір масива: '))
arr = []

for i in range(n):
    arr.append(int(input(f'[{i}]: ')))

print(f'Максимальний від’ємний елемент: {func(arr)}')