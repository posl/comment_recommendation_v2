class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        #dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = -prices[0]
        dp_pre_0 = 0
        for i in range(1, n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = temp
        return dp_i_0

if __name__ == '__main__':
    prices = list(map(int, input().split()))
    a = Solution()
    print(a.maxProfit(prices))