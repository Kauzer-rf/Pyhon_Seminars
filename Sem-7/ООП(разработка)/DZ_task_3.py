"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""
import os


def cls():
    os.system('cls'if os.name == 'nt' else 'clear')


cls()

class Worker:
    # _incom = {"wage": 30000, "bonus": 10000}

    def __init__(self, name, surname, position, _incom):
            self.name = name  
            self.surname = surname  
            self.position = position
            self._incom = _incom

class Position(Worker):

    # def get_full_name(self):
    #     print(f'{self.name} {self.surname}')

    # def get_total_income(self, _incom):
    #     self.total_cash = _incom[0] + _incom[1]

    def __str__(self):
        return f'Сотрудник: {self.name} {self.surname} \nДолжность: {self.position} \nЗарплата: {self._incom}'



a = Position('Andrey','Fedotov', 'Пекарь', '40000')
print(a)