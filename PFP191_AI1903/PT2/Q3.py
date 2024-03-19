def knapsack(N, W, items):
    
    dp = [[0] * (W + 1) for _ in range(N + 1)]

   
    for i in range(1, N + 1):
        weight_i, value_i, name_i = items[i - 1]

        
        for w in range(1, W + 1):
            if weight_i <= w:
               
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight_i] + value_i)
            else:
                
                dp[i][w] = dp[i - 1][w]

    
    included_items = []
    w = W
    for i in range(N, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            weight_i, _, name_i = items[i - 1]
            included_items.append((name_i, 1))
            w -= weight_i


    return dp[N][W], included_items


with open("BAG.INP", "r") as file:
    N, W = map(int, file.readline().split())
    items = [list(map(int, line.split()[:-1])) + [line.split()[-1]] for line in file.readlines()]


max_value, included_items = knapsack(N, W, items)


print("Maximum value:", max_value)
print("Included items:")
for item in included_items:
    print(item[0], item[1])
