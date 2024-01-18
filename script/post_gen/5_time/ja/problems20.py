Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def maxProfit(self, prices: list[int]) -> int:
        pass

=======
Suggestion 2

def maxProfit(self, prices: list[int]) -> int:
        # dp[i][0]：i日目において、株を持っていないときの利益
        # dp[i][1]：i日目において、株を持っているときの利益
        # dp[i][2]：i日目において、クールダウン中の利益
        dp = [[0] * 3 for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        
        for i in range(1, len(prices)):
            # i日目において、株を持っていないときの利益
            # 1. i - 1日目において、株を持っていない
            # 2. i - 1日目において、株を持っていたが、i日目に売却した
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            
            # i日目において、株を持っているときの利益
            # 1. i - 1日目において、株を持っている
            # 2. i - 2日目において、クールダウン中で、i日目に購入した
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][2] - prices[i])
            
            # i日目において、クールダウン中の利益
            # 1. i - 1日目において、株を持っていたが、i日目に売却した
            dp[i][2] = dp[i - 1][1]
            
        return max(dp[-1][0], dp[-1][2])

=======
Suggestion 3

def maxProfit(self, prices: list[int]) -> int:
        #dp[i][0]: i日目に株を持っていない場合の最大利益
        #dp[i][1]: i日目に株を持っている場合の最大利益
        #dp[i][2]: i日目に株を売却した後の翌日に株を購入することができない（つまり、クールダウンが1日ある）場合の最大利益
        #dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
        #dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
        #dp[i][2] = dp[i-1][1] + prices[i]
        dp = [[0 for _ in range(3)] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
            dp[i][2] = dp[i-1][1] + prices[i]
        return max(dp[-1][0], dp[-1][1], dp[-1][2])

=======
Suggestion 4

def maxProfit(self, prices: list[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices) + 1)]
        dp[0][1] = -float('inf')
        for i in range(1, len(prices) + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
            if i >= 2:
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i - 1])
            else:
                dp[i][1] = max(dp[i - 1][1], - prices[i - 1])
        return dp[-1][0]

=======
Suggestion 5

def maxProfit(self, prices: list[int]) -> int:
        # 1：持っている
        # 0：持っていない
        # -1：クールダウン
        dp = [[0, 0, 0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            # i日目に持っている場合は、i-1日目に持っているか、i-1日目にクールダウンしていてi日目に買ったかのどちらか
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            # i日目に持っていない場合は、i-1日目に持っていないか、i-1日目に売ったかのどちらか
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
            # i日目にクールダウンしている場合は、i-1日目に持っていたかのどちらか
            dp[i][2] = dp[i-1][1]
        return max(dp[-1][1], dp[-1][2])

=======
Suggestion 6

def maxProfit(self, prices: list[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        dp[1][1] = max(dp[0][1], -prices[1])
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        for i in range(2, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        return dp[len(prices)-1][0]

=======
Suggestion 7

def maxProfit(self, prices: list[int]) -> int:
        # 1. 状態を定義する
        # dp[i][j][k] := i 日目に j 回取引を行い、k = 0 のときは株を持っていないときの最大利益、k = 1 のときは株を持っているときの最大利益
        # 2. 状態遷移を定義する
        # dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
        # dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 2][j - 1][0] - prices[i])
        # 3. 初期条件を定義する
        # dp[0][0][0] = 0
        # dp[0][0][1] = -inf
        # dp[0][1][0] = -inf
        # dp[0][1][1] = -inf
        # 4. 漸化式をループ構造で実装する
        # 5. 答えを出力する
        n = len(prices)
        dp = [[[0] * 2 for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 0
        dp[0][1][0] = -prices[0]
        for i in range(1, n + 1):
            dp[i][0][0] = max(dp[i - 1][0][0], dp[i - 1][0][1] + prices[i - 1])
            dp[i][0][1] = max(dp[i - 1][0][1], dp[i - 1][1][0] - prices[i - 1])
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][0][0])
        return dp[n][0][0]

=======
Suggestion 8

def maxProfit(self, prices: list[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])

            if i >= 2:
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
            else:
                dp[i][1] = max(dp[i - 1][1], -prices[i])

        return dp[-1][0]

=======
Suggestion 9

def maxProfit(self, prices: list[int]) -> int:
        # 0: buy, 1: sell, 2: cooldown
        dp = [[0, 0, 0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            # buy
            dp[i][0] = max(dp[i - 1][2] - prices[i], dp[i - 1][0])
            # sell
            dp[i][1] = dp[i - 1][0] + prices[i]
            # cooldown
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        return max(dp[-1][1], dp[-1][2])
