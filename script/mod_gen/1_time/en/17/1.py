def coinChange(coins, amount):
    if amount == 0:
        return 0
    if len(coins) == 0:
        return -1
    if len(coins) == 1:
        if amount % coins[0] == 0:
            return amount//coins[0]
        return -1
    if amount < min(coins):
        return -1
    if amount in coins:
        return 1
    coins.sort()
    for i in range(len(coins)):
        if coins[i] > amount:
            break
    coins = coins[:i]
    #print(coins)
    dp = [0] * (amount + 1)
    for i in range(1, amount + 1):
        if i in coins:
            dp[i] = 1
        else:
            dp[i] = float('inf')
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    if dp[amount] == float('inf'):
        return -1
    return dp[amount]
print(coinChange([1,2,5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))
print(coinChange([1], 1))
print(coinChange([1], 2))
print(coinChange([1,2,5], 100))
