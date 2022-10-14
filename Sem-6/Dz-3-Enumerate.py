# Напишите программу, которая принимает на вход число N и выводит числа от -N до N.

N = abs(int(input('Введите число N: ')))
my_list = []
for i in range(-N, N+1):
    my_list.append(i)

for sorting in enumerate(my_list):  # используем enumerate для вывода значений и индексов
    print(sorting)