def func(string):
    if len(string) > 2:
        return string[1], string[-2]
    
print(func("Apple"))