def list_maker():
    L = list(x for x in input("Enter any value, char: ").split())
    print(L)

list_maker()

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

def concatenate(list1, list2):
    list3 = []
    i = 0 
    while i <= len(list1) -1  :
        new_ele = list1[i] + list2[i]

        list3.append(new_ele)
        i +=1
    return list3

print(concatenate(list1, list2))


