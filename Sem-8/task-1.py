"""__init__ используется когда нужно сделать перегрузку с вводом параметра"""

class MyClass:
    def __init__(self, param):
        self.param = param

obj = MyClass(1)