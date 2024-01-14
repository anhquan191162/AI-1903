def sum(n):
    res = (n*(n+1))/2
    print(f"The arithmetic progression sum with n = {n} is {res} ")

def factorial(n):
    res = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n+1):
            res = res*i
    print(f"The factorial of this value is: {res} ")        
        

def sum2(n):
    a = 1
    res = (n/2)*(1/(2*a + (n-1)*1))
    print(f"The harmonic sum with n = {n} is {res}")



while True:
        n = int(input("Enter value: "))
        if n > 5:
          sum(n)
          factorial(n)
          sum2(n)
          break

        else:
          print("Value is smaller than 5.")
          print("Re-input value: ")  
    

while True:
    n = int(input("Enter positive value bigger than 1: "))
    if n > 1:
        def prime_num_check(n):
            for i in range(2, n):
                if (n%i) == 0:
                    print(f"{n} is not a prime number")
                    print(f"{i} * {n/i} equals {n}")   
                    return False 
                    
                else:
                    print(f"{n} is a prime number")
                    return True
                       
                               
    else:
        print("Value is equal or smaller than 1.")
        print("Re-input value:")
    prime_num_check(n)







    def prime_dividers(number):
        dividers = set()
        for i in range(2, number + 1):
            while prime_num_check(i) and number % i == 0:
                dividers.add(i)
                number //= i
        return dividers
    

    def gcd(a, b):
        while b:
            a, b = b, a % b
            return a
        
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    m = int(input("Enter the first integer (m): "))
    n = int(input("Enter the second integer (n): "))
    common_dividers = prime_dividers(m) and prime_dividers(n)
    print(f"CMD = {common_dividers}")
    gcd_result = gcd(m ,n)
    print(f"GCD = {gcd_result}")
    lcm_res = lcm(m, n)
    print(f"LCM = {lcm_res}")




