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
