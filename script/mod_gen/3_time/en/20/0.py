def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 1:
        return 0
    if len(prices) == 2:
        return max(0, prices[1] - prices[0])
    dp = [[0, 0] for _ in range(len(prices))]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    dp[1][0] = max(0, prices[1] - prices[0])
    dp[1][1] = max(-prices[0], -prices[1])
    for i in range(2, len(prices)):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 2][0] - prices[i], dp[i - 1][1])
    return dp[-1][0]

if __name__ == '__main__':
    maxProfit()