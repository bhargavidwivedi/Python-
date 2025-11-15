import math
class Circle:
    def __init__(self, r):
        self.radius = r
    
    def Area(self):
        self.area = 2 * math.pi * (self.radius ** 2)
        return self.area
    
    def Perimeter(self):
        self.perimeter = 2 * math.pi * self.radius
        return self.perimeter
    


c1 = Circle(4)
print(c1.Area())
print(c1.Perimeter())