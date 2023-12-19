def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    if n <= 1:
        return 0
    dp = [0] * n
    for i in range(1, n):
        for j in range(i):
            if j >= 2:
                dp[i] = max(dp[i], dp[j] + prices[i] - prices[j] + dp[j - 2])
            else:
                dp[i] = max(dp[i], prices[i] - prices[j])
        dp[i] = max(dp[i], dp[i - 1])
    return dp[-1]

if __name__ == '__main__':
    maxProfit()