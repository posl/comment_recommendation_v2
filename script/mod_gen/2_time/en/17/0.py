class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for i in coins:
            for j in range(i, amount+1):
                dp[j] = min(dp[j], dp[j-i]+1)
        return dp[-1] if dp[-1] != float("inf") else -1

if __name__ == '__main__':
    coins = list(map(int, input().split()))
    amount = int(input())
    a = Solution()
    print(a.coinChange(coins, amount))