def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float('inf') else -1
print(coinChange([1,2,5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))
