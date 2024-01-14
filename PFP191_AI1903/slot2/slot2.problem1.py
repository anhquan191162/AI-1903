def calculate_arr_avg(arr):
    avg = sum(arr) / len(arr)
    
    
    min_diff = float('inf')
    index = -1


    for i, num in enumerate(arr):
        diff = abs(avg - num)

        if diff < min_diff:
            min_diff = diff
            index = i
    return index


arr = [int(x) for x in input("Nhap mang cach deu bang dau cach: ").split()]
index = calculate_arr_avg(arr)
print(f"The element nearest to the average is at position {index+1}")
