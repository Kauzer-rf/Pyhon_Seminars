# 21.	Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:
# •	список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# •	список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# •	список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# •	список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# •	список: [], ищем: "123", ответ: -1

find = 'qwe'
my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]


def second_in(list, find):
    count = 0
    for i in range(len(list)):
        if list[i] == find:
            count += 1
            if count == 2:
                return i
    return -1


print(f'Номер индекса 2-ого вхождения: {second_in(my_list, find)}')

# Решение 2
# my_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# print(my_list)

# string_find = "йцу"
# count = 0
# for i in range(len(my_list)):
#     if string_find == my_list[i]:
#         count += 1
#         if count == 2:
#             print(i)
#             break
# else:
#     print(-1)
