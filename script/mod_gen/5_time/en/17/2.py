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
