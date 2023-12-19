def maxProfit(prices):
    if len(prices) == 1:
        return 0
    elif len(prices) == 2:
        if prices[1] > prices[0]:
            return prices[1] - prices[0]
        else:
            return 0
    else:
        dp = [0] * len(prices)
        dp[0] = 0
        dp[1] = max(prices[1] - prices[0], 0)
        dp[2] = max(prices[2] - prices[1], prices[2] - prices[0], 0)
        for i in range(3, len(prices)):
            dp[i] = max(dp[i-1], dp[i-3] + max(prices[i] - prices[i-1], 0))
        return dp[-1]
print(maxProfit([1,2,3,0,2])) #3
print(maxProfit([1])) #0
print(maxProfit([1,2])) #1
print(maxProfit([2,1,4])) #3
print(maxProfit([1,2,3,0,2,5])) #6
print(maxProfit([3,2,6,5,0,3])) #7
print(maxProfit([1,2,4,2,5,7,2,4,9,0])) #13
print(maxProfit([1,2,4,2,5,7,2,4,9,0,9])) #18
print(maxProfit([1,2,4,2,5,7,2,4,9,0,9,1])) #18
print(maxProfit([1,2,4,2,5,7,2,4,9,0,9,1,2])) #19
print(maxProfit([1,2,4,2,5,7,2,4,9,0,9,1,2,3])) #21
print(maxProfit([1,2,4,2,5,7,2,4,9,0,9,1,2,3,4])) #23
print(maxProfit([1,2,4,2,5,7,2,4,9,0,9,1,2,3,4,5])) #26
