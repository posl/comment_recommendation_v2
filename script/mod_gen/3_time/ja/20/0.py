class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[0] * 3 for _ in range(n)]
        # 0: 持っていない
        # 1: 持っている
        # 2: クールダウン
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][2] - prices[i], dp[i - 1][1])
            dp[i][2] = dp[i - 1][0]
        return max(dp[-1][0], dp[-1][2])

if __name__ == '__main__':
    prices = list(map(int, input().split()))
    a = Solution()
    print(a.maxProfit(prices))