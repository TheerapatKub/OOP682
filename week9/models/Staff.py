from models.person import Person

class Staff(Person):
    def __init__(self, pid, name, age, staff_id):
        super().__init__(pid, name, age)
        self.staff_id = staff_id

    def __str__(self):
        return super().__str__() + f", Staff ID: {self.staff_id}"