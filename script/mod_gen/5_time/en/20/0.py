class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0
        elif len(prices) == 2:
            return max(0, prices[1] - prices[0])
        else:
            dp = [0] * len(prices)
            dp[0] = 0
            dp[1] = max(0, prices[1] - prices[0])
            for i in range(2, len(prices)):
                dp[i] = max(dp[i-1], dp[i-2] + prices[i] - prices[i-1])
            return dp[-1]

if __name__ == '__main__':
    prices = list(map(int, input().split()))
    a = Solution()
    print(a.maxProfit(prices))