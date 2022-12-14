# 16. Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.
from typing import List


def list_numb(num):
    result = []
    for i in range(1, num + 1):
        result.append((1 + 1 / i) ** i)
    if i == num:
        print(result)
    return result


def Sum_item_list(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum


numb = int(input('Введите целое положительное число: '))
multipli = list_numb(numb)
print(f'Сумма последовательности = {round(Sum_item_list(multipli),2)}')

# 2ое решение
# while True:
#     num = input('Введите целое положительное число')
#     try:
#         num = int(num)
#         if num > 0:
#             break
#         else:
#             print('Ошибка. Число отрицательное')
#     except ValueError:
#         print('Ошибка. Число не целое')
# list = []
# for i in range(1, num+1):
#     elem = round(((1 + 1/i)**i), 2)
#     list.append(elem)
# print(list)
# print(f'Сумма чисел равна: {sum(list)}')
