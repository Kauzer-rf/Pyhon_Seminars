# 22.	Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# o	[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import os
def cls():
    os.system('cls'if os.name == 'nt' else 'clear')
cls()

def select_index(a):
    not_even = []
    if len(a) >= 2:
        for i in range(1, len(a), 2):
            not_even.append(a[i])
        return not_even
    else:
        print('В списке всего одно значение! ')


def get_sum(a):
    sum_ = 0
    for i in a:
        sum_ += i
    return sum_


list_ = [2, 3, 5, 9, 3]
print(f' На нечётных позициях элементы {select_index(list_)}')
print(f' Сумма нечётных элементов: {get_sum(select_index(list_))}')

# 2nd way
# spisok = [2, 3, 5, 9, 3]
# sum = 0
# for i in range(1,len(spisok,2)):
#     sum +=spisok[i]
# print(sum)

# 3rd way
# list=[2,3,5,9,3][1::2]
# print(sum(list))