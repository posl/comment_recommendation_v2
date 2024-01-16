Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def maxProfit(self, prices: list[int]) -> int:
        # 1. DP
        # 2. state: dp[i] = max(dp[i-1], dp[j-2] + prices[i] - prices[j])
        # 3. init: dp[0] = 0, dp[1] = 0, dp[2] = prices[1] - prices[0]
        # 4. func: dp[i] = max(dp[i-1], dp[j-2] + prices[i] - prices[j])
        # 5. res: dp[n-1]
        n = len(prices)
        if n < 2:
            return 0
        dp = [0] * n
        dp[1] = max(0, prices[1] - prices[0])
        for i in range(2, n):
            dp[i] = dp[i-1]
            for j in range(i):
                if j >= 2:
                    dp[i] = max(dp[i], dp[j-2] + prices[i] - prices[j])
                else:
                    dp[i] = max(dp[i], prices[i] - prices[j])
        return dp[n-1]

=======
Suggestion 3

def maxProfit(self, prices: list[int]) -> int:
        #DP
        #dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        #dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        if len(prices) < 2:
            return 0
        dp = [[0,0] for _ in range(len(prices))]
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
        return dp[-1][0]

=======
Suggestion 4

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [0] * n
        for i in range(1, n):
            dp[i] = dp[i-1]
            for j in range(i):
                if prices[i] > prices[j]:
                    dp[i] = max(dp[i], dp[j-2] + prices[i] - prices[j])
        return dp[-1]

=======
Suggestion 5

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            if i == 1:
                dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
            else:
                dp[i][1] = max(dp[i-1][1],dp[i-2][0]-prices[i])
        return dp[n-1][0]

=======
Suggestion 6

def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        buy = [0] * len(prices)
        sell = [0] * len(prices)
        buy[0] = -prices[0]
        buy[1] = max(-prices[0], -prices[1])
        sell[1] = max(0, prices[1] - prices[0])
        for i in range(2, len(prices)):
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
            sell[i] = max(sell[i-1], prices[i] + buy[i-1])
        return sell[-1]

=======
Suggestion 7

def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        dp[1][1] = -prices[1]
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        for i in range(2, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 2][0] - prices[i], dp[i - 1][1])
        return dp[-1][0]

=======
Suggestion 8

def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        buy = [0] * len(prices)
        sell = [0] * len(prices)
        buy[0] = -prices[0]
        buy[1] = max(-prices[0], -prices[1])
        sell[1] = max(0, prices[1] - prices[0])
        for i in range(2, len(prices)):
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
        return sell[-1]

=======
Suggestion 9

def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        dp = [[0,0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        dp[1][1] = max(-prices[0], -prices[1])
        dp[1][0] = max(0, prices[1] - prices[0])
        for i in range(2,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-2][0] - prices[i])
        return dp[-1][0]

=======
Suggestion 10

def maxProfit(self, prices: list[int]) -> int:
        #dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + prices[i])
        #dp[1][i] = max(dp[1][i - 1], dp[0][i - 2] - prices[i])
        dp = [[0 for _ in range(len(prices))] for _ in range(2)]
        dp[0][0] = 0
        dp[1][0] = -prices[0]
        dp[0][1] = max(dp[0][0], dp[1][0] + prices[1])
        dp[1][1] = max(dp[1][0], dp[0][0] - prices[1])
        for i in range(2, len(prices)):
            dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + prices[i])
            dp[1][i] = max(dp[1][i - 1], dp[0][i - 2] - prices[i])
        return dp[0][len(prices) - 1]
