# 29.Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
import os


def cls():
    os.system('cls'if os.name == 'nt' else 'clear')


cls()

a = int(input('a = '))
b = int(input('b = '))


def Efclid(a, b): # Нахождение наибольшего общего делителя (формула Эфклида)
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b
print(Efclid(a, b))

# Находим наименьшее общее кратное
print(a * b / Efclid(a,b))