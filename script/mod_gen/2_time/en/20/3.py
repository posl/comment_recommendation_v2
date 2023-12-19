def maxProfit(prices):
    n = len(prices)
    if n < 2:
        return 0
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = 0
    dp[1][0] = -prices[0]
    for i in range(1, n):
        dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + prices[i])
        dp[1][i] = max(dp[1][i - 1], dp[0][i - 2] - prices[i])
    return dp[0][n - 1]
prices = [1,2,3,0,2]
print(maxProfit(prices))
prices = [1]
print(maxProfit(prices))
