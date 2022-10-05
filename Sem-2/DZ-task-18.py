# # 18.	Реализуйте алгоритм перемешивания списка.


# from random import randint

# def mixing_list(list):
#     result = []
#     for i in range(len(list)):
#         temp = randint(0, len(list) - 1)
#         result.append(list[temp])
#         del list[temp]
#     return result


# list = [1, 2, 3, 4, 5, 6, 7]
# mixed_list = mixing_list(list)
# print(mix_list)

#Решение через функцию шафл
import random
n = int(input('Enter razmer spiska: '))
default_list = list([random.randint(10, 99) for i in range(0, n)])
print(f'Список до перемешиваения: \t{default_list}')
random.shuffle(default_list)
print(f'Список после перемешиваения: \t{default_list}')