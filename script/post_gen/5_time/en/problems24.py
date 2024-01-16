Synthesizing 10/10 solutions

=======
Suggestion 1

def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        dp=[[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            dp[i][0]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(s[i-1]==t[j-1]):
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return(dp[m][n])

=======
Suggestion 2

def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                dp[i][j] += dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[-1][-1]

=======
Suggestion 3

def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1
        for i in range(m):
            for j in range(n):
                if s[i] == t[j]:
                    dp[i+1][j+1] = dp[i][j+1] + dp[i][j]
                else:
                    dp[i+1][j+1] = dp[i][j+1]
        return dp[-1][-1]

=======
Suggestion 4

def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        @lru_cache(None)
        def dp(i, j):
            if j == n:
                return 1
            if i == m:
                return 0
            res = dp(i + 1, j)
            if s[i] == t[j]:
                res += dp(i + 1, j + 1)
            return res
        return dp(0, 0)

=======
Suggestion 5

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]*(len(s)+1) for _ in range(len(t)+1)]
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
Suggestion 6

def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][m]

=======
Suggestion 7

def numDistinct(self, s: str, t: str) -> int:
        if len(t)>len(s):
            return 0
        dp=[[0 for i in range(len(s)+1)]for j in range(len(t)+1)]
        for i in range(len(s)+1):
            dp[0][i]=1
        for i in range(1,len(t)+1):
            for j in range(1,len(s)+1):
                if s[j-1]==t[i-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i][j-1]
                else:
                    dp[i][j]=dp[i][j-1]
        return dp[len(t)][len(s)]

=======
Suggestion 8

def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m][n]

=======
Suggestion 9

def numDistinct(self, s: str, t: str) -> int:
        l1 = len(s)
        l2 = len(t)
        dp = [[0 for i in range(l1+1)] for j in range(l2+1)]
        for i in range(l1+1):
            dp[0][i] = 1
        for i in range(1,l2+1):
            for j in range(1,l1+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]+dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[l2][l1]

=======
Suggestion 10

def numDistinct(self, s: str, t: str) -> int:
        m = len(t)
        n = len(s)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for col in range(n+1):
            dp[0][col] = 1
        for row in range(1,m+1):
            for col in range(1,n+1):
                if t[row-1] == s[col-1]:
                    dp[row][col] = dp[row][col-1] + dp[row-1][col-1]
                else:
                    dp[row][col] = dp[row][col-1]
        return dp[-1][-1]
