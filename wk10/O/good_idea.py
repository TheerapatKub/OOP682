# Open-Closed Principle (OCP) states that software entities 
# (classes, modules, functions, etc.) 
# should be open for extension but closed for modification. 
# หมายถึง คุณควรจะสามารถเพิ่มฟังก์ชันใหม่ให้กับคลาสได้โดยไม่ต้องเปลี่ยนแปลงโค้ดที่มีอยู่แล้ว

# Good Idea of OCP Adherence
from abc import abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape): # วงกลม
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape): # สี่เหลี่ยม
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

def calculate_area(shape): # คำนวณพื้นที่
    return shape.area()