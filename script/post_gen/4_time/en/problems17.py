Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def coinChange(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    if len(coins) == 0:
        return -1
    dp = [float('inf') for i in range(amount+1)]
    dp[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if i-coin >= 0:
                dp[i] = min(dp[i-coin]+1, dp[i])
    if dp[amount] == float('inf'):
        return -1
    return dp[amount]

=======
Suggestion 2

def coinChange(coins, amount):
    if amount == 0:
        return 0
    if len(coins) == 0:
        return -1
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if i >= c:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return dp[-1] if dp[-1] != float('inf') else -1

=======
Suggestion 3

def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float('inf') else -1

print(coinChange([1,2,5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))

=======
Suggestion 4

def coinChange(coins, amount):
    dp = [0] + [float('inf')]*amount
    for coin in coins:
        for x in range(coin, amount+1):
            dp[x] = min(dp[x], dp[x-coin]+1)
    return dp[-1] if dp[-1] != float('inf') else -1

print(coinChange([1,2,5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))

=======
Suggestion 5

def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount
    for i in range(1, amount + 1):
        dp[i] = min([dp[i - c] if i - c >= 0 else float('inf') for c in coins]) + 1
    return dp[amount] if dp[amount] != float('inf') else -1

print(coinChange([1,2,5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))
print(coinChange([1], 1))
print(coinChange([1], 2))
print(coinChange([1,2,5,10], 18))
print(coinChange([1,2,5,10], 19))
print(coinChange([1,2,5,10], 20))
print(coinChange([1,2,5,10], 21))
print(coinChange([1,2,5,10], 22))
print(coinChange([1,2,5,10], 23))
print(coinChange([1,2,5,10], 24))
print(coinChange([1,2,5,10], 25))
print(coinChange([1,2,5,10], 26))
print(coinChange([1,2,5,10], 27))
print(coinChange([1,2,5,10], 28))
print(coinChange([1,2,5,10], 29))
print(coinChange([1,2,5,10], 30))
print(coinChange([1,2,5,10], 31))
print(coinChange([1,2,5,10], 32))
print(coinChange([1,2,5,10], 33))
print(coinChange([1,2,5,10], 34))
print(coinChange([1,2,5,10], 35))
print(coinChange([1,2,5,10], 36))
print(coinChange([1,2,5,10], 37))
print(coinChange([1,2,5,10], 38))
print(coinChange([1,2,5,10], 39))
print(coinChange([1

=======
Suggestion 6

def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin] + 1)
    if dp[amount] != float('inf'):
        return dp[amount]
    else:
        return -1

=======
Suggestion 7

def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))

=======
Suggestion 8

def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

=======
Suggestion 9

def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    #Dynamic Programming
    #Time: O(S*n) where S is the amount, n is the number of coins
    #Space: O(S)
    #dp[i] represents the least amount of coins that can make up the amount of i
    dp = [float('inf') for _ in range(amount+1)]
    dp[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[amount] if dp[amount] != float('inf') else -1
