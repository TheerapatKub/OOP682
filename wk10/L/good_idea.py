# LSP (Liskov Substitution Principle) 
# กล่าวว่า วัตถุของซับคลาสควรจะสามารถแทนที่วัตถุของซูเปอร์คลาสได้โดยไม่ทำให้โปรแกรมทำงานผิดพลาด  
# Good Idea of LSP Adherence
from abc import abstractmethod
class Shape:
    @abstractmethod
    def resize(self, new_width, new_height): pass
    @abstractmethod
    def area(self): pass
class Rectangle(Shape): # สี่เหลี่ยม
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
    def area(self):
        return self.width * self.height
class Square(Shape): # จัตุรัส
    def __init__(self, side):
        self.side = side
    def resize(self, new_width, new_height):
        self.side = new_width  # จัตุรัสมีความกว้างและความสูงเท่ากัน ดังนั้นการเปลี่ยนความกว้างก็จะเปลี่ยนความสูงด้วย
    def area(self):
        return self.side * self.side
def resize(shape, new_width, new_height):
    shape.resize(new_width, new_height)
    return shape.area()
rect = Rectangle(2, 3)
resize(rect, 4, 5)
print("Rectangle area:", rect.area()) 
square = Square(3)
resize(square, 4, 5)
print("Square area:", square.area())  