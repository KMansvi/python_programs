import math
class Circle:
    def __init__(self, radius):
            self.radius=radius
    def calculatearea(self):
            return math.pi*self.radius**2
    def calculateperimeter(self):
            return math.pi*2*self.radius
radius=float(input("Enter the radius:"))
circle=Circle(radius)
area=circle.calculatearea()
perimeter=circle.calculateperimeter()
print("Area of the circle is:",area)
print("Area of the circle is:",perimeter)
