Synthesizing 10/10 solutions

=======
Suggestion 1

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[0] * 3 for _ in range(n)]
        # 0: 持っていない
        # 1: 持っている
        # 2: クールダウン
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][2] - prices[i], dp[i - 1][1])
            dp[i][2] = dp[i - 1][0]
        return max(dp[-1][0], dp[-1][2])

=======
Suggestion 2

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(3)] for _ in range(n)]
        dp[0][0] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        return max(dp[-1][1], dp[-1][2])

=======
Suggestion 3

def maxProfit(self, prices: list[int]) -> int:
        return 0

=======
Suggestion 4

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        dp = [[0] * 3 for _ in range(n)]
        #dp[i][0]: i日目に売る場合の最大利益
        #dp[i][1]: i日目に買う場合の最大利益
        #dp[i][2]: i日目に何もしない場合の最大利益
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        for i in range(1, n):
            dp[i][0] = dp[i-1][1] + prices[i]
            if i == 1:
                dp[i][1] = max(dp[i-1][1], dp[i-1][2]) - prices[i]
            else:
                dp[i][1] = max(dp[i-1][1], dp[i-2][2]) - prices[i]
            dp[i][2] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
        return max(dp[-1][0], dp[-1][1], dp[-1][2])

=======
Suggestion 5

def maxProfit(self, prices: list[int]) -> int:
        #dp[i][0]はi日目に株を持っていない時の最大利益
        #dp[i][1]はi日目に株を持っている時の最大利益
        #dp[i][2]はi日目に株を売却した後のクールダウンの時の最大利益
        dp = [[0 for _ in range(3)] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
            dp[i][2] = dp[i-1][1] + prices[i]
        return max(dp[-1][0], dp[-1][2])

=======
Suggestion 6

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = -prices[0]
        for i in range(1, n):
            # 今日買った場合
            # 昨日売った場合の利益 - 今日の株価
            dp[i][0] = max(dp[i-1][1] - prices[i], dp[i-1][0])
            # 今日売った場合
            # 昨日買った場合の利益 + 今日の株価
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        return dp[n-1][1]

=======
Suggestion 7

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = -prices[0]
        for i in range(1, n):
            #dp[i][0]はi日目に株を持っている状態
            #dp[i][1]はi日目に株を持っていない状態でクールダウンしている状態
            #dp[i][2]はi日目に株を持っていない状態でクールダウンしていない状態
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        return max(dp[n - 1][1], dp[n - 1][2])

=======
Suggestion 8

def maxProfit(self, prices: list[int]) -> int:
        # 1日目からn日目までの株価をprices[i]とする
        # dp[i]をi日目までの株価で得られる最大利益とする
        # dp[0] = 0
        # dp[1] = max(dp[0], prices[1]-prices[0])
        # dp[i] = max(dp[i-1], prices[i]-prices[j]+dp[j-2]) (0<=j<=i-1)
        # dp[n-1]が答え
        n = len(prices)
        dp = [0] * n
        for i in range(1, n):
            dp[i] = max(dp[i-1], prices[i]-prices[i-1])
            for j in range(i-1):
                dp[i] = max(dp[i], prices[i]-prices[j]+dp[j-2])
        return dp[n-1]

=======
Suggestion 9

def maxProfit(self, prices: list[int]) -> int:
        pass

=======
Suggestion 10

def maxProfit(self, prices: list[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, len(dp)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            if i-2 < 0:
                dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
            else:
                dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])

        return dp[-1][0]
