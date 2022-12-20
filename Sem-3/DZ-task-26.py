# 26.	Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# o	для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

import os
def cls():
    os.system('cls'if os.name == 'nt' else 'clear')
cls()

# Вариант решения 1
# def get_fibonachi(n):
#     if n in (1, 2):
#         return 1
#     return get_fibonachi(n - 1) + get_fibonachi(n - 2)


# def get_list_fibonachi(n):
#     list_ = []
#     for i in range(- n, 0):
#         if i % 2 == 0:
#             list_.append(- (get_fibonachi(- i)))
#         else:
#             list_.append(get_fibonachi(- i))
#     list_.append(0)
#     for i in range(1, n + 1):
#         list_.append(get_fibonachi(i))
#     return list_


# num = int(input('Введите целое положительное число: '))
# print(f'Последовательность Фиббоначи: {get_list_fibonachi(num)}')

# # Вариант решения 2
n = int(input('Input your number: '))
a = 0
b = 1
fibo1 = [0]
for i in range(n):
    a, b = b, a+b
    fibo1.append(a)
a = 0
b = 1
fibo2 = []
for i in range(n):
    a, b = b, a-b
    fibo2.append(a)
fibo2.reverse()
print(fibo2 + fibo1)
