def maxProfit(prices):
    print(prices)
    n = len(prices)
    if n == 1:
        return 0
    dp = [[0 for x in range(2)] for x in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
    dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])
    for i in range(2, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
    print(dp)
    return dp[n-1][0]
print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))
print(maxProfit([1,2,4]))
print(maxProfit([1,2,3,0,2,1,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]))
print(maxProfit([1,2,3,0,2,1,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]))
print(maxProfit([1,2,3,0,2,1,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1]))
print(maxProfit([1,2,3,0,2,1,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2]))
print(maxProfit([1,2,3,0,2,1,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3]))
print(max

if __name__ == '__main__':
    maxProfit()