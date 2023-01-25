class MyClass:
    __attr = 'value'
    def __method(self):
        print('This is private method!')

mc = MyClass()
mc.__method()
print(mc.__attr)

# Инкапсуляция метода