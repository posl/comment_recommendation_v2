Synthesizing 10/10 solutions

=======
Suggestion 1

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]
        for i in range(len(s)+1):
            dp[0][i] = 1
        for i in range(1,len(t)+1):
            for j in range(1,len(s)+1):
                if t[i-1] != s[j-1]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j-1]
        return dp[-1][-1]

=======
Suggestion 2

def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        
        if m < n:
            return 0
        
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        
        for i in range(m+1):
            dp[i][n] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
                    
        return dp[0][0]

=======
Suggestion 3

def numDistinct(self, s: str, t: str) -> int:
        sLen = len(s)
        tLen = len(t)
        dp = [[0 for i in range(tLen+1)] for j in range(sLen+1)]
        for i in range(sLen+1):
            dp[i][0] = 1
        for i in range(1, sLen+1):
            for j in range(1, tLen+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[sLen][tLen]

=======
Suggestion 4

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
        for i in range(len(s)+1):
            dp[0][i] = 1
        for i in range(1,len(t)+1):
            for j in range(1,len(s)+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = (dp[i-1][j-1] + dp[i][j-1])
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]

=======
Suggestion 5

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        for j in range(len(s) + 1):
            dp[0][j] = 1
        for i in range(len(t)):
            for j in range(len(s)):
                if t[i] == s[j]:
                    dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]
        return dp[-1][-1]

=======
Suggestion 6

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for i, c1 in enumerate(s, 1):
            for j, c2 in enumerate(t, 1):
                dp[i][j] = dp[i - 1][j] + (dp[i - 1][j - 1] if c1 == c2 else 0)
        return dp[-1][-1]

=======
Suggestion 7

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
Suggestion 8

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
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
        # DP solution
        # dp[i][j] = number of distinct subsequences of s[:i] which equals t[:j]
        # dp[i][j] = dp[i-1][j] + (dp[i-1][j-1] if s[i-1] == t[j-1] else 0)
        # dp[0][j] = 0, dp[i][0] = 1
        # O(mn) time, O(mn) space
        m, n = len(s), len(t)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1): dp[i][0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j]
                if s[i-1] == t[j-1]: dp[i][j] += dp[i-1][j-1]
        return dp[m][n]
        
        # Rolling array solution
        # dp[j] = number of distinct subsequences of s[:i] which equals t[:j]
        # dp[j] = dp[j] + (dp[j-1] if s[i-1] == t[j-1] else 0)
        # dp[0] = 1
        # O(mn) time, O(n) space
        m, n = len(s), len(t)
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        for i in range(1, m+1):
            prev = dp[0]
            for j in range(1, n+1):
                cur = dp[j]
                dp[j] = dp[j] + (prev if s[i-1] == t[j-1] else 0)
                prev = cur
        return dp[n]

=======
Suggestion 10

def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if n > m:
            return 0
        dp = [[0] * (m+1) for i in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if i == 0:
                    dp[i][j] = 1
                elif j == 0:
                    dp[i][j] = 0
                elif t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1] 
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[n][m]
