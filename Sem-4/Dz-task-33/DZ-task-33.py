# 33.	Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k и приравняйте его к нулю.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x²  = 0
# 2*x**2 + 4*x + 5 = 0
# или
# 2*x^2 + 4*x + 5 = 0
from random import randint
import os


def cls():
    os.system('cls'if os.name == 'nt' else 'clear')


cls()


k = int(input('Введите натуральную степень k: '))

# "K" при старшей степени != 0
koeff = [randint(0, 100) for i in range(k)]+[randint(1, 100)]

poly = '+'.join([f'{(j,"")[j==1]}x^{i}' for i,
                j in enumerate(koeff) if j][::-1])

# Поиск и замены:
poly = poly.replace('x^1+', 'x+')
poly = poly.replace('x^0', '')
poly += ('', '1')[poly[-1] == '+']
poly = (poly, poly[:-2])[poly[-2:] == '^1']
print(poly)
with open("Sem-4\Dz-task-33\Dz_33_result.txt", "w") as file:
    file.write(poly)
