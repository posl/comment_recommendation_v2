Synthesizing 10/10 solutions

=======
Suggestion 1

def numDistinct(self, s: str, t: str) -> int:
        # DP
        # dp[i][j] = sのi番目までの文字列からtのj番目までの文字列を作る方法の数
        # dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i] == t[j]
        #          = dp[i-1][j] if s[i] != t[j]
        m, n = len(s), len(t)
        # dp = [[0] * (n + 1) for _ in range(m + 1)]
        # for i in range(m + 1):
        #     dp[i][0] = 1
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if s[i - 1] == t[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        #         else:
        #             dp[i][j] = dp[i - 1][j]
        # return dp[m][n]
        # dp = [1] * (n + 1)
        # for i in range(1, m + 1):
        #     prev = 1
        #     for j in range(1, n + 1):
        #         tmp = dp[j]
        #         if s[i - 1] == t[j - 1]:
        #             dp[j] += prev
        #         prev = tmp
        # return dp[n]
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, m + 1):
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[n]

=======
Suggestion 2

def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] := s[i:] と t[j:] において、t[j] と s[i] が一致している場合における部分列の数
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        # t が空文字列の場合、空文字列の部分列は s のどの位置でも一つだけ存在する
        for i in range(len(s) + 1):
            dp[i][len(t)] = 1
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                # t[j] と s[i] が一致しない場合、t[j] を s[i] に一致させることはできない
                if s[i] != t[j]:
                    dp[i][j] = dp[i + 1][j]
                # t[j] と s[i] が一致する場合、t[j] を s[i] に一致させることができる
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i + 1][j + 1]
        return dp[0][0]

=======
Suggestion 3

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        for i in range(len(s)):
            dp[i][0] = 1
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i]==t[j]:
                    dp[i+1][j+1] = dp[i][j]+dp[i][j+1]
                else:
                    dp[i+1][j+1] = dp[i][j+1]
        return dp[-1][-1]

=======
Suggestion 4

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # sの文字列の中から、tの文字列を抜き出す
        # その組み合わせの数を求める
        # s = "rabbbit", t = "rabbit"
        # まず、rabbbitの中から、rを探し、rが見つかったら、
        # その次の文字を探す
        # rが見つかったら、次の文字を探す
        # これを繰り返す
        # rが見つからなかったら、次の文字を探す
        # これを繰り返す
        # sの文字列をすべて探す
        # これを繰り返す
        # こうすると、rabbbitの中から、rabbitを取り出すことができる
        # その組み合わせの数を求める
        # これを繰り返す
        # こうすると、sの文字列の中から、tの文字列を抜き出すことができる
        # その組み合わせの数を求める
        # これを繰り返す
        # こうすると、sの文字列の中から、tの文字列を抜き出すことができる
        # その組み合わせの数を求める
        # これを繰り返す
        # こうすると、sの文字列の中から、tの文字列を抜き出すことができる
        # その組み合わせの数を求める
        # これを繰り返す
        # こうすると、sの文字列の中から、tの文字列を抜き出すことができる
        # その組み合わせの数を求める
        # これを繰り返す

=======
Suggestion 5

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(t))]
        for i in range(len(s)):
            if s[i] == t[0]:
                dp[0][i] = 1
        for i in range(1,len(t)):
            for j in range(i,len(s)):
                if t[i] == s[j]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]

=======
Suggestion 6

def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        elif len(t) == 0:
            return 1
        else:
            dp = [[0]*(len(t)+1) for i in range(len(s)+1)]
            for i in range(len(s)+1):
                dp[i][0] = 1
            for i in range(1,len(s)+1):
                for j in range(1,len(t)+1):
                    if s[i-1] == t[j-1]:
                        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]
            return dp[len(s)][len(t)]

=======
Suggestion 7

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] = 0, if s[i] != t[j]
        #            dp[i-1][j-1] + dp[i-1][j], if s[i] == t[j]
        # dp[i][0] = 1
        # dp[0][j] = 0, if i == 0
        #            1, if s[0] == t[j]
        #            0, if s[0] != t[j]
        # dp[0][0] = 1, if s[0] == t[0]
        #            0, if s[0] != t[0]
        # dp[i][j] = dp[i-1][j-1] + dp[i-1][j], if s[i] == t[j]
        #          = dp[i-1][j], if s[i] != t[j]
        # dp[i][0] = 1
        # dp[0][j] = 0, if i == 0
        #            1, if s[0] == t[j]
        #            0, if s[0] != t[j]
        # dp[0][0] = 1, if s[0] == t[0]
        #            0, if s[0] != t[0]
        # dp[i][j] = dp[i-1][j-1] + dp[i-1][j], if s[i] == t[j]
        #          = dp[i-1][j], if s[i] != t[j]
        # dp[i][0] = 1
        # dp[0][j] = 0, if i == 0
        #            1, if s[0] == t[j]
        #            0, if s[0] != t[j]
        # dp[0][0] = 1, if s[0] == t[0]
        #            0, if s[0] != t[0]
        # dp[i][j] = dp[i-1][j-1] + dp[i-1][j], if s[i] == t[j]
        #          = dp[i-1][j], if s[i] != t[j]
        # dp[i][

=======
Suggestion 8

def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        for i in range(len(s) + 1):
            dp[0][i] = 1
        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[-1][-1]

=======
Suggestion 9

def numDistinct(self, s: str, t: str) -> int:
        #dp[i][j] := sのi文字目までを使ってtのj文字目までを作る方法の数
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        #初期化
        for i in range(len(s) + 1):
            dp[i][0] = 1
        #dp
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                #s[i-1]とt[j-1]が一致するとき
                if s[i-1] == t[j-1]:
                    #sのi-1文字目を使う場合と使わない場合
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                #一致しないとき
                else:
                    #sのi-1文字目を使わない場合
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

=======
Suggestion 10

def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] := sのi文字目までとtのj文字目までの部分列の数
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]

        # dp[0][0] = 1とする
        dp[0][0] = 1

        for i in range(len(s)+1):
            for j in range(len(t)+1):
                # sのi文字目までとtのj文字目までの部分列の数
                dp[i][j] = dp[i-1][j]
                # sのi文字目までとtのj文字目までの部分列の数
                # ただし、s[i-1] == t[j-1]の場合
                if i > 0 and j > 0 and s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]

        return dp[len(s)][len(t)]
