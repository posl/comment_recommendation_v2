class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == '__main__':
    coins = list(map(int, input().split()))
    amount = int(input())
    a = Solution()
    print(a.coinChange(coins, amount))