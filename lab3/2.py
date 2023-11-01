def func(string):
    result = []
    prev_char = None
    
    for char in string:
        if char != prev_char:
            result.append(char)
        prev_char = char
    
    return ''.join(result)

print('Result: ' + func("ttessst strrriingg"))