
    
    
numbers = [1,2,3,4,5,6,7]
numbers = [int(numbers[i])**2 for i in range(len(numbers))]
print(numbers)


L4 = ["Hello", "take"]
L5 = ["Dear", "Sir"]
L6 = []
for i in L4:
    for j in L5:
        L6.append(i + j)
print(L6)
