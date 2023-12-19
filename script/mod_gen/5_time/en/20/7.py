def maxProfit(prices):
    n = len(prices)
    buy = [0] * (n+1)
    sell = [0] * (n+1)
    buy[1] = -prices[0]
    for i in range(2, n+1):
        buy[i] = max(buy[i-1], sell[i-2] - prices[i-1])
        sell[i] = max(sell[i-1], buy[i-1] + prices[i-1])
    return sell[n]
print(maxProfit([1,2,3,0,2]))
