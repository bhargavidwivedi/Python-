
def cal_square(number):
    for i in range(1, 6):
        square = i ** 2
        print(f"Square of {i} is {square}")
number = float(input("Enter the number:"))
cal_square(number)