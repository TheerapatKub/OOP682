class Person:
    def __init__(self, pid, name, age):
        self.pid = pid
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age})"

class Student(Person):
    def __init__(self, pid, name, age, student_id):
        super().__init__(pid, name, age)
        self.student_id = student_id
    def __str__(self):
        return super().__str__() + f", Student ID: {self.student_id}"


class Staff(Person):
    def __init__(self, pid, name, age, staff_id):
        super().__init__(pid, name, age)
        self.staff_id = staff_id
    def __str__(self):
        return super().__str__() + f", Staff ID: {self.staff_id}"

person = Person(1234567890123, "John Doe", 30)
student = Student(1234567890123, "Alice", 28, "S12345")
staff = Staff(2345678901234, "Bob", 35, "ST6789")
print(person)
print(student)
print(staff)    

def get_person_info(person):
    print(isinstance(person, Person))
    return f"Name: {person.name}, Age: {person.age}"


if __name__ == "__main__":
    student = Student(1234567890123, "Alice", 28, "5123")
    staff = Staff(2345678901234, "Bob", 35, "ST456")

    print(f"Student: {student.name}, Age: {student.age}, Student ID: {student.student_id}")
    print(f"Staff: {staff.name}, Age: {staff.age}, Staff ID: {staff.staff_id}")

    print(get_person_info(student))
    print(get_person_info(staff))

    get_person_info(student)
    get_person_info(staff)




