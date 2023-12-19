Synthesizing 9/10 solutions

=======
Suggestion 1

def maxProfit(prices):
    n = len(prices)
    if n < 2:
        return 0
    dp = [[0]*2 for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    dp[1][0] = max(dp[0][0], dp[0][1]+prices[1])
    dp[1][1] = max(dp[0][1], dp[0][0]-prices[1])
    for i in range(2, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
    return dp[n-1][0]

=======
Suggestion 2

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

=======
Suggestion 3

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    dp = [[0 for i in range(3)] for j in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    dp[0][2] = 0
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][2])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        dp[i][2] = dp[i-1][1] + prices[i]
    return max(dp[n-1][0], dp[n-1][2])

print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))
print(maxProfit([1,2,4]))
print(maxProfit([2,1,2,0,1]))
print("The values above should be 3, 0, 3, and 2.")

=======
Suggestion 4

def maxProfit(prices):
    if len(prices) < 2:
        return 0
    dp = [[0 for i in range(2)] for j in range(len(prices))]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
    dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])
    for i in range(2, len(prices)):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
    return dp[-1][0]

=======
Suggestion 5

def maxProfit(prices):
    n = len(prices)
    if n == 0:
        return 0
    dp = [[0 for _ in range(2)] for _ in range(n)]
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

=======
Suggestion 6

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    if n < 2:
        return 0
    dp = [[0 for _ in range(2)] for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
    dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])
    for i in range(2, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
    return dp[-1][0]

=======
Suggestion 7

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    #DP, O(n) time, O(n) space
    #dp[i] = max(dp[i-1], prices[i]-prices[j]+dp[j-2]) for j in range(i)
    #dp[i] = max(dp[i-1], prices[i]-min(prices[:i]))
    #dp[0] = 0
    #dp[1] = max(0, prices[1]-prices[0])
    #dp[2] = max(dp[1], prices[2]-min(prices[:2]))
    #dp[3] = max(dp[2], prices[3]-min(prices[:3]))
    #dp[4] = max(dp[3], prices[4]-min(prices[:4]))
    #dp[5] = max(dp[4], prices[5]-min(prices[:5]))
    #dp[6] = max(dp[5], prices[6]-min(prices[:6]))
    #dp[7] = max(dp[6], prices[7]-min(prices[:7]))
    #dp[8] = max(dp[7], prices[8]-min(prices[:8]))
    #dp[9] = max(dp[8], prices[9]-min(prices[:9]))
    #dp[10] = max(dp[9], prices[10]-min(prices[:10]))
    #dp[11] = max(dp[10], prices[11]-min(prices[:11]))
    #dp[12] = max(dp[11], prices[12]-min(prices[:12]))
    #dp[13] = max(dp[12], prices[13]-min(prices[:13]))
    #dp[14] = max(dp[13], prices[14]-min(prices[:14]))
    #dp[15] = max(dp[14], prices[15]-min(prices[:15]))
    #dp[16] = max(dp[15], prices[16]-min(prices[:16]))
    #dp[17] = max(dp[16], prices[17]-min(prices[:17]))
    #dp[18] = max(dp[17], prices[18]-min(prices[:18]))
    #dp[19] = max(dp[

=======
Suggestion 8

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    if n <= 1:
        return 0
    dp = [0] * n
    for i in range(1, n):
        for j in range(i):
            if j >= 2:
                dp[i] = max(dp[i], dp[j] + prices[i] - prices[j] + dp[j - 2])
            else:
                dp[i] = max(dp[i], prices[i] - prices[j])
        dp[i] = max(dp[i], dp[i - 1])
    return dp[-1]

=======
Suggestion 9

def maxProfit(prices):
    n = len(prices)
    if n == 1:
        return 0
    buy = [0]*n
    sell = [0]*n
    buy[0] = -prices[0]
    buy[1] = max(-prices[0], -prices[1])
    sell[1] = max(0, prices[1]-prices[0])
    for i in range(2, n):
        buy[i] = max(buy[i-1], sell[i-2]-prices[i])
        sell[i] = max(sell[i-1], buy[i-1]+prices[i])
    return sell[n-1]

prices = [1,2,3,0,2]
print(maxProfit(prices))
