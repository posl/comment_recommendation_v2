Synthesizing 10/10 solutions

=======
Suggestion 1

def coinChange(coins, amount):
    dp = [float('inf') for _ in range(amount+1)]
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[-1] if dp[-1] != float('inf') else -1

print(coinChange([1,2,5],11))
print(coinChange([2],3))
print(coinChange([1],0))
print(coinChange([1],1))
print(coinChange([1],2))
print(coinChange([1,2,5],100))

=======
Suggestion 2

def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for c in coins:
            if i >= c:
                dp[i] = min(dp[i], dp[i - c] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

=======
Suggestion 3

def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount
    for i in range(1, amount + 1):
        dp[i] = min([dp[i - c] if i - c >= 0 else float('inf') for c in coins]) + 1
    return dp[-1] if dp[-1] != float('inf') else -1

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
Suggestion 4

def coinChange(coins, amount):
    dp = [float('inf')]*(amount+1)
    dp[0] = 0
    for i in range(1,amount+1):
        for j in range(len(coins)):
            if(coins[j]<=i):
                dp[i] = min(dp[i],dp[i-coins[j]]+1)
    if(dp[amount]==float('inf')):
        return -1
    return dp[amount]

print(coinChange([1,2,5],11))
print(coinChange([2],3))
print(coinChange([1],0))

=======
Suggestion 5

def coinChange(coins, amount):
    # dp[i] = min(dp[i], dp[i - coin] + 1)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

=======
Suggestion 6

def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin]+1)
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

coins = [1]
amount = 1
print(coinChange(coins, amount))

coins = [1]
amount = 2
print(coinChange(coins, amount))

=======
Suggestion 7

def coinChange(coins, amount):
  dp = [0] + [float("inf")] * amount
  for coin in coins:
    for i in range(coin, amount + 1):
      dp[i] = min(dp[i], dp[i - coin] + 1)
  return dp[-1] if dp[-1] != float("inf") else -1

coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))

=======
Suggestion 8

def coinChange(coins, amount):
    if amount == 0:
        return 0
    coins.sort(reverse=True)
    if amount < coins[-1]:
        return -1
    if amount == coins[-1]:
        return 1
    min_coins = [amount + 1] * (amount + 1)
    min_coins[0] = 0
    for i in range(1, amount+1):
        for j in range(len(coins)):
            if coins[j] <= i:
                min_coins[i] = min(min_coins[i], min_coins[i - coins[j]] + 1)
            else:
                break
    return min_coins[amount] if min_coins[amount] < amount + 1 else -1

coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))

=======
Suggestion 9

def coinChange(coins, amount):
    dp = [float("inf")]*(amount+1)
    dp[0] = 0
    for i in range(1,amount+1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i-coin]+1)
    if dp[amount] == float("inf"):
        return -1
    else:
        return dp[amount]
    
print(coinChange([1,2,5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))

=======
Suggestion 10

def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

print(coinChange([1,2,5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))
print(coinChange([1], 1))
print(coinChange([1], 2))
print(coinChange([186,419,83,408], 6249))
print(coinChange([1,2,3,4,5,6,7,8,9,10], 100))
