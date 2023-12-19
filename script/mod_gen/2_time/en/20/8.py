def maxProfit(prices):
    if len(prices) == 1:
        return 0
    elif len(prices) == 2:
        if prices[0] < prices[1]:
            return prices[1] - prices[0]
        else:
            return 0
    else:
        buy = 0
        sell = 0
        cooldown = 0
        for i in range(1,len(prices)):
            buy = max(buy, cooldown - prices[i])
            cooldown = max(cooldown, sell)
            sell = max(sell, buy + prices[i])
        return sell
print(maxProfit([1,2,3,0,2])) #3
print(maxProfit([1])) #0
print(maxProfit([1,2])) #1
print(maxProfit([1,2,4])) #3
print(maxProfit([1,2,3])) #2
print(maxProfit([1,2,3,4])) #3
print(maxProfit([1,2,3,4,5])) #4
print(maxProfit([1,2,3,4,5,6])) #5
print(maxProfit([1,2,3,4,5,6,7])) #6
print(maxProfit([1,2,3,4,5,6,7,8])) #7
print(maxProfit([1,2,3,4,5,6,7,8,9])) #8
print(maxProfit([1,2,3,4,5,6,7,8,9,10])) #9
print(maxProfit([1,2,3,4,5,6,7,8,9,10,11])) #10
print(maxProfit([1,2,3,4,5,6,7,8,9,10,11,12])) #11
print(maxProfit([1,2,3,4,5,6,7,8,9,10,11,12,13])) #12
print(maxProfit([1,2,3,4,5,6,7,8,9,10,11,12,13,14])) #13
print(maxProfit([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
