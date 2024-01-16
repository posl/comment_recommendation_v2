Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0
        if len(prices) == 2:
            return max(prices[1] - prices[0], 0)
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            dp[i] = max(dp[i - 1], dp[i - 2] + prices[i] - prices[i - 1])
        return max(dp[-1], dp[-2])

=======
Suggestion 3

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[1][0] = max(-prices[0], -prices[1])
        dp[1][1] = max(0, prices[1] - prices[0])
        for i in range(2, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 2][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        return dp[n - 1][1]

=======
Suggestion 4

def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        dp[1][1] = -prices[1]
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        for i in range(2, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 2][0] - prices[i], dp[i - 1][1])
        return dp[-1][0]

=======
Suggestion 5

def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        
        dp = [[0 for _ in range(3)] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])
        
        return max(dp[-1][1], dp[-1][2])

=======
Suggestion 6

def maxProfit(self, prices: list[int]) -> int:
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        n = len(prices)
        if n <= 1:
            return 0
        dp_i_0 = 0
        dp_i_1 = -prices[0]
        dp_pre_0 = 0
        for i in range(1, n):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = tmp
        return dp_i_0

=======
Suggestion 7

def maxProfit(self, prices: list[int]) -> int:
        buy, sell, cooldown = -prices[0], 0, 0
        for i in range(1, len(prices)):
            buy, sell, cooldown = max(buy, cooldown - prices[i]), max(sell, buy + prices[i]), max(cooldown, sell)
        return sell

=======
Suggestion 8

def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        dp = [0] * len(prices)
        dp[1] = max(prices[1] - prices[0], 0)
        for i in range(2, len(prices)):
            dp[i] = max(dp[i - 1], dp[i - 2] + prices[i] - prices[i - 1])
            for j in range(2, i):
                dp[i] = max(dp[i], dp[j - 2] + prices[i] - prices[j])
        return dp[-1]

=======
Suggestion 9

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        buy = [0] * n
        sell = [0] * n
        buy[0] = -prices[0]
        buy[1] = max(buy[0], -prices[1])
        sell[1] = max(sell[0], buy[0] + prices[1])
        for i in range(2, n):
            buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
        return sell[n - 1]

=======
Suggestion 10

def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        if len(prices) == 2:
            return max(0, prices[1] - prices[0])
        dp = [[0, 0] for i in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])
        for i in range(2, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        return dp[-1][0]
