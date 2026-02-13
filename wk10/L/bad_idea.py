# LSP (Liskov Substitution Principle) 
# กล่าวว่า วัตถุของซับคลาสควรจะสามารถแทนที่วัตถุของซูเปอร์คลาสได้โดยไม่ทำให้โปรแกรมทำงานผิดพลาด  
# Bad Idea of LSP Violation
class Rectangle: # สี่เหลี่ยม
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
class Square(Rectangle): # จัตุรัส
    def __init__(self, side):
        super().__init__(side, side)
    def set_width(self, width):
        self.width = width
        self.height = width  # ผิดหลัก LSP เพราะการตั้งค่าความกว้างจะเปลี่ยนความสูงด้วย
    def set_height(self, height):
        self.height = height
        self.width = height  # ผิดหลัก LSP เพราะการตั้งค่าความสูงจะเปลี่ยนความกว้างด้วย
def resize_rectangle(rectangle, new_width, new_height):
    rectangle.set_height(new_height)
    rectangle.set_width(new_width)
    return rectangle.width * rectangle.height

rect = Rectangle(2, 3)
print("Rectangle area:", resize_rectangle(rect, 4, 5)) 
square = Square(4)
print("Square area:", resize_rectangle(square, 4, 5))  