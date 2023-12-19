Synthesizing 10/10 solutions

=======
Suggestion 1

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    dp = [[0 for i in range(2)] for j in range(len(prices))]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
    dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])
    for i in range(2, len(prices)):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
    return dp[len(prices)-1][0]

=======
Suggestion 2

def maxProfit(prices):
    pass

=======
Suggestion 3

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) <= 1:
        return 0

    profit = 0
    buy = prices[0]
    sell = prices[0]
    cooldown = prices[0]

    for price in prices[1:]:
        if price < buy:
            buy = price
            sell = price
        elif price > sell:
            sell = price
        else:
            if sell > buy:
                profit += sell - buy
            buy = price
            sell = price

    if sell > buy:
        profit += sell - buy

    return profit

print maxProfit([1,2,3,0,2])
print maxProfit([1])
print maxProfit([2,1,4,5,2,9,7])
print maxProfit([2,1,4,5,2,9,7,1,2,3,4,5,6,7,8,9,10])

=======
Suggestion 4

def maxProfit(prices):
    n = len(prices)
    dp = [[0 for i in range(2)] for j in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
        if i-2 >= 0:
            dp[i][1] = max(dp[i-1][1],dp[i-2][0]-prices[i])
        else:
            dp[i][1] = max(dp[i-1][1],-prices[i])
    return dp[n-1][0]

print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))
print(maxProfit([1,2,3,0,2,1,3,2,4,5,6,3,1,5,7,2,4,6,8,9,2,4,5,7,8,9,2,4,5,6,7,8,9,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]))

=======
Suggestion 5

def maxProfit(prices):
    n = len(prices)
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

=======
Suggestion 6

def maxProfit(prices):
    n = len(prices)
    if n < 2:
        return 0
    if n == 2:
        return max(0, prices[1] - prices[0])
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[1][0] = -prices[0]
    dp[1][1] = max(-prices[0], -prices[1])
    for i in range(2, n):
        dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + prices[i])
        dp[1][i] = max(dp[1][i - 1], dp[0][i - 2] - prices[i])
    return dp[0][n - 1]

=======
Suggestion 7

def maxProfit(prices):
    n = len(prices)
    dp = [[0 for i in range(2)] for j in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        if i >= 2:
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        else:
            dp[i][1] = max(dp[i-1][1], -prices[i])

    return dp[n-1][0]

=======
Suggestion 8

def maxProfit(prices):
    n = len(prices)
    dp = [[0 for i in range(2)] for i in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    dp[1][0] = max(dp[0][0],dp[0][1]+prices[1])
    dp[1][1] = max(dp[0][1],dp[0][0]-prices[1])
    for i in range(2,n):
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
        dp[i][1] = max(dp[i-1][1],dp[i-2][0]-prices[i])
    return dp[n-1][0]

print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))

=======
Suggestion 9

def maxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0
    dp = [[0,0] for _ in range(n)]
    # dp[i][0] means the profit in day i without stock in hand
    # dp[i][1] means the profit in day i with stock in hand
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    for i in range(1,n):
        # if you don't have stock in hand in day i, you can choose to buy or not buy
        # if you buy, the profit will be dp[i-1][0]-prices[i]
        # if you don't buy, the profit will be dp[i-1][0]
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
        # if you have stock in hand in day i, you can choose to sell or not sell
        # if you sell, the profit will be dp[i-1][1]+prices[i]
        # if you don't sell, the profit will be dp[i-1][1]
        # but you cannot sell stock in day i if you buy it in day i
        dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
    return dp[-1][0]

=======
Suggestion 10

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0
    n = len(prices)
    dp = [[0 for _ in range(2)] for _ in range(n)]
    for i in range(n):
        if i == 0:
            dp[i][0] = 0
            dp[i][1] = -prices[i]
            continue
        if i == 1:
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
            continue
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
    return dp[n-1][0]

prices = [1,2,3,0,2]
print(maxProfit(prices))
