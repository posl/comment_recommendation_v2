class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [0] + [float("inf")] * amount
        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[-1] if dp[-1] != float("inf") else -1

if __name__ == '__main__':
    coins = list(map(int, input().split()))
    amount = int(input())
    a = Solution()
    print(a.coinChange(coins, amount))