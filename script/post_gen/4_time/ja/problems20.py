Synthesizing 10/10 solutions

=======
Suggestion 1

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[1][0] = max(dp[0][0], -prices[1])
        dp[1][1] = max(dp[0][1], dp[0][0] + prices[1])
        for i in range(2, n):
            dp[i][0] = max(dp[i-1][0], dp[i-2][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        return dp[n-1][1]

=======
Suggestion 2

def maxProfit(self, prices: list[int]) -> int:
        # 0:持っていない 1:持っている 2:冷却中
        dp = [[0 for _ in range(3)] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            # 持っていない場合は、前日も持っていないか、前日は冷却中で今日買った
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            # 持っている場合は、前日も持っているか、前日は持っていなくて今日買った
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            # 冷却中の場合は、前日も冷却中か、前日は持っていて今日売った
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1])
        return max(dp[-1][0], dp[-1][1], dp[-1][2])

=======
Suggestion 3

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 1日目で買うか買わないか
        # 2日目で買うか買わないか
        # 3日目で買うか買わないか
        # 4日目で買うか買わないか
        # 5日目で買うか買わないか
        # 6日目で買うか買わないか
        # 7日目で買うか買わないか
        # 8日目で買うか買わないか
        # 9日目で買うか買わないか
        # 10日目で買うか買わないか
        # 11日目で買うか買わないか
        # 12日目で買うか買わないか
        # 13日目で買うか買わないか
        # 14日目で買うか買わないか
        # 15日目で買うか買わないか
        # 16日目で買うか買わないか
        # 17日目で買うか買わないか
        # 18日目で買うか買わないか
        # 19日目で買うか買わないか
        # 20日目で買うか買わないか
        # 21日目で買うか買わないか
        # 22日目で買うか買わないか
        # 23日目で買うか買わないか
        # 24日目で買うか買わないか
        # 25日目で買うか買わないか
        # 26日目で買うか買わないか
        # 27日目で買うか買わないか
        # 28日目で買うか買

=======
Suggestion 4

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[0,0] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[1][0] = max(dp[0][0], dp[0][1]+prices[1])
        dp[1][1] = max(dp[0][1], dp[0][0]-prices[1])
        for i in range(2, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-2][0]-prices[i], dp[i-1][1])
        return dp[n-1][0]

=======
Suggestion 5

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        #dp[i][0]はi日目に株を持っていない時の最大利益
        #dp[i][1]はi日目に株を持っている時の最大利益
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        
        for i in range(1, n):
            #i日目に株を持っていない時の最大利益は、i-1日目に株を持っていない時の最大利益とi-1日目に売却した時の利益の大きい方
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            #i日目に株を持っている時の最大利益は、i-1日目に株を持っている時の最大利益とi-2日目に株を持っていない時の最大利益からi日目に株を買った時の利益の大きい方
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        
        #最後に株を持っていない時の最大利益が答え
        return dp[n - 1][0]

=======
Suggestion 6

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = -prices[0]
        dp[1][1] = -prices[1]
        dp[2][1] = max(dp[0][1], dp[1][1])
        dp[2][0] = max(dp[1][0], dp[1][1] + prices[2])
        for i in range(3, n):
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        return dp[n - 1][0]

=======
Suggestion 7

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1, n):
            # 今日持っていない場合、昨日持っていない or 昨日持っていて、今日売った場合
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            # 今日持っている場合、昨日持っていない or 昨日持っていて、今日買った場合
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
        return dp[-1][0]

=======
Suggestion 8

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[0] * 3 for _ in range(n)]
        #dp[i][0]はi日目に買っているときの最大利益
        #dp[i][1]はi日目に売っているときの最大利益
        #dp[i][2]はi日目に休んでいるときの最大利益
        dp[0][0] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][2] - prices[i], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][0] + prices[i], dp[i - 1][1])
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        return max(dp[n - 1][1], dp[n - 1][2])

=======
Suggestion 9

def maxProfit(self, prices: list[int]) -> int:
        # 価格の変化を記録する
        changes = [prices[i]-prices[i-1] for i in range(1, len(prices))]
        # 価格の変化を記録した配列が空の場合
        if not changes:
            return 0
        # 価格の変化を記録した配列が1つの要素の場合
        if len(changes) == 1:
            return max(changes[0], 0)
        # 価格の変化を記録した配列が2つの要素の場合
        if len(changes) == 2:
            return max(changes[0], changes[1], 0)
        # 価格の変化を記録した配列が3つ以上の要素の場合
        # 価格の変化を記録した配列の先頭3つの要素を初期値とする
        dp = [changes[0], changes[0]+changes[1], max(changes[0]+changes[2], changes[1]+changes[2], 0)]
        # 価格の変化を記録した配列の先頭3つの要素を除いた残りの要素に対してループ処理
        for i in range(3, len(changes)):
            # i 日目の株価を売却する場合
            sell = dp[i-2] + changes[i]
            # i 日目の株価を購入しない場合
            no_buy = dp[i-1]
            # i 日目の株価を購入する場合
            buy = dp[i-3] + changes[i]
            # i 日目の株価を売却する場合と購入しない場合と購入する場合の最大値を i 日目の最大利益とする
            dp.append(max(sell, no_buy, buy))
        # 価格の変化を記録した配列の最後の要素が最大利益となる

=======
Suggestion 10

def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0, 0] for _ in range(n)]
        # dp[i][0]はi日目に持っている株の最大利益
        # dp[i][1]はi日目に持っていない株の最大利益
        dp[0][0] = -prices[0]
        for i in range(1, n):
            # i日目に株を持っている場合
            # i-1日目に株を持っていた場合と、i-2日目に株を持っていなかった場合から選ぶ
            dp[i][0] = max(dp[i - 1][0], dp[i - 2][1] - prices[i])
            # i日目に株を持っていない場合
            # i-1日目に株を持っていない場合と、i-1日目に株を持っていた場合から選ぶ
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        return dp[-1][1]
