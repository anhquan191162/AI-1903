import math



def quadratic_equation(a, b, c, x):
    S1 = a*x**2 + b*x + c
    print(f"for a , b , c , x the value for a quadratic equation = {S1}")

def quadratic_formula(a, b, c, x):
    S2 = math.sqrt(b**2 - 4*a*c)

    if S2 > 0:
        
    

    
        solution1 = (-b + math.sqrt(S2)) / 2*a
        solution2 = (-b - math.sqrt(S2)) / 2*a
        print(f"S2 = {S2}")
        print(f"There exist 2 unique solutions x ={solution1} and x = {solution2}")
    elif S2 == 0:
        solution3 = -b/a
        print(f"There exist only one solution x = {solution3}")
    if S2 < 0 :
    
        print("No solution")

""""
def triangle_check(a, b, c):
    a1 = int(input("Enter first side: "))
    a2 = int(input("Enter second side: "))
    a3 = int(input("Enter third side: "))
    triangle = list(a, b, c)
    def largest_value(triangle, n):
        max_value = [0]

        for i in range(1, n):
            if triangle[i] > max_value:
                max_value = triangle[i]
            return max_value
"""


   



a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))
x = int(input("Enter x: "))    
quadratic_formula(a, b, c, x)
quadratic_equation(a, b, c, x)





a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))


if a + b > c and b + c > a and c + a > b:
    
    perimeter = a + b + c
    print(f"The perimeter of the triangle is {perimeter}")

    
    s = perimeter / 2

    
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"The area of the triangle is {area}")
else:
    print("a, b, c are not sides of a triangle")



a = float(input("Enter value: "))
b = float(input("Enter value: "))
c = float(input("Enter value: "))

num_list = [a, b, c]
max_value = max(num_list)
sorted_list = sorted(num_list)
print(num_list)
print(f"The max value is {max_value}")
print("Arranged list :", sorted_list )
