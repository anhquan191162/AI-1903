
    
    
numbers = [1,2,3,4,5,6,7]
numbers = [int(numbers[i])**2 for i in range(len(numbers))]
print(numbers)


L4 = ["Hello", "take"]
L5 = ["Dear", "Sir"]

def concatenate(list1, list2):
    newL = []
    
    newL.append((list1[i] for i in range(len(list1)))+ (list2[j]) for j in range(len(list2)))
    return newL
    

print(concatenate(L4, L5))
