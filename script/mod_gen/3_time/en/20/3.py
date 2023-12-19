def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) < 2:
        return 0
    
    dp = [[0 for _ in range(3)] for _ in range(len(prices))]
    dp[0][0] = -prices[0]
    dp[1][0] = max(dp[0][0], -prices[1])
    dp[1][1] = max(dp[0][1], dp[0][0] + prices[1])
    dp[1][2] = 0
    for i in range(2, len(prices)):
        dp[i][0] = max(dp[i-1][0], dp[i-2][1] - prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        dp[i][2] = max(dp[i-1][2], dp[i-1][1])
    return max(dp[-1][1], dp[-1][2])

if __name__ == '__main__':
    maxProfit()