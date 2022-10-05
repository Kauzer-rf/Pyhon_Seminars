# 23.	Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# o	[2, 3, 4, 5, 6] => [12, 15, 16];
# o	[2, 3, 5, 6] => [12, 15]
import os
def cls():
    os.system('cls'if os.name == 'nt' else 'clear')
cls()

def multiply_item(a: list):
    b = []
    if len(a) % 2 != 0:
        for i in range(int(len(a) / 2)):
            b.append(a[i] * a[- 1 - i])
        b.append(a[i + 1] ** 2)
    if len(a) % 2 == 0:
        for i in range(int(len(a) / 2)):
            b.append(a[i] * a[- 1 - i])
    return b


list_1 = [2, 3, 4, 5, 6]
list_2 = [2, 3, 5, 6]
print(f'Произведение списка №1 {list_1} => {multiply_item(list_1)}')
print(f'Произведение списка №2 {list_2} => {multiply_item(list_2)}')