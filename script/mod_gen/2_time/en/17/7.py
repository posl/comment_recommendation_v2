def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
print(coinChange([1,2,5], 11)) #3
print(coinChange([2], 3)) #-1
print(coinChange([1], 0)) #0
print(coinChange([1], 1)) #1
print(coinChange([1], 2)) #2
print(coinChange([1,2,5], 100)) #20
print(coinChange([186,419,83,408], 6249)) #20
print(coinChange([2,5,10,1], 27)) #4
print(coinChange([186,419,83,408], 6249)) #20
print(coinChange([1,2,5], 100)) #20
print(coinChange([1,5,10,25], 100)) #4
print(coinChange([1,5,10,25], 100)) #4
print(coinChange([2], 3)) #-1
print(coinChange([1,2,5], 11)) #3
print(coinChange([1,5,10,25], 100)) #4
print(coinChange([1,5,10,25], 100)) #4
print(coinChange([2], 3)) #-1
print(coinChange([1,2,5], 11)) #3
print(coinChange([1,5,10,25], 100)) #4
print(coinChange([1,5,10,25], 100)) #4
print(coinChange([2], 3)) #-1
print(coinChange([1,2,5], 11)) #3
print(coinChange([1,5,10,25], 100)) #4
print(coinChange([1,5,10,25], 100)) #4
print(coinChange([2], 3)) #-1
print(coinChange
