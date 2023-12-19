def maxProfit(prices):
    n = len(prices)
    dp = [[0 for i in range(2)] for j in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
        if i-2 >= 0:
            dp[i][1] = max(dp[i-1][1],dp[i-2][0]-prices[i])
        else:
            dp[i][1] = max(dp[i-1][1],-prices[i])
    return dp[n-1][0]
print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))
print(maxProfit([1,2,3,0,2,1,3,2,4,5,6,3,1,5,7,2,4,6,8,9,2,4,5,7,8,9,2,4,5,6,7,8,9,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]))
