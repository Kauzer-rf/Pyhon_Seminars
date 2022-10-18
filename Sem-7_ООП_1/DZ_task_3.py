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


class Worker:
    def __init__(self):
        self.name = input('Введите имя сотрудника: ')
        self.surname = input('Введите фамилию сотрудника: ')
        self.position = None
        self._incom = {
            "wage": 30000,
            "bonus": 10000,
        }


class Position(Worker):
    def __init__(self, name, surname, _incom):
        super().__init__(name, surname, _incom)

    def get_full_name(self, name, surname):
        return f'Имя сотрудника: {name}, его фамилия: {surname}'

    def get_total_income(self, _incom):
        self.total_cash = _incom[0] + _incom[1]
        return f'ЗП составляет: {self.total_cash} рублей, с учетом премии.'


a = Position()

a.get_full_name()
a.get_total_income()
