Synthesizing 10/10 solutions

=======
Suggestion 1

def coinChange(coins, amount):
    dp = [float('inf') for i in range(amount+1)]
    dp[0] = 0
    for i in range(1, amount+1):
        for j in range(len(coins)):
            if i >= coins[j]:
                dp[i] = min(dp[i], dp[i-coins[j]]+1)
    return dp[amount] if dp[amount] != float('inf') else -1

=======
Suggestion 2

def coinChange(coins, amount):
    if amount == 0:
        return 0
    if len(coins) == 0:
        return -1
    if len(coins) == 1:
        if amount % coins[0] == 0:
            return amount//coins[0]
        return -1
    if amount < min(coins):
        return -1
    if amount in coins:
        return 1
    coins.sort()
    for i in range(len(coins)):
        if coins[i] > amount:
            break
    coins = coins[:i]
    #print(coins)
    dp = [0] * (amount + 1)
    for i in range(1, amount + 1):
        if i in coins:
            dp[i] = 1
        else:
            dp[i] = float('inf')
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    if dp[amount] == float('inf'):
        return -1
    return dp[amount]

print(coinChange([1,2,5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))
print(coinChange([1], 1))
print(coinChange([1], 2))
print(coinChange([1,2,5], 100))

=======
Suggestion 3

def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

=======
Suggestion 4

def coinChange(coins, amount):
    if amount == 0:
        return 0
    dp = [0] + [float('inf')] * amount
    for i in range(1, amount + 1):
        dp[i] = min([dp[i - c] if i - c >= 0 else float('inf') for c in coins]) + 1
    return -1 if dp[-1] == float('inf') else dp[-1]

print(coinChange([1,2,5], 11)) #3
print(coinChange([2], 3)) #-1
print(coinChange([1], 0)) #0
print(coinChange([1], 1)) #1
print(coinChange([1], 2)) #2
print(coinChange([1,2,5,10], 18)) #3
print(coinChange([1,2,5,10], 17)) #4
print(coinChange([1,2,5,10], 16)) #3
print(coinChange([1,2,5,10], 15)) #2
print(coinChange([1,2,5,10], 14)) #2
print(coinChange([1,2,5,10], 13)) #2
print(coinChange([1,2,5,10], 12)) #2
print(coinChange([1,2,5,10], 11)) #2
print(coinChange([1,2,5,10], 10)) #1
print(coinChange([1,2,5,10], 9)) #2
print(coinChange([1,2,5,10], 8)) #2
print(coinChange([1,2,5,10], 7)) #3
print(coinChange([1,2,5,10], 6)) #2
print(coinChange([1,2,5,10], 5)) #1
print(coinChange([1,2,5,10], 4)) #2
print(coinChange([1,2,5,10], 3)) #3
print(coinChange([1,2,5,10], 2)) #1
print(coinChange([1,2,

=======
Suggestion 5

def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

=======
Suggestion 6

def coinChange(coins, amount):
    dp = [float('inf')]*(amount+1)
    dp[0] = 0
    for i in range(1,amount+1):
        for j in range(len(coins)):
            if i >= coins[j]:
                dp[i] = min(dp[i], dp[i-coins[j]]+1)
    return dp[amount] if dp[amount] != float('inf') else -1


coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))

coins = [2]
amount = 3
print(coinChange(coins, amount))

coins = [1]
amount = 0
print(coinChange(coins, amount))

=======
Suggestion 7

def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount

    for i in range(1, amount + 1):
        dp[i] = min([dp[i - c] if i - c >= 0 else float('inf') for c in coins]) + 1

    return dp[-1] if dp[-1] != float('inf') else -1

coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))

=======
Suggestion 8

def coinChange(coins, amount):
    dp = [0] + [float('inf')]*amount

    for i in range(1, amount+1):
        dp[i] = min([dp[i-c] if i-c >= 0 else float('inf') for c in coins]) + 1

    return dp[amount] if dp[amount] != float('inf') else -1

=======
Suggestion 9

def coinChange(coins, amount):
    dp = [float('inf')]*(amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[amount] if dp[amount] != float('inf') else -1

print(coinChange([1,2,5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))
print(coinChange([1], 1))
print(coinChange([1], 2))
print(coinChange([1,2,5], 100))

=======
Suggestion 10

def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], dp[i - c] + 1)
    if dp[amount] == float('inf'):
        return -1
    else:
        return dp[amount]

print(coinChange([1,2,5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))
