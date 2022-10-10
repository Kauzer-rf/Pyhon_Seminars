"""
Как посчитать строку как числа (2+2)*3
"""
s = '(2+2)*3'

def parse(s):
    result = []
    digit = ''
    for symb in s:
        if symb.isdigit():
            digit += symb
        elif symb in ['(', ')']:
            if digit:
                result.apped(float(digit))
                digit = ''
            result.append(symb)
        else:
            if digit:
                result.apped(float(digit))
            digit = ''
            result.append(symb)
    else:
        if digit:
           result.apped(float(digit))
    return result 

    print(parse(s))