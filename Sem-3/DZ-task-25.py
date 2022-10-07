# 25.	Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# o	45 -> 101101
# o	3 -> 11
# o	2 -> 10

import os
def cls():
    os.system('cls'if os.name == 'nt' else 'clear')
cls()

# def get_number(a: int):
#     list_ = []
#     while a >= 1:
#         list_.append(a % 2)
#         a = int(a / 2)
#     list_.reverse()
#     bin_number = ''
#     for item in list_:
#         bin_number += str(item)
#     return int(bin_number)


# num = int(input('Введите целое число: '))
# print('Двоичное число =>',get_number(num))

# 2nd way
a = int(input('Enter number: '))
print(bin(a)[2:])