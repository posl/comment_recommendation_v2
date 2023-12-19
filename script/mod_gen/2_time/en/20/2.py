def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) < 2: return 0
    buy, sell, prev_sell, prev_buy = -prices[0], 0, 0, 0
    for price in prices:
        prev_buy = buy
        buy = max(prev_sell - price, prev_buy)
        prev_sell = sell
        sell = max(prev_buy + price, prev_sell)
    return sell
print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))
print(maxProfit([1,2]))
print(maxProfit([1,2,3]))
print(maxProfit([1,2,3,4]))
print(maxProfit([1,2,3,4,5]))
print(maxProfit([1,2,3,4,5,6]))
print(maxProfit([1,2,3,4,5,6,7]))
print(maxProfit([1,2,3,4,5,6,7,8]))
print(maxProfit([1,2,3,4,5,6,7,8,9]))
print(maxProfit([1,2,3,4,5,6,7,8,9,10]))
print(maxProfit([1,2,3,4,5,6,7,8,9,10,11]))
print(maxProfit([1,2,3,4,5,6,7,8,9,10,11,12]))
print(maxProfit([1,2,3,4,5,6,7,8,9,10,11,12,13]))
print(maxProfit([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
print(maxProfit([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(maxProfit([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
print(maxProfit([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]))
print(maxProfit([
