tuple1 = ("Orange", [10,20,30], (5,15,25))
print(tuple1[1][1])

tuple11 = (10,20,30,40)
def print_tuple_ele(tuple):
    i = int(input(f"Enter index from 0 to {len(tuple)}: "))
    if i not in range(4):
        print("Out of range")
        return print_tuple_ele(tuple)
    else:
        print(tuple[i])
    '''return print_tuple_ele(tuple)'''
    

print_tuple_ele(tuple11)
    

tuple22 = (11, 22)
tuple2 =  (99, 88)
print(tuple22)
print(tuple2)
tuple22, tuple2 = tuple2, tuple22
print(tuple22)
print(tuple2)