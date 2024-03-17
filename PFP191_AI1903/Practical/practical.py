def prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
            else:
                return True

lst = list(int(x) for x in input("Enter positive integers: ").split())
primelst = []
for i in lst:
    if i < 0:
        print(f"Invalid. {i} is not a positive integers.")
    else:
        if prime(i):
            primelst.append(i)

print(primelst)
print(max(primelst))




            
            

