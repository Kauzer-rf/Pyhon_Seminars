""""
Напишите программу, которая удаляет 'абв' из строки.
"""

my_text = 'Прочитал абв новоабвсти иабв удивился.'
def del_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_words(my_text)
print(my_text)
