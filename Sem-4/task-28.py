# 28.	Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1.	с помощью математических формул нахождения корней квадратного уравнения
# 2.	с помощью дополнительных библиотек Python (math)
import os


def cls():
    os.system('cls'if os.name == 'nt' else 'clear')


cls()

A = float(input('Enter A: '))
B = float(input('Enter B: '))
C = float(input('Enter C: '))
D = B**2 - 4*A*C

x = 0
x1 = 0

if D == 0:
    x = -B/(2*A)
    print(f'Корень: {x}')
elif D > 0:
    x1 = (-B + D ** 0.5) / (2 * A)
    x = (-B - D ** 0.5) / (2 * A)
    print(f'Корни: {x} и {x1}')
else:
    print('нет корней')