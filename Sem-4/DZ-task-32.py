# 32.	Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import os
from random import random


def cls():
    os.system('cls'if os.name == 'nt' else 'clear')


cls()

rnd_list = []
for i in range(10):
    rnd_list.append(int(random()*10))
print(f'Сгенерирована последовательность: {rnd_list}')
rnd_list.sort()
print(f'Для удобства отсортивруем ее: {rnd_list}')
sorted_list = []
for j in rnd_list:
    counter = 0
    for k in rnd_list:
        if j == k:
            counter += 1
    if counter == 1:
        sorted_list.append(j)

print(f'Список уникальных элементов: {sorted_list}')
