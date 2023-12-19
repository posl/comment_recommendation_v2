def maxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0
    dp = [[0,0] for _ in range(n)]
    # dp[i][0] means the profit in day i without stock in hand
    # dp[i][1] means the profit in day i with stock in hand
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    for i in range(1,n):
        # if you don't have stock in hand in day i, you can choose to buy or not buy
        # if you buy, the profit will be dp[i-1][0]-prices[i]
        # if you don't buy, the profit will be dp[i-1][0]
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
        # if you have stock in hand in day i, you can choose to sell or not sell
        # if you sell, the profit will be dp[i-1][1]+prices[i]
        # if you don't sell, the profit will be dp[i-1][1]
        # but you cannot sell stock in day i if you buy it in day i
        dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
    return dp[-1][0]

if __name__ == '__main__':
    maxProfit()