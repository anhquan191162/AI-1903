
def multiplication_and_sum(a, b):
   

    multiplication = a * b
    print(f"The multiplication of a and b = {multiplication} ")
    sum = a + b
    print(f"The sum of a and b = {sum}")
    

a = float(input("Enter first value: "))
b = float(input("Enter second value: "))
multiplication_and_sum(a, b)


prev_num = 0

for i in range(0,10):
    sum = prev_num + i
    print(f"Current number: {i} Previous number: {prev_num} Sum: {sum} ")
    
    prev_num = i
    