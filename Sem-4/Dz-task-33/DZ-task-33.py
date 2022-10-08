# 33.	Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k и приравняйте его к нулю.
# Пример:
# 1.	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x²  = 0
# 2*x**2 + 4*x + 5 = 0
# или
# 2*x^2 + 4*x + 5 = 0
import os


def cls():
    os.system('cls'if os.name == 'nt' else 'clear')


cls()

from random import random


with open('Sem-4\Dz-task-33\Dz_33_1.txt', 'w') as file:
    file.write(f'{int(random()* 100)}*x^2 + {int(random()* 100)}*x^5')

with open('Sem-4\Dz-task-33\Dz_33_2.txt', 'w') as file:
    file.write(f'{int(random()* 100)}*x^4 + {int(random()* 100)}*x^6')

with open('Sem-4\Dz-task-33\Dz_33_1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()

with open('Sem-4\Dz-task-33\Dz_33_2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2

with open('Sem-4\Dz-task-33\Dz_33_result.txt', 'w') as file:
    file.write(f'{list_of_poly_1} + {list_of_poly_2}')