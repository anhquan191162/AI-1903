arr = [int(x) for x in input("Enter values for an array seperated by blank: ").split()]

print(f"Original sequence: {arr}")


def prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

def indicate_primes(num):
    prime_indicator = []
    for i in num:
        if prime(i):
            prime_indicator.append(i)
        else:
            pass
    return prime_indicator

prime_list = indicate_primes(arr)
print(f"Prime list: {prime_list}")
print(f"Largest prime: {max(prime_list)}")
print(f"Sum of list: {sum(prime_list)}")

            
        





