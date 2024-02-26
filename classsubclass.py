import math
class shape:
    def calculatearea(self):
        pass
    def calculateperimeter(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def calculatearea(self):
        return math.pi*self.radius**2
    def calculateperimeter(self):
        return math.pi*2*self.radius
class rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def calculatearea(self):
        return self.l*self.b
    def calculateperimeter(self):
        return 2*(self.l+self.b)
class triangle(shape):
    def __init__(self,base,h,s1,s2,s3):
        self.base=base
        self.h=h
        self.s1=s1
        self.s2=s2
        self.s3=s3
    def calculatearea(self):
        return 0.5*self.base*self.h
    def calculateperimeter(self):
        return self.s1+self.s2+self.s3

r=int(input())
l=int(input())
b=int(input())
base=int(input())
h=int(input())
s1=int(input())
s2=int(input())
s3=int(input())
c=circle(r)
rec=rectangle(l,b)
tri=triangle(base,h,s1,s2,s3)
circlearea=c.calculatearea()
circleperimeter=c.calculateperimeter()
recarea=rec.calculatearea()
recperimeter=rec.calculateperimeter()
triarea=tri.calculatearea()
triperimeter=tri.calculateperimeter()
print("The area of circle is:",circlearea)
print("The perimeter of circle is:",circleperimeter)
print("The area of rectangle is:",recarea)
print("The perimeter of rectangle is:",recperimeter)
print("The area of triangle is:",triarea)
print("The perimeter of triangle is:",triperimeter)
