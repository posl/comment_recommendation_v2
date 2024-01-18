Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]*(len(s)+1) for _ in range(len(t)+1)]
        for i in range(len(s)+1):
            dp[0][i] = 1
        for i in range(1,len(t)+1):
            for j in range(1,len(s)+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]

=======
Suggestion 2

def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] := sのi文字目、tのj文字目までの部分文字列の数
        # 0 <= i <= len(s)
        # 0 <= j <= len(t)
        # dp[0][0] = 1
        # dp[i][0] = 1
        # dp[0][j] = 0
        # dp[i][j] = dp[i-1][j] + dp[i-1][j-1] if s[i-1] == t[j-1]
        # dp[i][j] = dp[i-1][j] if s[i-1] != t[j-1]
        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:

=======
Suggestion 3

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

=======
Suggestion 4

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                dp[i][j] += dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[-1][-1]

=======
Suggestion 5

def numDistinct(self, s: str, t: str) -> int:
        #dp[i][j] := s[:i]からt[:j]を作る場合の数
        #dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i-1] == t[j-1]
        #dp[i][j] = dp[i-1][j] if s[i-1] != t[j-1]
        #dp[0][0] = 1
        #dp[i][0] = 1
        #dp[0][j] = 0
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                dp[i][j] += dp[i-1][j]
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
        return dp[len(t)][len(s)]

=======
Suggestion 7

def numDistinct(self, s: str, t: str) -> int:
        #メモ化再帰
        @functools.lru_cache(maxsize=None)
        def dfs(i, j):
            #tが空文字列の場合は1
            if j == -1:
                return 1
            #sが空文字列の場合は0
            if i == -1:
                return 0
            #s[i]とt[j]が等しい場合は、s[i]を使う場合と使わない場合の和
            if s[i] == t[j]:
                return dfs(i-1, j) + dfs(i-1, j-1)
            #s[i]とt[j]が等しくない場合は、s[i]を使わない場合
            else:
                return dfs(i-1, j)
        return dfs(len(s)-1, len(t)-1)

=======
Suggestion 8

def numDistinct(self, s: str, t: str) -> int:
        #dp[i][j] = sのi文字目までとtのj文字目まででの部分列の数
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        #tが空文字列の場合
        for i in range(len(s) + 1):
            dp[i][0] = 1
        #初期化
        for j in range(len(t)):
            for i in range(len(s)):
                if s[i] == t[j]:
                    dp[i + 1][j + 1] = dp[i][j] + dp[i][j + 1]
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1]
        return dp[-1][-1]

=======
Suggestion 9

def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] := s[:i] から t[:j] を作る場合の数
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        # dp[0][0] = 1
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                # s[i - 1] を選ばない場合
                dp[i][j] += dp[i - 1][j]
                # s[i - 1] を選ぶ場合
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[-1][-1]
