# 17. Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода и зависит от количества элементов в списке) в одной строке одно число.
# Пример:
# Файл:
# 4
# 5
# 2
# N = 3 => [-3, -2, -1, 0, 1, 2, 3]
# Результат: 1*2*(-1) = -2
import random

N = int(input('Введите число N: '))
list = []
for i in range(-N, N+1):
    list.append(i)
print(f'Полученный список: {list}')

num1 = random.randrange(len(list))
num2 = random.randrange(len(list))
num3 = random.randrange(len(list))

print(
    f'Сгенеририровны случайные позиции и записаны в file.txt: {num1}, {num2}, {num3}.')

with open('file.txt', 'w') as data:
    data.write(f'{num1}\n')
    data.write(f'{num2}\n')
    data.write(f'{num3}\n')

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(f'Прочтен из file.txt следующиq индекс: {line}')
data.close()


index_1 = 0
index_2 = 0
index_3 = 0
for i in range(len(list)):
    if i == num1:
        index_1 = list[i]
    elif i == num2:
        index_2 = list[i]
    elif i == num3:
        index_3 = list[i]
multiplay = index_1*index_2*index_3
print(f'Произведение чисел с индексами {num1}, {num2}, {num3} = {index_1}*{index_2}*{index_3} = {multiplay} ')
