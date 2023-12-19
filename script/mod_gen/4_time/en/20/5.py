def maxProfit(prices):
    n = len(prices)
    if n < 2:
        return 0
    if n == 2:
        return max(0, prices[1] - prices[0])
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[1][0] = -prices[0]
    dp[1][1] = max(-prices[0], -prices[1])
    for i in range(2, n):
        dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + prices[i])
        dp[1][i] = max(dp[1][i - 1], dp[0][i - 2] - prices[i])
    return dp[0][n - 1]

if __name__ == '__main__':
    maxProfit()