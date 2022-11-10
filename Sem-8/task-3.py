"""__STR__"""

class MyClass:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2
    def  __str__(self):
        return f'Удаляем объекты {self.param_1}, {self.param_2} класса MyClass'

mc = MyClass('text_1', 'text_2')
print(mc)