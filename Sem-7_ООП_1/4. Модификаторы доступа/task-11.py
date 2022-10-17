# Наследование

class User:
    name = None
    surname = None

    def get_name(self):
        self.name = 'Ivanov'
        print(self.name)

class Teacher(User):
    pass
    def get_name(self):
        pass

class Student(User):
    pass

obj = Student()
    