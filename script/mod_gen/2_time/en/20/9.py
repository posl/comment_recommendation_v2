def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # dynamic programming
    # dp[i] is the max profit of day i
    # dp[i] = max(dp[i-1], dp[i-2] + prices[i] - prices[i-1])
    # dp[0] = 0
    # dp[1] = max(0, prices[1] - prices[0])
    # dp[2] = max(dp[1], dp[0] + prices[2] - prices[1])
    # dp[3] = max(dp[2], dp[1] + prices[3] - prices[2])
    # ...
    # dp[n] = max(dp[n-1], dp[n-2] + prices[n] - prices[n-1])
    #
    # dp[n] = max(dp[n-1], dp[n-3] + prices[n] - prices[n-1])
    # dp[n] = max(dp[n-1], dp[n-3] + prices[n] - prices[n-1])
    # dp[n] = max(dp[n-1], dp[n-3] + prices[n] - prices[n-1])
    if len(prices) <= 1:
        return 0
    elif len(prices) == 2:
        return max(0, prices[1] - prices[0])
    elif len(prices) == 3:
        return max(max(0, prices[1] - prices[0]), max(0, prices[2] - prices[1]), max(0, prices[2] - prices[0]))
    dp = [0] * len(prices)
    dp[0] = 0
    dp[1] = max(0, prices[1] - prices[0])
    dp[2] = max(dp[1], dp[0] + prices[2] - prices[1])
    for i in range(3, len(prices)):
        dp[i] = max(dp[i-1], dp[i-3] + prices[i] - prices[i-1])
    return dp[-1]
print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))
print(maxProfit([1,2,3,0,2,1,4
