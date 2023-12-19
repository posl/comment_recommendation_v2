Synthesizing 10/10 solutions

=======
Suggestion 1

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 1:
        return 0
    if len(prices) == 2:
        return max(0, prices[1] - prices[0])
    dp = [[0, 0] for _ in range(len(prices))]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    dp[1][0] = max(0, prices[1] - prices[0])
    dp[1][1] = max(-prices[0], -prices[1])
    for i in range(2, len(prices)):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 2][0] - prices[i], dp[i - 1][1])
    return dp[-1][0]

=======
Suggestion 2

def maxProfit(prices):
    if len(prices) <= 1:
        return 0
    sell = 0
    cooldown = 0
    buy = -prices[0]
    for i in range(1, len(prices)):
        buy = max(buy, cooldown - prices[i])
        cooldown = max(cooldown, sell)
        sell = max(sell, buy + prices[i])
    return sell

=======
Suggestion 3

def maxProfit(prices):
    n = len(prices)
    dp = [[0,0] for i in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        if i == 1:
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        else:
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
    return dp[n-1][0]

print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))
print(maxProfit([1,2]))
print(maxProfit([2,1]))
print(maxProfit([2,1,2,0,1]))
print(maxProfit([2,1,4,5,2,9,7]))
print(maxProfit([2,1,4,5,2,9,7,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(maxProfit([2,1,4,5,2,9,7,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(maxProfit([2,1,4,5,2,9,7,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1]))
print(maxProfit([2,1,4,5,2,9,7,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,2,3,4,5,6,7,8,9,10,11,12,13

=======
Suggestion 4

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) < 2:
        return 0
    
    dp = [[0 for _ in range(3)] for _ in range(len(prices))]
    dp[0][0] = -prices[0]
    dp[1][0] = max(dp[0][0], -prices[1])
    dp[1][1] = max(dp[0][1], dp[0][0] + prices[1])
    dp[1][2] = 0
    for i in range(2, len(prices)):
        dp[i][0] = max(dp[i-1][0], dp[i-2][1] - prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        dp[i][2] = max(dp[i-1][2], dp[i-1][1])
    return max(dp[-1][1], dp[-1][2])

=======
Suggestion 5

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

=======
Suggestion 6

def maxProfit(prices):
    dp = [[0, 0] for _ in range(len(prices))]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
    dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])
    for i in range(2, len(prices)):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
    return dp[-1][0]

print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))

=======
Suggestion 7

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    if n < 2:
        return 0
    dp = [[0 for _ in range(2)] for _ in range(n)]
    dp[0][1] = -prices[0]
    dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
    dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])
    for i in range(2, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
    return dp[-1][0]

=======
Suggestion 8

def maxProfit(prices) -> int:
    n = len(prices)
    if n < 2:
        return 0
    dp = [[0 for _ in range(2)] for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
    dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])
    for i in range(2, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
    return dp[n - 1][0]

=======
Suggestion 9

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) < 2:
        return 0
    #dp[i][0] means the max profit at day i, if we don't have stock at day i
    #dp[i][1] means the max profit at day i, if we have stock at day i
    dp = [[0 for _ in range(2)] for _ in range(len(prices))]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    dp[1][0] = max(dp[0][0], dp[0][1]+prices[1])
    dp[1][1] = max(dp[0][1], dp[0][0]-prices[1])
    for i in range(2, len(prices)):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
    return dp[-1][0]

=======
Suggestion 10

def maxProfit(prices):
    n = len(prices)
    if n == 1:
        return 0
    dp = [[0, 0] for _ in range(n)]
    dp[0][1] = -prices[0]
    dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
    dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])
    for i in range(2, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
    return dp[n-1][0]
