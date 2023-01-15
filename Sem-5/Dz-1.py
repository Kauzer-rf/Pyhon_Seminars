""""
38. Напишите программу, которая удаляет 'абв' из строки.
"""
# Решение_1
# my_text = 'Прочитал абв новости абв и абв удивился.'
# find_text = "абв"
# lst = [i for i in my_text.split() if find_text not in i]
# print(f'Результат: {" ".join(lst)}')

# Решение_2
my_text = 'Прочитал абв новости абв и абв удивился.'
find_text = ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), my_text.split())))
print(find_text)
