def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) < 2:
        return 0
    #dp[i][0] means the max profit at day i, if we don't have stock at day i
    #dp[i][1] means the max profit at day i, if we have stock at day i
    dp = [[0 for _ in range(2)] for _ in range(len(prices))]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    dp[1][0] = max(dp[0][0], dp[0][1]+prices[1])
    dp[1][1] = max(dp[0][1], dp[0][0]-prices[1])
    for i in range(2, len(prices)):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
    return dp[-1][0]

if __name__ == '__main__':
    maxProfit()