Synthesizing 10/10 solutions

=======
Suggestion 1

def numDistinct(self, s: str, t: str) -> int:
        #dp[i][j] = sのi文字目までの部分列のうち、tのj文字目までの部分列と一致するものの数
        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1] == t[j-1]:
                    #sのi文字目とtのj文字目が一致する場合
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    #sのi文字目とtのj文字目が一致しない場合
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

=======
Suggestion 2

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    dp[i+1][j+1] = dp[i][j] + dp[i][j+1]
                else:
                    dp[i+1][j+1] = dp[i][j+1]
        return dp[-1][-1]

=======
Suggestion 3

def numDistinct(self, s: str, t: str) -> int:
        #dp[i][j]はsのi番目までの文字列とtのj番目までの文字列でsのi番目までの文字列からtのj番目までの文字列を作る場合の数
        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(s)][len(t)]

=======
Suggestion 4

def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] := sのi番目までの文字列からtのj番目までの文字列を作る組み合わせ
        # とすると、dp[i][j]は以下のようになる
        # dp[i][j] = dp[i-1][j-1] + dp[i-1][j] (s[i] == t[j])
        # dp[i][j] = dp[i-1][j] (s[i] != t[j])
        # なお、dp[i][0] = 1
        # dp[0][j] = 0 (j > 0)
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for i in range(1, len(s) + 1):
            for j in range(1, min(i, len(t)) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[len(s)][len(t)]

=======
Suggestion 5

def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] := s[:i] から t[:j] を作る場合の数
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                # s[i-1] を使わない場合
                dp[i][j] += dp[i-1][j]
                # s[i-1] を使う場合
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]

        return dp[-1][-1]

=======
Suggestion 6

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
        for i in range(len(s)+1):
            dp[0][i] = 1
        for i in range(1,len(t)+1):
            for j in range(1,len(s)+1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1]+dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]

=======
Suggestion 7

def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] := sのi文字目までとtのj文字目までで作れる部分列の数
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        # dp[i][0] = 1
        for i in range(len(s) + 1):
            dp[i][0] = 1
        # dp[i][j] = dp[i-1][j] + dp[i-1][j-1] if s[i-1] == t[j-1]
        # dp[i][j] = dp[i-1][j] if s[i-1] != t[j-1]
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                dp[i][j] += dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[-1][-1]

=======
Suggestion 8

def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j]: sのi文字目までとtのj文字目までの部分列数
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        # dp[i][0] = 1: sのi文字目までと空文字の部分列数は1
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                # s[i-1]とt[j-1]が等しいとき、
                # dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                # s[i-1]とt[j-1]が等しくないとき、
                # dp[i][j] = dp[i-1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

=======
Suggestion 9

def numDistinct(self, s: str, t: str) -> int:
        #dp[i][j] = s[i]まででt[j]までの部分列の数
        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

=======
Suggestion 10

def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] := sのi文字目までとtのj文字目までで作れる部分列の個数
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        # dp[0][0] = 1とすると、dp[1][1]のとき、s[1] == t[1]のときに1となってしまう
        # dp[0][0] = 1とすると、dp[1][0]のとき、s[1] == t[0]のときに1となってしまう
        # dp[0][0] = 1とすると、dp[0][1]のとき、s[0] == t[1]のときに1となってしまう
        # dp[0][0] = 1とすると、dp[0][1]のとき、s[0] == t[0]のときに1となってしまう
        # dp[0][0] = 1とすると、dp[0][1]のとき、s[0] == t[0]のときに1となってしまう
        # dp[0][0] = 1とすると、dp[1][0]のとき、s[0] == t[0]のときに1となってしまう
        # dp[0][0] = 1とすると、dp[1][1]のとき、s[0] == t[0]のときに1となってしまう
        # dp[0][0] = 1とすると、dp[1][1]のとき、s[0] == t[1]のときに1となってしまう
        # dp[0][0] = 1とすると、dp[1][1]のとき、s[1] == t[0]のときに1となってしまう
        # dp[0][0] = 1とすると、dp[1][1]のとき
