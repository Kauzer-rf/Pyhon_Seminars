# 34.	Даны два файла, в каждом из которых находится запись многочлена, приравненного к нулю. Задача - сформировать файл, 
# содержащий сумму многочленов (суммируем подобные слагаемые).
# Пример:
# 1	Файл :		2*x**2 + 4*x + 5 = 0
# 2	Файл :		4*x**2 + 7*x + 9 = 0
# 3	Файл: (содержит результат)	6*x**2 + 11*x + 14 = 0
# Пример:
# 1	Файл :		2*x**3 + 4*x**2 + 5*x + 1 = 0
# 2	Файл :		4*x**2 + 7*x + 9 = 0
# 3	Файл: (содержит результат)	2*x**3 + 8*x**2 + 12*x + 10 = 0
import os


def cls():
    os.system('cls'if os.name == 'nt' else 'clear')


cls()

from random import random


with open('Sem-4\Dz-task-34\Dz_34_1.txt', 'w') as file:
    file.write(f'{int(random()* 100)}*x^2 + {int(random()* 100)}*x^5')

with open('Sem-4\Dz-task-34\Dz_34_2.txt', 'w') as file:
    file.write(f'{int(random()* 100)}*x^4 + {int(random()* 100)}*x^6')

with open('Sem-4\Dz-task-34\Dz_34_1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()

with open('Sem-4\Dz-task-34\Dz_34_2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2

with open('Sem-4\Dz-task-34\Dz_34_result.txt', 'w') as file:
    file.write(f'{list_of_poly_1} + {list_of_poly_2}')