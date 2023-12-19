def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0
    n = len(prices)
    dp = [[0 for _ in range(2)] for _ in range(n)]
    for i in range(n):
        if i == 0:
            dp[i][0] = 0
            dp[i][1] = -prices[i]
            continue
        if i == 1:
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
            continue
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
    return dp[n-1][0]
prices = [1,2,3,0,2]
print(maxProfit(prices))
