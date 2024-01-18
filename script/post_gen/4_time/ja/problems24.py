Synthesizing 10/10 solutions

=======
Suggestion 1

def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] := Sのi文字目までとTのj文字目までの部分列の数
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        # dp[0][0] = 1
        dp[0][0] = 1

        for i in range(len(s)):
            for j in range(len(t) + 1):
                # Sのi文字目を使わない場合
                dp[i + 1][j] += dp[i][j]
                # Sのi文字目を使う場合
                if j < len(t) and s[i] == t[j]:
                    dp[i + 1][j + 1] += dp[i][j]

        return dp[-1][-1]

=======
Suggestion 2

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for j in range(1, len(t) + 1):
            for i in range(1, len(s) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

=======
Suggestion 3

def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] := sのi文字目までとtのj文字目までの部分列の数
        # dp[0][0] = 1
        # dp[0][j] = 0
        # dp[i][0] = 1
        # dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i-1] == t[j-1]
        #          = dp[i-1][j] otherwise
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for j in range(1, len(t) + 1):
            dp[0][j] = 0
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                dp[i][j] = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[len(s)][len(t)]

=======
Suggestion 4

def numDistinct(self, s: str, t: str) -> int:
        pass

=======
Suggestion 5

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
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
Suggestion 6

def numDistinct(self, s: str, t: str) -> int:
        #dp[i][j] := sのi文字目までとtのj文字目までの部分列の数
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j]+dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

=======
Suggestion 7

def numDistinct(self, s: str, t: str) -> int:
        #dp[i][j] := sのi番目までの文字列を使ってtのj番目までの文字列を作る場合の数
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        #初期条件
        for i in range(len(s) + 1):
            dp[i][0] = 1
        #dp更新
        for i in range(len(s)):
            for j in range(len(t)):
                #文字が一致した場合、dp[i][j]はdp[i-1][j-1]の場合の数に等しい
                if s[i] == t[j]:
                    dp[i+1][j+1] = dp[i][j] + dp[i][j+1]
                #文字が一致しない場合、dp[i][j]はdp[i-1][j]の場合の数に等しい
                else:
                    dp[i+1][j+1] = dp[i][j+1]
        return dp[-1][-1]

=======
Suggestion 8

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
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
Suggestion 9

def numDistinct(self, s: str, t: str) -> int:
        # DP
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        for i in range(len(s) + 1):
            dp[0][i] = 1
        for i in range(len(t)):
            for j in range(len(s)):
                if t[i] == s[j]:
                    dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]
        return dp[-1][-1]

=======
Suggestion 10

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(t))] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    elif i == 0:
                        dp[i][j] = dp[i][j-1] + 1
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    if i == 0 and j == 0:
                        dp[i][j] = 0
                    elif i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i][j-1]
        return dp[len(s)-1][len(t)-1]
