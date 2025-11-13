
def even_number():
    total_sum = 0
    for i in range(0, 11):
     if   i % 2 == 0:
       total_sum += i
     print(f"Sum of {i} is {total_sum}")
even_number()

