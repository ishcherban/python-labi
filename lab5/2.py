arr = [
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

offset = 0

for y in range(7):
    for x in range(offset, 7 + offset):
        arr[y].append(x)
    offset -= 1

for i in arr:
    print(i)