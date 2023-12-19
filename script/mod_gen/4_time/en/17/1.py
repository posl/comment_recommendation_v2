def coinChange(coins, amount):
    if amount == 0:
        return 0
    if len(coins) == 0:
        return -1
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if i >= c:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return dp[-1] if dp[-1] != float('inf') else -1

if __name__ == '__main__':
    coinChange()