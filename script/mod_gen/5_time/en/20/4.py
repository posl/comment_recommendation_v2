def maxProfit(prices):
    if len(prices) < 2:
        return 0
    dp = [[0 for _ in range(len(prices))] for _ in range(3)]
    dp[0][0] = -prices[0]
    dp[1][0] = 0
    dp[2][0] = 0
    for i in range(1, len(prices)):
        dp[0][i] = max(dp[0][i - 1], dp[2][i - 1] - prices[i])
        dp[1][i] = dp[0][i - 1] + prices[i]
        dp[2][i] = max(dp[1][i - 1], dp[2][i - 1])
    return max(dp[1][-1], dp[2][-1])

if __name__ == '__main__':
    maxProfit()