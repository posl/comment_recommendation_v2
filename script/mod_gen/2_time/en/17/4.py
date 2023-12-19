def coinChange(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    result = float('inf')
    for i in range(len(coins)):
        res = coinChange(coins, amount - coins[i])
        if res != -1:
            result = min(result, res + 1)
    if result == float('inf'):
        return -1
    return result
coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))
