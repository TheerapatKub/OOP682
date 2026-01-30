from models.Classroom import ClassRoom
from models.student import Student

oop = ClassRoom("OOP")
oop.add_student(Student("1234567890123", "Alice", 20, "S12345"))
oop.add_student(Student("2345678901234", "Bob", 22, "S67890"))
print(len(oop))
oop.add_student(Student("3", "Charlie", 21, "S54321"))
print(len(oop))
print("Students in the classroom:")
for i in range(len(oop)):
    print(oop[i])