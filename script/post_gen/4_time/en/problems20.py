Synthesizing 10/10 solutions

=======
Suggestion 1

def maxProfit(self, prices: list[int]) -> int:
        dp = [[0,0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[1][0] = max(dp[0][0],-prices[1])
        dp[1][1] = max(dp[0][1],dp[0][0]+prices[1])
        for i in range(2,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-2][1]-prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i])
        return dp[-1][1]

=======
Suggestion 2

def maxProfit(self, prices: list[int]) -> int:
        buy, sell, pre_sell = -prices[0], 0, 0
        for i in range(1, len(prices)):
            buy, sell, pre_sell = max(buy, pre_sell - prices[i]), max(sell, buy + prices[i]), sell
        return sell

=======
Suggestion 3

def maxProfit(self, prices: list[int]) -> int:
        pass

=======
Suggestion 4

def maxProfit(self, prices: list[int]) -> int:
        # Dynamic Programming
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        # dp[i][0] means the maximum profit of day i with no stock in hand
        # dp[i][1] means the maximum profit of day i with stock in hand
        # dp[i-1][0] means we do not buy stock in day i
        # dp[i-1][1] + prices[i] means we sell stock in day i
        # dp[i-1][1] means we do not sell stock in day i
        # dp[i-2][0] - prices[i] means we buy stock in day i
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,len(prices)):
            if i == 1:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        return dp[-1][0]

=======
Suggestion 5

def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        dp = [[0 for _ in range(len(prices))] for _ in range(3)]
        dp[0][0] = -prices[0]
        dp[1][0] = 0
        dp[2][0] = 0
        for i in range(1, len(prices)):
            dp[0][i] = max(dp[0][i - 1], dp[2][i - 1] - prices[i])
            dp[1][i] = dp[0][i - 1] + prices[i]
            dp[2][i] = max(dp[1][i - 1], dp[2][i - 1])
        return max(dp[1][len(prices) - 1], dp[2][len(prices) - 1])

=======
Suggestion 6

def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        buy = [0] * len(prices)
        sell = [0] * len(prices)
        buy[0] = -prices[0]
        buy[1] = max(buy[0], -prices[1])
        sell[0] = 0
        sell[1] = max(sell[0], buy[0] + prices[1])
        for i in range(2, len(prices)):
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
        return sell[-1]

=======
Suggestion 7

def maxProfit(self, prices: list[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        
        for i in range(1, len(prices)):
            # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
            if i == 1:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], -prices[i])
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        return dp[-1][0]

=======
Suggestion 8

def maxProfit(self, prices: list[int]) -> int:
        dp = [[0,0,0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][2]-prices[i])
            dp[i][1] = dp[i-1][0]+prices[i]
            dp[i][2] = max(dp[i-1][1],dp[i-1][2])
        return max(dp[-1][1],dp[-1][2])

=======
Suggestion 9

def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0
        elif len(prices) == 2:
            return max(prices[1]-prices[0], 0)
        else:
            dp = [[0 for i in range(len(prices))] for j in range(3)]
            dp[0][0] = -prices[0]
            dp[1][0] = 0
            dp[2][0] = 0
            for i in range(1, len(prices)):
                dp[0][i] = max(dp[0][i-1], dp[2][i-1]-prices[i])
                dp[1][i] = dp[0][i-1]+prices[i]
                dp[2][i] = max(dp[1][i-1], dp[2][i-1])
            return max(dp[1][len(prices)-1], dp[2][len(prices)-1])

=======
Suggestion 10

def maxProfit(self, prices: list[int]) -> int:
        # dp[i][0] : the maximum profit at day i if you don't have stock
        # dp[i][1] : the maximum profit at day i if you have stock
        # dp[i][2] : the maximum profit at day i if you cooldown
        dp = [[0] * 3 for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            # if you don't have stock at day i, you can choose to do nothing or sell stock at day i-1
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # if you have stock at day i, you can choose to do nothing or buy stock at day i-1
            dp[i][1] = max(dp[i-1][1], dp[i-1][2] - prices[i])
            # if you cooldown at day i, you can only do it at day i-1
            dp[i][2] = dp[i-1][0]
        return max(dp[-1][0], dp[-1][2])
