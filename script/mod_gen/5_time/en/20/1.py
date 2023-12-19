def maxProfit(prices):
    n = len(prices)
    if n == 1:
        return 0
    dp = [[0 for _ in range(2)] for _ in range(n)]
    dp[0][0], dp[0][1] = 0, -prices[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        if i == 1:
            dp[i][1] = max(dp[i-1][1], -prices[i])
        else:
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
    return dp[n-1][0]

if __name__ == '__main__':
    maxProfit()