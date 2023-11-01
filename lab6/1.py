n = int(input("Введіть розмір масиву: "))
arr = []

for i in range(n):
    arr.append(int(input(f'[{i}]: ')))

for i in range(n):
    if (i % 2) == 0:
        arr.append(arr[i])

print(arr)