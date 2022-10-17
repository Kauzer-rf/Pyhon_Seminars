"""
Задание 1.
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

import time


class TrafficLight:
    __color = 'Red'

    # def __running__(self):
    #     self.__color = 'Red'
    #     time.sleep(7)

    #     self.__color = 'Yellow'
    #     time.sleep(2)

    #     self.__color = 'Green'
    #     time.sleep(5)
    def __running__(self):
        print('Red')
        time.sleep(7)

        print('Yellow')
        time.sleep(2)

        print('Green')
        time.sleep(5)

a = TrafficLight()
a.__running__()
# print(a.__color)
