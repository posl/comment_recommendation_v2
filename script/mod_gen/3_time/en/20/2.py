def maxProfit(prices):
    n = len(prices)
    dp = [[0,0] for i in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        if i == 1:
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        else:
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
    return dp[n-1][0]
print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))
print(maxProfit([1,2]))
print(maxProfit([2,1]))
print(maxProfit([2,1,2,0,1]))
print(maxProfit([2,1,4,5,2,9,7]))
print(maxProfit([2,1,4,5,2,9,7,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(maxProfit([2,1,4,5,2,9,7,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(maxProfit([2,1,4,5,2,9,7,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1]))
print(maxProfit([2,1,4,5,2,9,7,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,2,3,4,5,6,7,8,9,10,11,12,13
