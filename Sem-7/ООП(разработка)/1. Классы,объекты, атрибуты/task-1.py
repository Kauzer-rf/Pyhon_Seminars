class Lada:
    # атрибуты класса
    n_of_wheels = 4
    rule = 1

    def __init__(self, color, engine):  # встроенный метод, под копотом класса
        self.color = color
        self.engine = engine

    def method(self):
        print(Lada.rule)
        print(self.rule)
        self.rule = 2
        print(Lada.rule)
        print(self.rule)
        print(self.color)


obj = Lada('red', 'gas')
print(obj.color)
obj.color = 'grey'
print(obj.color)
print(obj.n_of_wheels)

n_of_wheels = 5
print(obj.n_of_wheels)
