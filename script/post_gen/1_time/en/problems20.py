Synthesizing 10/10 solutions

=======
Suggestion 1

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[0 for i in range(n)] for j in range(n)]
        for k in range(1, n):
            for i in range(n-k):
                j = i + k
                if k == 1:
                    dp[i][j] = max(prices[j] - prices[i], 0)
                else:
                    dp[i][j] = dp[i+1][j]
                    for m in range(i+1, j+1):
                        if m > i+1:
                            dp[i][j] = max(dp[i][j], dp[i][m-2] + max(prices[m] - prices[i], 0) + dp[m][j])
                        else:
                            dp[i][j] = max(dp[i][j], max(prices[m] - prices[i], 0) + dp[m][j])
        return dp[0][n-1]

=======
Suggestion 2

def maxProfit(self, prices: list[int]) -> int:
        if len(prices) <= 1:
            return 0
        elif len(prices) == 2:
            if prices[1] > prices[0]:
                return prices[1] - prices[0]
            else:
                return 0
        else:
            dp = [[0 for _ in range(len(prices))] for _ in range(2)]
            dp[0][0] = 0
            dp[1][0] = -prices[0]
            dp[0][1] = max(dp[0][0], dp[1][0] + prices[1])
            dp[1][1] = max(dp[1][0], dp[0][0] - prices[1])
            for i in range(2, len(prices)):
                dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + prices[i])
                dp[1][i] = max(dp[1][i - 1], dp[0][i - 2] - prices[i])
            return dp[0][len(prices) - 1]

=======
Suggestion 3

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = -prices[0]
        dp[1][1] = max(dp[0][1], -prices[1])
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        for i in range(2, n):
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        return dp[n - 1][0]

=======
Suggestion 4

def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0
        elif len(prices) == 2:
            return max(0, prices[1]-prices[0])
        elif len(prices) == 3:
            return max(0, max(prices[1]-prices[0], prices[2]-prices[1], prices[2]-prices[0]))
        # dp[i][0] means the maximum profit on the i^th day, if the i^th day is a rest day.
        # dp[i][1] means the maximum profit on the i^th day, if the i^th day is a buy day.
        # dp[i][2] means the maximum profit on the i^th day, if the i^th day is a sell day.
        dp = [[0 for _ in range(3)] for _ in range(len(prices))]
        dp[0][0], dp[0][1], dp[0][2] = 0, -prices[0], 0
        dp[1][0], dp[1][1], dp[1][2] = 0, -prices[1], prices[1]-prices[0]
        dp[2][0], dp[2][1], dp[2][2] = max(0, max(prices[1]-prices[0], prices[2]-prices[1], prices[2]-prices[0])), max(-prices[0], -prices[1]), max(prices[1]-prices[0], prices[2]-prices[1])
        for i in range(3, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            dp[i][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])
            dp[i][2] = dp[i-1][1]+prices[i]
        return max(dp[len(prices)-1][0], dp[len(prices)-1][2])

=======
Suggestion 5

def maxProfit(self, prices: list[int]) -> int:
        buy = -prices[0]
        sell = 0
        cooldown = 0
        for i in range(1, len(prices)):
            buy = max(buy, cooldown - prices[i])
            cooldown = max(cooldown, sell)
            sell = max(sell, buy + prices[i])
        return sell

=======
Suggestion 6

def maxProfit(self, prices: list[int]) -> int:
        #DP
        #buy[i] = max(buy[i-1], sell[i-2]-price[i])
        #sell[i] = max(sell[i-1], buy[i-1]+price[i])
        buy = [0]*len(prices)
        sell = [0]*len(prices)
        buy[0] = -prices[0]
        for i in range(1, len(prices)):
            if i == 1:
                buy[i] = max(buy[i-1], -prices[i])
            else:
                buy[i] = max(buy[i-1], sell[i-2]-prices[i])
            sell[i] = max(sell[i-1], buy[i-1]+prices[i])
        return sell[-1]

=======
Suggestion 7

def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2: return 0
        a = [0] * len(prices)
        a[1] = max(0, prices[1] - prices[0])
        for i in range(2, len(prices)):
            a[i] = max(a[i - 1], prices[i] - prices[0])
            for j in range(1, i - 1):
                a[i] = max(a[i], a[j - 1] + max(0, prices[i] - prices[j + 1]))
        return a[-1]

=======
Suggestion 8

def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0
        else:
            dp = [[0,0] for i in range(len(prices))]
            dp[0][1] = -prices[0]
            dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
            dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])
            for i in range(2,len(prices)):
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
            return dp[-1][0]

=======
Suggestion 9

def maxProfit(self, prices: list[int]) -> int:
        # row 1: buy, row 2: sell, row 3: cooldown
        dp = [[0 for _ in range(len(prices))] for _ in range(3)]
        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            # buy: cooldown - price
            dp[0][i] = max(dp[0][i-1], dp[2][i-1] - prices[i])
            # sell: buy + price
            dp[1][i] = dp[0][i-1] + prices[i]
            # cooldown: max(sell, cooldown)
            dp[2][i] = max(dp[1][i-1], dp[2][i-1])
        return max(dp[1][-1], dp[2][-1])

=======
Suggestion 10

def maxProfit(self, prices: list[int]) -> int:
        #dp[i] = max(dp[i-1], prices[i] - prices[j] + dp[j-2]) for j in range(i-1)
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            maxProfit = dp[i-1]
            for j in range(i-1):
                if j >= 2:
                    maxProfit = max(maxProfit, prices[i] - prices[j] + dp[j-2])
                else:
                    maxProfit = max(maxProfit, prices[i] - prices[j])
            dp[i] = maxProfit
        return dp[-1]
