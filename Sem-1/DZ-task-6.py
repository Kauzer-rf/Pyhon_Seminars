# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
day = int(input('Введите день недели (число от 1 до 7): '))
if (day >= 5):
    print('Это выходной день')
else:
    print('Это будний день')
