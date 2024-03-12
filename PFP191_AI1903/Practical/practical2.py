lst = list(int(x) for x in input("Enter integers: ").split())
def cal_sum(list):

    i = 0
    while i < len(list):
        
        left_sum = sum(list[0:i])
        right_sum = sum(list[i+1:int(len(list))])
        if left_sum == right_sum:
            return f"Yes,{i}"
        else:

            i += 1
    return f'No'

print(cal_sum(lst))

