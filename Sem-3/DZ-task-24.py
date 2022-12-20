# 24.	Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# o	[1.1, 1.2, 3.1, 5, 10.01] => 0.19

from typing import List
import os
from unicodedata import decimal


def cls():
    os.system('cls'if os.name == 'nt' else 'clear')


cls()

# Вариант решения 1
# def sort_fractional_part(a: List):
#     for i in range(len(a)):
#         if type(a[i]) == float:
#             a[i] = round(a[i] - int(a[i]), 2)
#     a.sort()
#     return a


# def get_difference_max_min_fractional(a: List):
#     max = 0
#     min = 0
#     for i in range(- 1, - len(a) + 1, - 1):
#         if type(a[i]) == float:
#             max = a[i]
#             break
#     for item in a:
#         if type(item) == float:
#             min = item
#             break
#     print(f'Максимальное значение: {max}')
#     print(f'Миннимальное значение: {min}')
#     difference = max - min
#     return difference


# list_ = [1.1, 1.2, 3.1, 5, 10.01]
# print(f'Дан список: {list_}\n')
# print(
#     f'Разница между максимальным и минимальным значением дробной части элементов => {get_difference_max_min_fractional(sort_fractional_part(list_))}')


# Вариант решения 2
a = [1.1, 1.2, 3.1, 5, 10.01]
b = []
for i in a:
    if i % 1 != 0:
        b.append(i % 1)
b.sort()
print(b)

print(
    f'Разница между максимальным и минимальным значением дробной части элементов равна: {round((b[-1]-b[0]),3)}')
