def coinChange(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    if len(coins) == 0:
        return -1
    dp = [float('inf') for i in range(amount+1)]
    dp[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if i-coin >= 0:
                dp[i] = min(dp[i-coin]+1, dp[i])
    if dp[amount] == float('inf'):
        return -1
    return dp[amount]

if __name__ == '__main__':
    coinChange()