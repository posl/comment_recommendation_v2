def coinChange(coins, amount):
    if amount == 0:
        return 0
    coins.sort(reverse=True)
    if amount < coins[-1]:
        return -1
    if amount == coins[-1]:
        return 1
    min_coins = [amount + 1] * (amount + 1)
    min_coins[0] = 0
    for i in range(1, amount+1):
        for j in range(len(coins)):
            if coins[j] <= i:
                min_coins[i] = min(min_coins[i], min_coins[i - coins[j]] + 1)
            else:
                break
    return min_coins[amount] if min_coins[amount] < amount + 1 else -1
coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))
