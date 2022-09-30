# 13.	Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
# import string

# string_1 = input('Введите строку 1: ')
# string_2 = input('Введите строку 2: ')
# print(string_1.count (string_2))

# Решение циклами
str1 = input('Введите строку 1: ')
str2 = input('Введите строку 2: ')
count = 0
k = 1
for i in range(0, len(str1) - len(str2)+1, k):
    if str2 in str1[i:i+len(str2)]:
        count += 1
        k = len(str2)
    else:
        k = 1
print(f"Вторая строка входит в первую {count} раз(а).")
