def binary_search(arr, low, high, x):
    high = len(arr) - 1
    mid = 0 
    low = 0
    if high >= low:
        mid = (high + low)//2

        if arr[mid] == x:
            return x
        
        elif arr[mid] > x:
            low = mid - 1
        
        else:
            return mid
    
    
