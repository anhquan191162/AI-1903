def fibonacci(n):
    if n<0:
        return -1
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


lst = [41, 32, 8, 15, 24, 28, 11, 10, 58, 31, 7]
lst.sort()
print(lst)


def even_odd(num):
    if num % 2 == 0:
        return "is even"
    else:
        return "is odd"
    



            



    