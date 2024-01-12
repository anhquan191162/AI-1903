def func1(a, b, c):
    print("Printing values:")
    print(a)
    print(b)
    print(c)

func1(20, 40 ,60)


def func2(c, d):
    print("Printing values:")
    print(c)
    print(d)

func2(80, 100)


def calculation(a, b):
    a = a + 10

    b = b + 20
    return a, b

res = calculation(40, 10)
print(res)

def showEmployee(e, salary = 9000 ):


    
    
    
    
    print(f"Name: {e}, Salary: {salary}")    

showEmployee("Ben", 12000)
showEmployee("Jessa")


def func(a, b):
    result = a + b
    result = result + 5
    return result

result = func(5, 10)
print(result)

def additional(n):
    

    sum = (n*(n+1))/2
    print(sum)

additional(5)


n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
    


