def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # buy[i] = max(buy[i-1], sell[i-2] - prices[i])
    # sell[i] = max(sell[i-1], buy[i-1] + prices[i])
    # buy[0] = -prices[0]
    # buy[1] = max(buy[0], sell[0] - prices[1])
    # sell[0] = 0
    # sell[1] = max(sell[0], buy[0] + prices[1])
    if not prices:
        return 0
    buy = [-prices[0], 0]
    sell = [0, 0]
    for i in range(1, len(prices)):
        buy.append(max(buy[i], sell[i-2] - prices[i]))
        sell.append(max(sell[i-1], buy[i-1] + prices[i]))
    return sell[-1]

if __name__ == '__main__':
    maxProfit()