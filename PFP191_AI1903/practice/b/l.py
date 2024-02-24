def check_positive_integers(list):
    
    for elem in list:
        if type(elem) is not int or elem < 1:
            print("There is an element that is not an integer or is smaller than 1.")
            break
    return list


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n%i== 0:
            return False
        
    return n
        
    
   

lst = list(int(x) for x in input("Enter values bigger than 1: ").split())
check_positive_integers(lst)
new_lst = []
for i in lst:
    if is_prime(i):
        new_lst.append(i)
    else:
        pass
    
print(lst)
print(new_lst)
print(max(new_lst))
print(sum(new_lst))

