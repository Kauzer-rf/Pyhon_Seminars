# 27.Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.
import os


def cls():
    os.system('cls'if os.name == 'nt' else 'clear')


cls()

str = '22 56 33 6 4 56 444 7 1'
b = str.split(' ')
bet = []
for i in b:
    bet.append(int(i))

bet.sort()
print(bet[-1], bet[0])