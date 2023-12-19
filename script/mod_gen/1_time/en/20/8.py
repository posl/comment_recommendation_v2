def maxProfit(prices):
    n = len(prices)
    if n == 1:
        return 0
    buy = [0]*n
    sell = [0]*n
    buy[0] = -prices[0]
    buy[1] = max(-prices[0], -prices[1])
    sell[1] = max(0, prices[1]-prices[0])
    for i in range(2, n):
        buy[i] = max(buy[i-1], sell[i-2]-prices[i])
        sell[i] = max(sell[i-1], buy[i-1]+prices[i])
    return sell[n-1]
prices = [1,2,3,0,2]
print(maxProfit(prices))
