Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def maxProfit(self, prices: list[int]) -> int:
        if len(prices) <= 1:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        dp[1][1] = -prices[1]
        dp[1][0] = max(0, dp[0][1] + prices[1])
        for i in range(2, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        print(dp)
        return dp[len(prices) - 1][0]

=======
Suggestion 3

def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        # dp[i][0] is the maximum profit on day i without stock
        # dp[i][1] is the maximum profit on day i with stock
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])

=======
Suggestion 4

def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0
        dp = [[0 for i in range(2)] for j in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])
        for i in range(2, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            if i == 2:
                dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
            else:
                dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        return dp[len(prices)-1][0]

=======
Suggestion 5

def maxProfit(self, prices: list[int]) -> int:
        sell = 0
        buy = -prices[0]
        rest = 0
        for i in range(1, len(prices)):
            prev_sell = sell
            sell = buy + prices[i]
            buy = max(buy, rest - prices[i])
            rest = max(rest, prev_sell)
        return max(sell, rest)

=======
Suggestion 6

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        dp = [[0] * 3 for _ in range(n)]
        # 0: buy, 1: sell, 2: cooldown
        dp[0][0] = -prices[0]
        dp[1][0] = max(dp[0][0], -prices[1])
        dp[1][1] = max(dp[0][1], dp[0][0] + prices[1])
        dp[1][2] = dp[0][1]
        for i in range(2, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 2][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            dp[i][2] = dp[i - 1][1]
        return dp[n - 1][1]

=======
Suggestion 7

def maxProfit(self, prices: list[int]) -> int:
        dp = [0 for i in range(len(prices))]
        for i in range(1,len(prices)):
            for j in range(i):
                if j == 0:
                    dp[i] = max(dp[i],prices[i]-prices[j])
                elif j > 1:
                    dp[i] = max(dp[i],prices[i]-prices[j]+dp[j-2])
                else:
                    dp[i] = max(dp[i],prices[i]-prices[j]+dp[j-1])
            dp[i] = max(dp[i],dp[i-1])
        return dp[-1]

=======
Suggestion 8

def maxProfit(self, prices: list[int]) -> int:
        dp = [[0,0,0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        return max(dp[-1][1], dp[-1][2])

=======
Suggestion 9

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[0, 0] for i in range(n)]
        dp[0][1] = -prices[0]
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])
        for i in range(2, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-2][0] - prices[i], dp[i-1][1])
        return dp[n-1][0]

=======
Suggestion 10

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Dynamic programming
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        # dp[i][0] means the profit of day i with no stock in hand
        # dp[i][1] means the profit of day i with stock in hand
        # dp[i-1][0] means the profit of day i-1 with no stock in hand, and no transaction on day i
        # dp[i-1][1] + prices[i] means the profit of day i-1 with stock in hand, and sell the stock on day i
        # dp[i-1][1] means the profit of day i-1 with stock in hand, and no transaction on day i
        # dp[i-2][0] - prices[i] means the profit of day i-2 with no stock in hand, and buy the stock on day i
        # dp[i-1][0] means the profit of day i-1 with no stock in hand, and no transaction on day i
        # dp[i-1][1] means the profit of day i-1 with stock in hand, and no transaction on day i
        # dp[0][0] = 0
        # dp[0][1] = -prices[0]
        # dp[1][0] = max(dp[0][0], dp[0][1] + prices[1]) = max(0, -prices[0] + prices[1]) = max(0, prices[1] - prices[0])
        # dp[1][1] = max(dp[0][1], dp[-1][0] - prices[1]) = max(-prices[0], -prices[1])
        # dp[2][0] = max(dp[1][0], dp[1][1] + prices[2]) = max(max(0, prices[1] - prices[0]), -prices[1] + prices[2])
        # dp[2][1] = max(dp[1][1], dp[0][0] - prices[2]) = max(max(-prices[0], -prices[1]), -prices[
