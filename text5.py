class Person:
    name = 'Nurs'
    age = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set(self, name, age):
        self.name = name
        self.age = age

class Student (Person):
    course = 1

    def set(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

igor = Student("Вася", 19)
# igor._Person__set('igor', 19)
igor.set('Игорь', 23, 5)
print('Имя:', igor.name, 'Возраст -', igor.age, 'Курс - ', igor.course)


vlad = Person('Влад', 25)
# vlad._Person__set('Влад', 25)
print(vlad.name + ' ' + str(vlad.age))

nurs = Person('Нурс', 17)
# nurs._Person__set('Нурс', 17)
print(nurs.age)
