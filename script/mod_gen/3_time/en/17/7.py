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
