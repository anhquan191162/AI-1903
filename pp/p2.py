def binary_search(A:list, target:int):
    low = 0
    high = len(A)-1
    while low <= high:
        mid = int(low + ((high-low)/2))
        if A[mid] == target:
            return mid
        if A[mid] < target:
            low = mid + 1
        if A[mid] > target:
            high = mid - 1


    return -1

print(binary_search([2, 14, 16,17,19,23,29], 23))


'''def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)'''




