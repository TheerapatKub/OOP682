# Open-Closed Principle (OCP) states that software entities 
# (classes, modules, functions, etc.) 
# should be open for extension but closed for modification. 
# This means that you should be able to add new functionality 
# to a class without changing its existing code.

# Bad Idea of OCP Violation
class Circle: # วงกลม
    def __init__(self, radius):
        self.radius = radius

class Rectangle: # สี่เหลี่ยม
    def __init__(self, width, height):
        self.width = width
        self.height = height
# class Triangle: # สามเหลี่ยม
#     def __init__(self, base, height):
def calculate_area(shape): # คำนวณพื้นที่
    if isinstance(shape, Circle):
        return 3.14 * shape.radius ** 2
    elif isinstance(shape, Rectangle):
        return shape.width * shape.height
    else:
        raise ValueError("Unknown shape")