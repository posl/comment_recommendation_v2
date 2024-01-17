class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Dynamic Programming
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        n = len(prices)
        if n == 1:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,n):
            if i == 1:
                dp[i][0] = max(dp[i-1][0],dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1],dp[i-1][0] - prices[i])
            else:
                dp[i][0] = max(dp[i-1][0],dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1],dp[i-2][0] - prices[i])
        return dp[n-1][0]

if __name__ == '__main__':
    prices = list(map(int, input().split()))
    a = Solution()
    print(a.maxProfit(prices))