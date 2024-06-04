def solve(arr:list):
    arr2 = sorted(arr)
    sum = 1
    for i in range(len(arr2)):
        if arr2[i] <= sum:
            sum += arr2[i]
        else:
            break
    return sum
    
    
    
        


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    print(solve(arr))
