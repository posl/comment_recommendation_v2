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
