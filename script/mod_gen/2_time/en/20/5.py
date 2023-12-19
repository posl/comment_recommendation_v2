def maxProfit(prices):
    sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
    for price in prices:
        prev_buy = buy
        buy = max(prev_sell - price, prev_buy)
        prev_sell = sell
        sell = max(prev_buy + price, prev_sell)
    return sell
print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))
print(maxProfit([1,2,4]))
print(maxProfit([1,2,4,2,5,7,2,4,9,0,9]))
print(maxProfit([1,2,3,4,5,6,7,8,9]))
print(maxProfit([9,8,7,6,5,4,3,2,1]))
print(maxProfit([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]))
print(maxProfit([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0]))
print(maxProfit([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0,1]))
print(maxProfit([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0,1,2]))
print(maxProfit([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0,1,2,3]))
print(maxProfit([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0,1,2,3,4]))
print(maxProfit([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0,1,2,3,4,5]))
print(maxProfit([1,2,3,4,5,6,
