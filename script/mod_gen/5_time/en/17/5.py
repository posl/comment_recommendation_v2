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
