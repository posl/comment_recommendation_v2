def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    dp = [[0 for i in range(3)] for j in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    dp[0][2] = 0
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][2])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        dp[i][2] = dp[i-1][1] + prices[i]
    return max(dp[n-1][0], dp[n-1][2])
print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))
print(maxProfit([1,2,4]))
print(maxProfit([2,1,2,0,1]))
print("The values above should be 3, 0, 3, and 2.")

if __name__ == '__main__':
    prices = list(map(int, input().split()))
    a = maxProfit(prices)
    print(a)