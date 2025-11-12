import math
def area_circum(radius):
    if radius > 0:
        circumference = 2*math.pi*radius
        print("Circumference:", circumference)
        area = 2*radius
        print("Area:", area)
    else:
        print("Not Defined")
radius = float(input("Enter the number:"))

area_circum(radius)

