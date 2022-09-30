# 13.	Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
# import string

# string_1 = input('Введите строку 1: ')
# string_2 = input('Введите строку 2: ')
# print(string_1.count (string_2))

# Решение циклами
str1 = input('Введите строку 1: ')
str2 = input('Введите строку 2: ')
count = 0
k = 0
if len(str2) > 1:
    for i in range(1, len(str1)):
        if str2 in str1[k:i]:
            count += 1
            k = i
else:
    for j in range(len(str1)):
        if str1[j] == str2:
            count += 1

print(f"Вторая строка входит в первую {count} раз(а).")
