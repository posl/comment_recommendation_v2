def coinChange(coins, amount):
    dp = [0] + [float('inf')]*amount
    for i in range(1, amount+1):
        dp[i] = min([dp[i-c] if i-c >= 0 else float('inf') for c in coins]) + 1
    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == '__main__':
    coins = list(map(int, input().split()))
    amount = int(input())
    a = coinChange(coins, amount)
    print(a)