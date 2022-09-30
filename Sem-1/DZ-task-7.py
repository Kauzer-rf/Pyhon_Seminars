# Напишите программу для. проверки истинности утверждения
#    ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def TrueOrFalse():
    res = True
    for X in range(2):
        for Y in range(2):
            for Z in range(2):
                leftValue = not (X or Y or Z)
                rightValue = not X and not Y and not Z
                if leftValue != rightValue:
                    print(f'X = {X}, Y = {Y}, Z = {Z}')
                    print(False)
                    res = False
                else:
                    print(f'X = {X}, Y = {Y}, Z = {Z}')
                    print(True)
    return res


print('Результат: ')
result = TrueOrFalse()

# Альтернативное решение
# for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 f = not(x or y or z) == (not(x) and not(y) and not(z))
#                 print(x,y,z,f)
