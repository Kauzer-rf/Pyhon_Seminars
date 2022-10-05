# 20. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

n = int(input ('Enter number: '))
my_list = ['er567', 'iu5', 'tru456t', 'ffg567']
length = len(my_list)
n = str(n)
Flag = False
for i in range (length):
    if my_list[i].find(n) !=-1:
        Flag = True
        break
print(Flag)