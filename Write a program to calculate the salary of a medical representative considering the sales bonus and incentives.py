
def calculate(sales):
    if sales >= 100000:
       conveyance = 500
       bonus = 1000
       basic = 4000
       hra = 0.20 * basic
       da = 0.10 * basic
       incentive = 0.10 * sales
    else:
        conveyance = 500
        bonus = 500
        basic = 4000
        hra = 0.10 * basic
        da = 0.10 * basic
        incentive = 0.04 * sales
       
        total_salary = basic + bonus + conveyance + hra + da + incentive
        print("Total Salary:", total_salary)
        print("Conveyance:", conveyance)
        print("Bonus:", bonus)
        print("Basic:", basic)
        print("HRA:", hra)
        print("DA:", da)
        print("Incentive:", incentive)

sales = float(input("Enter the sale:"))
calculate(sales)






    


       
