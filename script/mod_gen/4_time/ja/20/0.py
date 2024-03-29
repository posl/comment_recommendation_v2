class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[1][0] = max(dp[0][0], -prices[1])
        dp[1][1] = max(dp[0][1], dp[0][0] + prices[1])
        for i in range(2, n):
            dp[i][0] = max(dp[i-1][0], dp[i-2][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        return dp[n-1][1]

if __name__ == '__main__':
    prices = list(map(int, input().split()))
    a = Solution()
    print(a.maxProfit(prices))