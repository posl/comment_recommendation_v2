def coinChange(coins, amount):
    # create a list of size amount + 1 to represent the minimum number of coins needed for each amount
    # initialize the first element to 0 since 0 amount needs 0 coins
    numCoins = [0] + [float('inf')] * amount
    # loop through the list of numCoins
    for i in range(len(numCoins)):
        # for each coin, loop through the list of numCoins
        for coin in coins:
            # if the amount is greater than or equal to the coin value
            if i >= coin:
                # the minimum number of coins for that amount is the minimum of the current number of coins at that amount and the minimum number of coins at the amount minus the coin value + 1
                numCoins[i] = min(numCoins[i], numCoins[i - coin] + 1)
    # if the minimum number of coins for the amount is infinity, return -1
    if numCoins[amount] == float('inf'):
        return -1
    # otherwise, return the minimum number of coins for the amount
    return numCoins[amount]

if __name__ == '__main__':
    coinChange()