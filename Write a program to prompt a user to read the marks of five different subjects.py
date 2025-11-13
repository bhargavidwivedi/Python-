
def calculate(percentage):
    if percentage >= 90:
        print("Distinction")
    elif percentage >= 80 and percentage < 90:
        print("First Class")
    elif percentage >= 70 and percentage < 80:
        print("Second Class")
    elif percentage >= 60 and percentage < 70:
        print("Pass")
    else:
        print("Fail")

percentage = float(input("Enter the percentage:"))
calculate(percentage)

