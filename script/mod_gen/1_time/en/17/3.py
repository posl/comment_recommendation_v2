def coinChange(coins, amount):
    if amount == 0:
        return 0
    dp = [0] + [float('inf')] * amount
    for i in range(1, amount + 1):
        dp[i] = min([dp[i - c] if i - c >= 0 else float('inf') for c in coins]) + 1
    return -1 if dp[-1] == float('inf') else dp[-1]
print(coinChange([1,2,5], 11)) #3
print(coinChange([2], 3)) #-1
print(coinChange([1], 0)) #0
print(coinChange([1], 1)) #1
print(coinChange([1], 2)) #2
print(coinChange([1,2,5,10], 18)) #3
print(coinChange([1,2,5,10], 17)) #4
print(coinChange([1,2,5,10], 16)) #3
print(coinChange([1,2,5,10], 15)) #2
print(coinChange([1,2,5,10], 14)) #2
print(coinChange([1,2,5,10], 13)) #2
print(coinChange([1,2,5,10], 12)) #2
print(coinChange([1,2,5,10], 11)) #2
print(coinChange([1,2,5,10], 10)) #1
print(coinChange([1,2,5,10], 9)) #2
print(coinChange([1,2,5,10], 8)) #2
print(coinChange([1,2,5,10], 7)) #3
print(coinChange([1,2,5,10], 6)) #2
print(coinChange([1,2,5,10], 5)) #1
print(coinChange([1,2,5,10], 4)) #2
print(coinChange([1,2,5,10], 3)) #3
print(coinChange([1,2,5,10], 2)) #1
print(coinChange([1,2,
