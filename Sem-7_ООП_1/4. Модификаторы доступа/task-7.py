class Auto:
    def __init__(self):
        self.auto_name = 'Mazda'  # публичный атрибут
        self._auto_year = 2019    # _ это защищенный атрибут, для служебного пользования
        self.__auto_model = 'CX9' # __ это приватный атрибут

    def func(self):
        print(self._auto_year)
        self.__auto_model = 2020

a = Auto()
# print(a.__auto_model) работать не будет т.к. не доступа.
print(a._Auto__auto_model) # Обход формальной инкасуляции Питона.

# В данном коде есть атрибут __auto_model, являющий приватным.
# Он инкапсулирован в класс Auto и не может быть вызван вне его.