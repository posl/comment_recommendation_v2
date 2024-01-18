Synthesizing 10/10 solutions

=======
Suggestion 1

def maxProfit(self, prices: list[int]) -> int:
        buy = -prices[0]
        sell = 0
        cooldown = 0
        for i in range(1, len(prices)):
            buy = max(buy, cooldown - prices[i])
            cooldown = sell
            sell = max(sell, buy + prices[i])
        return sell

=======
Suggestion 2

def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0
        dp = [[0,0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        dp[1][0] = max(dp[0][0],dp[0][1]+prices[1])
        dp[1][1] = max(dp[0][1],dp[0][0]-prices[1])
        for i in range(2,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-2][0]-prices[i])
        return dp[-1][0]

=======
Suggestion 3

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[1][0] = max(-prices[0], -prices[1])
        dp[1][1] = max(0, prices[1] - prices[0])
        for i in range(2, n):
            dp[i][0] = max(dp[i-1][0], dp[i-2][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        return dp[n-1][1]

=======
Suggestion 4

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = -prices[0]
        dp[1][1] = max(-prices[0], -prices[1])
        dp[1][0] = max(0, prices[1] - prices[0])
        for i in range(2, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 2][0] - prices[i], dp[i - 1][1])
        return dp[n - 1][0]

=======
Suggestion 5

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 1日目は買うことができる
        # 1日目の株価を買う
        # 2日目は売ることができる
        # 2日目の株価を売る
        # 3日目はクールダウン
        # 3日目の株価を買う
        # 4日目は売ることができる
        # 4日目の株価を売る
        # 5日目はクールダウン
        # 5日目の株価を買う
        # 6日目は売ることができる
        # 6日目の株価を売る
        # 7日目はクールダウン
        # 7日目の株価を買う
        # 8日目は売ることができる
        # 8日目の株価を売る
        # 9日目はクールダウン
        # 9日目の株価を買う
        # 10日目は売ることができる
        # 10日目の株価を売る
        # 11日目はクールダウン
        # 11日目の株価を買う
        # 12日目は売ることができる
        # 12日目の株価を売る
        # 13日目はクールダウン
        # 13日目の株価を買う
        # 14日目は売ることができる
        # 14日目の株価を売る
        # 15日目はクールダウン
        # 15日目の株価を買う
        # 16日目は売ることができる
        # 16日目の株価を売る
        # 17日目はクールダウン
        #

=======
Suggestion 6

def maxProfit(self, prices: list[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[1][0] = max(dp[0][0], dp[0][1]+prices[1])
        dp[1][1] = max(dp[0][1], dp[0][0]-prices[1])
        for i in range(2, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-2][0]-prices[i], dp[i-1][1])
        return dp[-1][0]

=======
Suggestion 7

def maxProfit(self, prices: list[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], (dp[i - 2][1] if i >= 2 else 0) - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        return dp[-1][1]

=======
Suggestion 8

def maxProfit(self, prices: list[int]) -> int:
        if len(prices) <= 1:
            return 0
        elif len(prices) == 2:
            return max(0, prices[1] - prices[0])
        elif len(prices) == 3:
            return max(0, prices[2] - prices[0], prices[1] - prices[0], prices[2] - prices[1])
        else:
            dp = [[0 for _ in range(len(prices))] for _ in range(3)]
            dp[0][0] = -prices[0]
            dp[0][1] = max(-prices[0], -prices[1])
            dp[1][1] = max(0, prices[1] - prices[0])
            dp[0][2] = max(dp[0][1], dp[1][1] - prices[2])
            dp[1][2] = max(dp[1][1], dp[0][1] + prices[2])
            for i in range(3, len(prices)):
                dp[0][i] = max(dp[0][i - 1], dp[1][i - 2] - prices[i])
                dp[1][i] = max(dp[1][i - 1], dp[0][i - 1] + prices[i])
            return dp[1][len(prices) - 1]

=======
Suggestion 9

def maxProfit(self, prices: list[int]) -> int:
        # dp[i][0]はi日目に株を持っていない時の最大利益
        # dp[i][1]はi日目に株を持っていて、クールダウン中の時の最大利益
        # dp[i][2]はi日目に株を持っていて、クールダウンをしていない時の最大利益
        # とすると、
        # dp[i][0] = max(dp[i-1][0], dp[i-1][2])
        # dp[i][1] = dp[i-1][0] + prices[i]
        # dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        # となる
        # dp[0][0] = 0
        # dp[0][1] = -prices[0]
        # dp[0][2] = 0
        n = len(prices)
        dp = [[0] * 3 for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            dp[i][1] = dp[i-1][0] - prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        return max(dp[n-1][0], dp[n-1][2])

=======
Suggestion 10

def maxProfit(self, prices: list[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        for i in range(1, len(dp)):
            dp[i][0] = max(dp[i-1][1] + prices[i], dp[i-1][0])
            if i >= 2:
                dp[i][1] = max(dp[i-2][0] - prices[i], dp[i-1][1])
            else:
                dp[i][1] = max(-prices[i], dp[i-1][1])
        return dp[-1][0]
