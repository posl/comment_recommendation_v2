Synthesizing 10/10 solutions

=======
Suggestion 1

def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

print(coinChange([1,2,5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))

=======
Suggestion 2

def coinChange(coins, amount):
    dp = [0] + [float('inf')]*amount
    for i in range(1, amount+1):
        dp[i] = min([dp[i-c] if i-c >= 0 else float('inf') for c in coins]) + 1
    return dp[amount] if dp[amount] != float('inf') else -1

print(coinChange([1,2,5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))
print(coinChange([1], 1))
print(coinChange([1], 2))
print(coinChange([1,2147483647], 2))

=======
Suggestion 3

def coinChange(coins, amount):
    dp = [float('inf')] * (amount+1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount+1):
            dp[x] = min(dp[x], dp[x-coin]+1)
    return dp[amount] if dp[amount] != float('inf') else -1

=======
Suggestion 4

def coinChange(coins, amount):
    dp = [float('inf')] * (amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1+dp[i-coin])
    return dp[amount] if dp[amount] != float('inf') else -1

=======
Suggestion 5

def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))

=======
Suggestion 6

def coinChange(coins, amount):
    dp = [float('inf')] * (amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i-coin]+1)
    if dp[amount] == float('inf'):
        return -1
    return dp[amount]

coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))

=======
Suggestion 7

def coinChange(coins, amount):
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
print(coinChange([1,2,5],11))
print(coinChange([2],3))
print(coinChange([1],0))

=======
Suggestion 8

def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for j in coins:
            if j <= i:
                dp[i] = min(dp[i], dp[i - j] + 1)
    return dp[amount] if dp[amount] <= amount else -1

print(coinChange([1,2,5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))
print(coinChange([1], 1))
print(coinChange([1], 2))

=======
Suggestion 9

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
Suggestion 10

def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float('inf') else -1
