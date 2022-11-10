""" __eq__"""

class MyClass:
    def __init__(self):
        self.x = 40
    def __eq__(self, y):
        print('!')

mc = MyClass()
print('Ravno' if mc == 40 else 'Ne ravno')
print('Ravno' if mc == 41 else 'Ne ravno')