# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

num = input('Введите вещественное число: ')
num = num.split('.')
q = int(num[0])
sum = 0

while q != 0:
    sum += q % 10
    q //= 10

if len(num) == 2:
    w = int(num[1])
    while w != 0:
        sum += w % 10
        w //= 10

print(f'Сумма цифр данного числа = {sum}')

# 2ой вариант решения
# sum = 0
# num = input('Введите вещественное число: ')
# for i in str(num):
#     if i!='.' and i != '-':
#         sum += int(i)
# print(f'Сумма цифр данного числа = {sum}')