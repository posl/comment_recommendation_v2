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
