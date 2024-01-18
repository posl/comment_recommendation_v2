class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        return dp[amount] if dp[amount] != amount+1 else -1

if __name__ == '__main__':
    coins = list(map(int, input().split()))
    amount = int(input())
    a = Solution()
    print(a.coinChange(coins, amount))