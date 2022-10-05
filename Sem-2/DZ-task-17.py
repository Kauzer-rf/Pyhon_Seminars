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

with open('file.txt', 'w') as data:
    count_number = random.randrange(1, N)
    for i in range(0, count_number):
        data.writelines(str(random.randrange(0, N+1)) + '\n')

result = 1
with open('file.txt', 'r') as data:
    for line in data:
        print(f'Прочтен из file.txt следующий индекс: {line}')
        result *= list[int(line)]
print(f'Произведение чисел = {result}')
