
def greatest(a,b,c,d):
    if a >= b and a >= c and a >= d:
        print("a is greatest")
    elif b >= a and b >= c and b >= d:
        print("b is greatest")
    elif c >= a and c >= b and c >= d:
        print("c is greatest")
    else:
        print("Invalid")


a = float(input("Enter the number:"))
b = float(input("Enter the number:"))
c = float(input("Enter the number:"))
d = float(input("Enter the number:"))
greatest(a,b,c,d)
