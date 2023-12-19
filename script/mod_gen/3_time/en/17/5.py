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
