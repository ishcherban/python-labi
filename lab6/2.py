arr = list(map(int,input('Введіть масив: ').split()))
new_arr = []
for i in arr:
    if arr.count(i) > 1 and i not in new_arr:
        new_arr.append(i)

print(new_arr)
