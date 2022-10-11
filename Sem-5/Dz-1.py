""""
Напишите программу, которая удаляет 'абв' из строки.
"""

my_text = 'Прочитал абв новости абв и абв удивился.'
find_text = "абв"
lst = [i for i in my_text.split() if find_text not in i]
print(f'Результат: {" ".join(lst)}')