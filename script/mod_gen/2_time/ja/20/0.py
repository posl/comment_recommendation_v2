class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = -float('inf')
        dp_pre_0 = 0

if __name__ == '__main__':
    prices = list(map(int, input().split()))
    a = Solution()
    print(a.maxProfit(prices))