# 27.Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.
import os


def cls():
    os.system('cls'if os.name == 'nt' else 'clear')


cls()

str = input("Введите список чисел, разделенных пробелом: ").split()
bet = list(map(int, str)) ## использование MAP для перевода строки в список чисел
bet.sort()
print(min(bet), max(bet))
