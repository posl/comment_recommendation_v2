def maxProfit(prices):
    if len(prices) == 1:
        return 0
    elif len(prices) == 2:
        if prices[1] > prices[0]:
            return prices[1]-prices[0]
        else:
            return 0
    else:
        dp = [0]*len(prices)
        dp[1] = max(prices[1]-prices[0],0)
        for i in range(2,len(prices)):
            dp[i] = max(dp[i-1],dp[i-2]+prices[i]-prices[i-1])
        return dp[-1]
        
print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))
print(maxProfit([1,2]))
print(maxProfit([2,1]))
print(maxProfit([2,1,4]))
print(maxProfit([2,1,4,5,2,9,7]))
print(maxProfit([2,1,4,5,2,9,7,1,3]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5,7]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5,7,8]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5,7,8,9]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5,7,8,9,8]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5,7,8,9,8,9]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5,7,8,9,8,9,7]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5,7,8,9,8,9,7,6]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5,7,8,9,8,9,
