class Item:
    c = 'Китай'

    def __init__(self, *args):
        self.name = args[0]
        self.price = int(args[1])
        self.a = args[2]
    def get_count(self):
        self.price -= 100

obj_1 = Item('Холодильник Самсунг', '500', '20/20/20')
obj_1 = Item ('LG', '500', '20/20/20')
obj_1.new_attr = 1000
print(obj_1.__dict__)

a = 3
print(type(a))
print(type(obj_1))