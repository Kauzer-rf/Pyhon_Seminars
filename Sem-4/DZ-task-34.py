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