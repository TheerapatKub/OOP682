class Dog:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name} is {self.age} years old.")


    def __str__(self):
        return f"Dog(Name: {self.name}, Age: {self.age})"
    
def main():
    my_dog = Dog("Buddy", 3)
    my_dog.info()
    your_dog = Dog("Paulie", 5)
    your_dog.info()


if __name__ == "__main__":
        main()
