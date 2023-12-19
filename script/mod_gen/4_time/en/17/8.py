def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    #Dynamic Programming
    #Time: O(S*n) where S is the amount, n is the number of coins
    #Space: O(S)
    #dp[i] represents the least amount of coins that can make up the amount of i
    dp = [float('inf') for _ in range(amount+1)]
    dp[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == '__main__':
    coinChange()