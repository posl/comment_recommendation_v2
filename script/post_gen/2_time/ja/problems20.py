Synthesizing 10/10 solutions

=======
Suggestion 1

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = -float('inf')
        dp_pre_0 = 0

=======
Suggestion 2

def maxProfit(self, prices: list[int]) -> int:
        #dp[i][0]: i日目に株を持っていない時の最大利益
        #dp[i][1]: i日目に株を持っている時の最大利益
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        
        for i in range(len(prices)):
            if i == 0:
                continue
            #今日株を持っていない場合
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            #今日株を持っている場合
            if i == 1:
                dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
            else:
                dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
        
        return dp[-1][0]

=======
Suggestion 3

def maxProfit(self, prices: list[int]) -> int:
        # 2次元配列を作成する
        dp = [[0, 0, 0] for _ in range(len(prices))]
        # 0: 何もしない
        # 1: 買う
        # 2: 売る
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            # 何もしない場合
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            # 買う場合
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
            # 売る場合
            dp[i][2] = dp[i-1][1] + prices[i]
        return max(dp[-1][0], dp[-1][2])

=======
Suggestion 4

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            if i >= 2:
                dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
            else:
                dp[i][1] = max(dp[i-1][1], -prices[i])
        return dp[n-1][0]

=======
Suggestion 5

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 1 <= prices.length <= 5000
        # 0 <= prices[i] <= 1000
        # 0 <= i <= 4999
        # 0 <= i + 2 <= 4999
        # 0 <= i + 1 <= 4999
        # 0 <= i - 1 <= 4999
        # 0 <= i - 2 <= 4999
        # 0 <= i - 3 <= 4999
        # 0 <= i - 4 <= 4999
        # 0 <= i - 5 <= 4999
        # 0 <= i - 6 <= 4999
        # 0 <= i - 7 <= 4999
        # 0 <= i - 8 <= 4999
        # 0 <= i - 9 <= 4999
        # 0 <= i - 10 <= 4999
        # 0 <= i - 11 <= 4999
        # 0 <= i - 12 <= 4999
        # 0 <= i - 13 <= 4999
        # 0 <= i - 14 <= 4999
        # 0 <= i - 15 <= 4999
        # 0 <= i - 16 <= 4999
        # 0 <= i - 17 <= 4999
        # 0 <= i - 18 <= 4999
        # 0 <= i - 19 <= 4999
        # 0 <= i - 20 <= 4999
        # 0 <= i - 21 <= 4999
        # 0 <= i - 22 <= 4999
        # 0 <= i - 23 <= 4999
        # 0 <= i - 24 <= 4999
        # 0 <= i - 25 <= 4999
        # 0 <= i - 26 <= 4999
        # 0 <= i - 27 <= 4999
        # 0 <= i - 28 <= 4999
        # 0 <= i - 29 <= 4999
        # 0 <= i - 30 <= 4999
        # 0 <= i - 31 <= 4999

=======
Suggestion 6

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        # 0: 持ってない
        # 1: 持ってる
        # 2: クールダウン中
        dp = [[0] * 3 for _ in range(n+1)]
        dp[0][0] = 0
        dp[0][1] = -float('inf')
        dp[0][2] = -float('inf')
        for i in range(1, n+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            dp[i][1] = max(dp[i-1][0] - prices[i-1], dp[i-1][1])
            dp[i][2] = dp[i-1][1] + prices[i-1]
        return max(dp[n][0], dp[n][2])

=======
Suggestion 7

def maxProfit(self, prices: list[int]) -> int:
        # dp[i][0] : i日目に持ってないときの最大利益
        # dp[i][1] : i日目に持っているときの最大利益
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])

        for i in range(2, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-2][0] - prices[i], dp[i-1][1])

        return dp[-1][0]

=======
Suggestion 8

def maxProfit(self, prices: list[int]) -> int:
        dp = [[0, 0, 0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        return max(dp[-1][1], dp[-1][2])

=======
Suggestion 9

def maxProfit(self, prices: list[int]) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])
        for i in range(2, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 2][0] - prices[i], dp[i - 1][1])
        return dp[-1][0]

=======
Suggestion 10

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[0] * 3 for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][2], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = dp[i - 1][1] + prices[i]
        return max(dp[n - 1][0], dp[n - 1][2])
