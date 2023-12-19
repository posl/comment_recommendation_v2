def maxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0
    dp = [[0,0,0] for _ in range(n)]
    dp[0][0] = -prices[0]
    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0],dp[i-1][2]-prices[i])
        dp[i][1] = dp[i-1][0]+prices[i]
        dp[i][2] = max(dp[i-1][1],dp[i-1][2])
    return max(dp[n-1][1],dp[n-1][2])
print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))
print(maxProfit([1,2]))
print(maxProfit([2,1]))
print(maxProfit([2,1,4]))
print(maxProfit([2,1,4,5]))
print(maxProfit([2,1,4,5,2]))
print(maxProfit([2,1,4,5,2,9]))
print(maxProfit([2,1,4,5,2,9,7]))
print(maxProfit([2,1,4,5,2,9,7,1]))
print(maxProfit([2,1,4,5,2,9,7,1,3]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5,2]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5,2,6]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5,2,6,3]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5,2,6,3,7]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5,2,6,3,7,3]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5,2,6,3,7,3,6
