def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount
    for i in range(1, amount + 1):
        dp[i] = min([dp[i - c] if i - c >= 0 else float('inf') for c in coins]) + 1
    return dp[amount] if dp[amount] != float('inf') else -1
print(coinChange([1,2,5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))
print(coinChange([1], 1))
print(coinChange([1], 2))
print(coinChange([1,2,5,10], 18))
print(coinChange([1,2,5,10], 19))
print(coinChange([1,2,5,10], 20))
print(coinChange([1,2,5,10], 21))
print(coinChange([1,2,5,10], 22))
print(coinChange([1,2,5,10], 23))
print(coinChange([1,2,5,10], 24))
print(coinChange([1,2,5,10], 25))
print(coinChange([1,2,5,10], 26))
print(coinChange([1,2,5,10], 27))
print(coinChange([1,2,5,10], 28))
print(coinChange([1,2,5,10], 29))
print(coinChange([1,2,5,10], 30))
print(coinChange([1,2,5,10], 31))
print(coinChange([1,2,5,10], 32))
print(coinChange([1,2,5,10], 33))
print(coinChange([1,2,5,10], 34))
print(coinChange([1,2,5,10], 35))
print(coinChange([1,2,5,10], 36))
print(coinChange([1,2,5,10], 37))
print(coinChange([1,2,5,10], 38))
print(coinChange([1,2,5,10], 39))
print(coinChange([1
