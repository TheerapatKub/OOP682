from week9.moduls.person import Person
from moduls.person import Person

class Student(Person):
    def __init__(self, pid, name, age, student_id):
        super().__init__(pid, name, age)
        self.student_id = student_id

    def __str__(self):
        return super().__str__() + f", Student ID: {self.student_id}"