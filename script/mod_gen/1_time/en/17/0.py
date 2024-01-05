def coinChange(coins, amount):
    dp = [float('inf') for i in range(amount+1)]
    dp[0] = 0
    for i in range(1, amount+1):
        for j in range(len(coins)):
            if i >= coins[j]:
                dp[i] = min(dp[i], dp[i-coins[j]]+1)
    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == '__main__':
    coins = list(map(int, input().split()))
    amount = int(input())
    a = coinChange(coins, amount)
    print(a)