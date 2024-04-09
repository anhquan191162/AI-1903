def factorial(n : int):
    while n>=0:
        if n == 1 or n == 0:
            return 1
        else:
            return n*factorial(n-1)
    else:
        print("Value is smaller than 0 or not an int.")

n = 5
print(factorial(n))