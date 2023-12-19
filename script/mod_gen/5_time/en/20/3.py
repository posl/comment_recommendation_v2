def maxProfit(prices):
    if len(prices) <= 1:
        return 0
    dp = [[0]*len(prices) for _ in range(len(prices))]
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            dp[i][j] = prices[j] - prices[i]
    print(dp)
    return max(max(dp))
print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))
