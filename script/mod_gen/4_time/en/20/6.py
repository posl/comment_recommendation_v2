def maxProfit(prices):
    n = len(prices)
    dp = [[0 for i in range(2)] for j in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        if i >= 2:
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        else:
            dp[i][1] = max(dp[i-1][1], -prices[i])
    return dp[n-1][0]

if __name__ == '__main__':
    maxProfit()