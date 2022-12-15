# Напишите программу для. проверки истинности утверждения
#    ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# Решение 1
# def TrueOrFalse():
#     res = True
#     for X in range(2):
#         for Y in range(2):
#             for Z in range(2):
#                 leftValue = not (X or Y or Z)
#                 rightValue = not X and not Y and not Z
#                 if leftValue != rightValue:
#                     print(f'X = {X}, Y = {Y}, Z = {Z}')
#                     print(False)
#                     res = False
#                 else:
#                     print(f'X = {X}, Y = {Y}, Z = {Z}')
#                     print(True)
#     return res


# print('Результат: ')
# result = TrueOrFalse()

# Решение 2
for x in range(2):
        for y in range(2):
            for z in range(2):
                f = not(x or y or z) == (not(x) and not(y) and not(z))
                print(x,y,z,f)

# Решение 3 (от ревьювера)
# for Z in range(2):
#     if not (X or Y or Z) != (not X and not Y and not Z):
#         print(f'X = {X}, Y = {Y}, Z = {Z}')
#         print(False)
#         res = False
# else:
#     print(f'X = {X}, Y = {Y}, Z = {Z}')
#     print(True)
