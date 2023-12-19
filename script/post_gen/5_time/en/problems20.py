Synthesizing 10/10 solutions

=======
Suggestion 1

def maxProfit(prices):
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
print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))

=======
Suggestion 2

def maxProfit(prices):
    n = len(prices)
    if n == 1:
        return 0
    dp = [[0 for _ in range(2)] for _ in range(n)]
    dp[0][0], dp[0][1] = 0, -prices[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        if i == 1:
            dp[i][1] = max(dp[i-1][1], -prices[i])
        else:
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
    return dp[n-1][0]

=======
Suggestion 3

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # buy[i] = max(buy[i-1], sell[i-2] - prices[i])
    # sell[i] = max(sell[i-1], buy[i-1] + prices[i])
    # buy[0] = -prices[0]
    # buy[1] = max(buy[0], sell[0] - prices[1])
    # sell[0] = 0
    # sell[1] = max(sell[0], buy[0] + prices[1])
    if not prices:
        return 0
    buy = [-prices[0], 0]
    sell = [0, 0]
    for i in range(1, len(prices)):
        buy.append(max(buy[i], sell[i-2] - prices[i]))
        sell.append(max(sell[i-1], buy[i-1] + prices[i]))
    return sell[-1]

=======
Suggestion 4

def maxProfit(prices):
    if len(prices) <= 1:
        return 0
    dp = [[0]*len(prices) for _ in range(len(prices))]
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            dp[i][j] = prices[j] - prices[i]
    print(dp)
    return max(max(dp))

print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))

=======
Suggestion 5

def maxProfit(prices):
    if len(prices) < 2:
        return 0
    dp = [[0 for _ in range(len(prices))] for _ in range(3)]
    dp[0][0] = -prices[0]
    dp[1][0] = 0
    dp[2][0] = 0
    for i in range(1, len(prices)):
        dp[0][i] = max(dp[0][i - 1], dp[2][i - 1] - prices[i])
        dp[1][i] = dp[0][i - 1] + prices[i]
        dp[2][i] = max(dp[1][i - 1], dp[2][i - 1])
    return max(dp[1][-1], dp[2][-1])

=======
Suggestion 6

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
    dp[1][0] = max(dp[0][0], dp[0][1]+prices[1])
    dp[1][1] = max(dp[0][1], dp[0][0]-prices[1])
    for i in range(2, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
    return dp[-1][0]

=======
Suggestion 8

def maxProfit(prices):
    n = len(prices)
    buy = [0] * (n+1)
    sell = [0] * (n+1)

    buy[1] = -prices[0]

    for i in range(2, n+1):
        buy[i] = max(buy[i-1], sell[i-2] - prices[i-1])
        sell[i] = max(sell[i-1], buy[i-1] + prices[i-1])

    return sell[n]

print(maxProfit([1,2,3,0,2]))

=======
Suggestion 9

def maxProfit(prices):
    print(prices)
    n = len(prices)
    if n == 1:
        return 0
    dp = [[0 for x in range(2)] for x in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
    dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])
    for i in range(2, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
    print(dp)
    return dp[n-1][0]

print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))
print(maxProfit([1,2,4]))
print(maxProfit([1,2,3,0,2,1,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]))
print(maxProfit([1,2,3,0,2,1,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]))
print(maxProfit([1,2,3,0,2,1,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1]))
print(maxProfit([1,2,3,0,2,1,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2]))
print(maxProfit([1,2,3,0,2,1,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3]))
print(max

=======
Suggestion 10

def maxProfit(prices):
    n = len(prices)
    if n < 2:
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


prices = [1,2,3,0,2]
print(maxProfit(prices))
prices = [1]
print(maxProfit(prices))
prices = [1,2,4]
print(maxProfit(prices))
prices = [1,2,3,0,2]
print(maxProfit(prices))
prices = [1,2,3,0,2]
print(maxProfit(prices))
prices
