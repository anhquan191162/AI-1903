def solve(arr:list):
    arr2 = sorted(arr,reverse=True)
    rank = {}
    top = 1
    
    m = max(arr)
    for i in range(len(arr2)):
        if arr2[i] not in rank:
            if arr2[i] == m:
                rank[arr2[i]] = 1
            else:
                top += i
                rank[arr2[i]] = top
                top = 1
        else:
            pass
    for i in arr:
        if i in rank:
            print(rank[i],end=' ')

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    solve(arr)
