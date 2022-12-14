"""
Задание 2.
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""
import os


def cls():
    os.system('cls'if os.name == 'nt' else 'clear')


cls()

class Road:
    default_mass = 25
    _length = int(input('Введите длину дороги в метрах: '))
    _width = int(input('Введите ширину дороги в метрах: '))

    def get_mass(self):
        self.find_mass = self._length * self._width * self.default_mass * 0.05
        print(
            f'На дорогу с указанными параметрами понадобится: {self.find_mass} кг асфальта')


a = Road()
a.get_mass()
