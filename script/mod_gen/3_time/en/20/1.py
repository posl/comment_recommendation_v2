def maxProfit(prices):
    if len(prices) <= 1:
        return 0
    sell = 0
    cooldown = 0
    buy = -prices[0]
    for i in range(1, len(prices)):
        buy = max(buy, cooldown - prices[i])
        cooldown = max(cooldown, sell)
        sell = max(sell, buy + prices[i])
    return sell

if __name__ == '__main__':
    maxProfit()