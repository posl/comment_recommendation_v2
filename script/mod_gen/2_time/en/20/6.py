def maxProfit(prices):
    buy = [0] * len(prices)
    sell = [0] * len(prices)
    buy[0] = -prices[0]
    sell[0] = 0
    for i in range(1, len(prices)):
        buy[i] = max(buy[i-1], sell[i-2] - prices[i])
        sell[i] = max(sell[i-1], buy[i-1] + prices[i])
    return sell[-1]

if __name__ == '__main__':
    maxProfit()