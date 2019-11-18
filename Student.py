from Person import Person

class Student(Person):
    def __init__(self, first, last, age, major):
        super().__init__(first, last, age)
        self.major = major

    def description(self):
        return super().description() + " " + self.major
