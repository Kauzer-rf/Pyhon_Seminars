# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input('Введите Х: '))
y = int(input('Введите У: '))

if (x > 0 and y > 0):
    print(f'x = {x}; y = {y} -> 1ая четверть')
elif (x < 0 and y > 0):
    print(f'x = {x}; y = {y} -> 2ая четверть')
elif (x < 0 and y < 0):
    print(f'x = {x}; y = {y} -> 3ая четверть')
elif (x > 0 and y < 0):
    print(f'x = {x}; y = {y} -> 4ая четверть')
elif (x == 0 or y == 0):
    print('Ошибка, X и Y должны быть больше 0.')
    