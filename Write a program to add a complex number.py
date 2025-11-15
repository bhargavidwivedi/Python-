
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self,num1):
        newReal = self.real + num1.real
        newImg = self.img + num1.img
        return Complex(newReal, newImg)
    
num1 = Complex(2,4)
num1.showNumber()
num1.__add__(num1)
num2 = Complex(3,5)
num2.showNumber()
num2.__add__(num2)

num3 = num1 + num2
num3.showNumber()
