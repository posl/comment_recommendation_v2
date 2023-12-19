def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) <= 1:
        return 0
    profit = 0
    buy = prices[0]
    sell = prices[0]
    cooldown = prices[0]
    for price in prices[1:]:
        if price < buy:
            buy = price
            sell = price
        elif price > sell:
            sell = price
        else:
            if sell > buy:
                profit += sell - buy
            buy = price
            sell = price
    if sell > buy:
        profit += sell - buy
    return profit
print maxProfit([1,2,3,0,2])
print maxProfit([1])
print maxProfit([2,1,4,5,2,9,7])
print maxProfit([2,1,4,5,2,9,7,1,2,3,4,5,6,7,8,9,10])
