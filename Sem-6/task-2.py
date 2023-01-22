# 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# *Пример:*
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# my_list = [2, 4, 7, 8, 34, 90, -34, 2, 7, -90, 7] #2 и 7
# print(my_list)
# my_new_list = []
# for i in range(0, len(my_list)):
#     for j in range(i+1, len(my_list)):
#         if my_list[i] == my_list[j]:
#             my_new_list.append(my_list[j])
# print(my_new_list) 

my_list = [1, 2, 3, 5, 1, 5, 3, 10]
print(my_list)

my_set = list(set(my_list))
print(my_set)