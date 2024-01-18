class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = -prices[0]
        sell = 0
        cooldown = 0
        for i in range(1, len(prices)):
            buy = max(buy, cooldown - prices[i])
            cooldown = sell
            sell = max(sell, buy + prices[i])
        return sell

if __name__ == '__main__':
    prices = list(map(int, input().split()))
    a = Solution()
    print(a.maxProfit(prices))