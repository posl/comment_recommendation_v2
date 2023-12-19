Synthesizing 10/10 solutions

=======
Suggestion 1

def maxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0
    dp = [[0,0,0] for _ in range(n)]
    dp[0][0] = -prices[0]
    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0],dp[i-1][2]-prices[i])
        dp[i][1] = dp[i-1][0]+prices[i]
        dp[i][2] = max(dp[i-1][1],dp[i-1][2])
    return max(dp[n-1][1],dp[n-1][2])

print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))
print(maxProfit([1,2]))
print(maxProfit([2,1]))
print(maxProfit([2,1,4]))
print(maxProfit([2,1,4,5]))
print(maxProfit([2,1,4,5,2]))
print(maxProfit([2,1,4,5,2,9]))
print(maxProfit([2,1,4,5,2,9,7]))
print(maxProfit([2,1,4,5,2,9,7,1]))
print(maxProfit([2,1,4,5,2,9,7,1,3]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5,2]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5,2,6]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5,2,6,3]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5,2,6,3,7]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5,2,6,3,7,3]))
print(maxProfit([2,1,4,5,2,9,7,1,3,5,2,6,3,7,3,6

=======
Suggestion 2

def maxProfit(prices):
    n = len(prices)
    if n == 1:
        return 0
    dp = [[0 for i in range(2)] for j in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
    dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])
    for i in range(2, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
    return dp[n-1][0]
print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))
print(maxProfit([1,2,3,0,2]))
print("The values above should be 3, 0, and 3.")

=======
Suggestion 3

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

=======
Suggestion 4

def maxProfit(prices):
    n = len(prices)
    if n < 2:
        return 0

    dp = [[0] * n for _ in range(2)]
    dp[0][0] = 0
    dp[1][0] = -prices[0]

    for i in range(1, n):
        dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + prices[i])
        dp[1][i] = max(dp[1][i - 1], dp[0][i - 2] - prices[i])

    return dp[0][n - 1]

prices = [1,2,3,0,2]
print(maxProfit(prices))
prices = [1]
print(maxProfit(prices))

=======
Suggestion 5

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    #if prices is empty return 0
    if not prices:
        return 0
    #create a list of length prices and initialize it to 0
    profits = [0] * len(prices)
    #loop through prices
    for i in range(1, len(prices)):
        #loop through prices from 0 to i
        for j in range(i):
            #if prices[i] - prices[j] is greater than profits[i]
            if prices[i] - prices[j] > profits[i]:
                #set profits[i] to prices[i] - prices[j]
                profits[i] = prices[i] - prices[j]
                #if j is greater than 2
                if j > 2:
                    #set profits[i] to profits[j-2] + prices[i] - prices[j]
                    profits[i] = profits[j-2] + prices[i] - prices[j]
                #if profits[i] is greater than profits[i-1]
                if profits[i] > profits[i-1]:
                    #set profits[i] to profits[i-1]
                    profits[i] = profits[i-1]
    #return profits[-1]
    return profits[-1]

=======
Suggestion 6

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

=======
Suggestion 7

def maxProfit(prices):
    buy = [0] * len(prices)
    sell = [0] * len(prices)
    buy[0] = -prices[0]
    sell[0] = 0
    for i in range(1, len(prices)):
        buy[i] = max(buy[i-1], sell[i-2] - prices[i])
        sell[i] = max(sell[i-1], buy[i-1] + prices[i])
    return sell[-1]

=======
Suggestion 8

def maxProfit(prices):
    n = len(prices)
    dp = [[0,0] for _ in range(n)]
    dp[0][0] = -prices[0]
    dp[1][0] = max(dp[0][0],-prices[1])
    dp[1][1] = max(dp[0][1],dp[0][0]+prices[1])
    for i in range(2,n):
        dp[i][0] = max(dp[i-1][0],dp[i-2][1]-prices[i])
        dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i])
    return dp[n-1][1]

=======
Suggestion 9

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

=======
Suggestion 10

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # dynamic programming
    # dp[i] is the max profit of day i
    # dp[i] = max(dp[i-1], dp[i-2] + prices[i] - prices[i-1])
    # dp[0] = 0
    # dp[1] = max(0, prices[1] - prices[0])
    # dp[2] = max(dp[1], dp[0] + prices[2] - prices[1])
    # dp[3] = max(dp[2], dp[1] + prices[3] - prices[2])
    # ...
    # dp[n] = max(dp[n-1], dp[n-2] + prices[n] - prices[n-1])
    #
    # dp[n] = max(dp[n-1], dp[n-3] + prices[n] - prices[n-1])
    # dp[n] = max(dp[n-1], dp[n-3] + prices[n] - prices[n-1])
    # dp[n] = max(dp[n-1], dp[n-3] + prices[n] - prices[n-1])
    if len(prices) <= 1:
        return 0
    elif len(prices) == 2:
        return max(0, prices[1] - prices[0])
    elif len(prices) == 3:
        return max(max(0, prices[1] - prices[0]), max(0, prices[2] - prices[1]), max(0, prices[2] - prices[0]))
    dp = [0] * len(prices)
    dp[0] = 0
    dp[1] = max(0, prices[1] - prices[0])
    dp[2] = max(dp[1], dp[0] + prices[2] - prices[1])
    for i in range(3, len(prices)):
        dp[i] = max(dp[i-1], dp[i-3] + prices[i] - prices[i-1])
    return dp[-1]

print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))
print(maxProfit([1,2,3,0,2,1,4
