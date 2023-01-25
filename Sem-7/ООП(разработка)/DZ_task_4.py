"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

import os


def cls():
    os.system('cls'if os.name == 'nt' else 'clear')


cls()


class Car:
    def __init__(self, color, name, is_police, speed):
        self.color = color
        self.name = name
        self.is_police = False
        self.speed = speed

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        print('Машина повернула')

    def show_speed(self):
        print(f'Скорость авто: ')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость TownCar: {self.speed}. Превышение!!!')
        else:
            print(f'Скорость TownCar: {self.speed}.')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость Work авто: {self.speed}. Превышение!!!')
        else:
            print(f'Скорость Work авто: {self.speed}.')


# class PoliceCar(Car):
# class SportCar(Car):
