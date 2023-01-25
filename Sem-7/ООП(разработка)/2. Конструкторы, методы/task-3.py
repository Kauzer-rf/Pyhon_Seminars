class Auto:
    # атрибуты класса
    auto_count = 0

    # методы класса

    def __init__(self):
        self.auto_count += 1
    def __add__(self, other):
        return self.auto_count + other.auto_count
    def __mul__(self, other):
        return self.auto_count * other.auto_count
    def __str__(self):
        return 'это объект класса'

a_1 = Auto()
print(a_1)