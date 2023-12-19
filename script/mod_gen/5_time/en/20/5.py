def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    #print(prices)
    #print(len(prices))
    if len(prices) < 2:
        return 0
    if len(prices) == 2:
        if prices[1] > prices[0]:
            return prices[1] - prices[0]
        else:
            return 0
    if len(prices) == 3:
        if prices[1] > prices[0]:
            if prices[2] > prices[1]:
                return prices[2] - prices[0]
            else:
                return prices[1] - prices[0]
        else:
            return 0
    profit = 0
    i = 0
    while i < len(prices) - 2:
        if prices[i+1] > prices[i]:
            if prices[i+2] > prices[i+1]:
                profit += prices[i+2] - prices[i]
                i += 3
            else:
                profit += prices[i+1] - prices[i]
                i += 2
        else:
            i += 1
    return profit

if __name__ == '__main__':
    maxProfit()