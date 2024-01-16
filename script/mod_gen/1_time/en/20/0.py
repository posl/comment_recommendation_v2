class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[0 for i in range(n)] for j in range(n)]
        for k in range(1, n):
            for i in range(n-k):
                j = i + k
                if k == 1:
                    dp[i][j] = max(prices[j] - prices[i], 0)
                else:
                    dp[i][j] = dp[i+1][j]
                    for m in range(i+1, j+1):
                        if m > i+1:
                            dp[i][j] = max(dp[i][j], dp[i][m-2] + max(prices[m] - prices[i], 0) + dp[m][j])
                        else:
                            dp[i][j] = max(dp[i][j], max(prices[m] - prices[i], 0) + dp[m][j])
        return dp[0][n-1]

if __name__ == '__main__':
    prices = list(map(int, input().split()))
    a = Solution()
    print(a.maxProfit(prices))