
def math_operators(a,b):
    print("Addition:", a+b)
    print("Substraction:", a-b)
    print("Multiplication:", a*b)
    if b != 0:
        print("Division:", a/b)
    else:
        print("Division undefined")

num1 = float(input("Enter the number:"))
num2 = float(input("Enter the number:"))
math_operators(num1, num2)