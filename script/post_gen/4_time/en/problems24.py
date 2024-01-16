Synthesizing 10/10 solutions

=======
Suggestion 1

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]*(len(s)+1) for _ in range(len(t)+1)]
        for i in range(len(s)+1):
            dp[0][i] = 1
        for i in range(1,len(t)+1):
            for j in range(1,len(s)+1):
                if t[i-1]==s[j-1]:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]

=======
Suggestion 2

def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        dp=[[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(n+1):
            dp[i][0]=1
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][m]

=======
Suggestion 3

def numDistinct(self, s: str, t: str) -> int:
        if not s or not t:
            return 0
        
        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        
        for i in range(len(s)+1):
            dp[i][0] = 1
            
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[len(s)][len(t)]

=======
Suggestion 4

def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] stores the number of distinct subsequences of s[0:i+1] which equals t[0:j+1]
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        # base case: dp[i][0] = 1, dp[0][j] = 0
        for i in range(len(s)+1):
            dp[i][0] = 1
        # state transition:
        # if s[i] == t[j]: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        # else: dp[i][j] = dp[i-1][j]
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] != t[j-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp[-1][-1]

=======
Suggestion 5

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[len(s)][len(t)]

=======
Suggestion 6

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for i in range(len(s) + 1)] for j in range(len(t) + 1)]
        for i in range(len(s) + 1):
            dp[0][i] = 1
        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                dp[i][j] = dp[i][j - 1]
                if t[i - 1] == s[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[-1][-1]

=======
Suggestion 7

def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1): 
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]
        return dp[0][0]

=======
Suggestion 8

def numDistinct(self, s: str, t: str) -> int:
        #dp[i][j] is the number of distinct subsequences of s[:i] which equals t[:j]
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else: dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

=======
Suggestion 9

def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
        for i in range(len(s)+1):
            dp[0][i] = 1
        for i in range(1, len(t)+1):
            for j in range(1, len(s)+1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]

=======
Suggestion 10

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] means the number of distinct subsequences of s[:i] which equals t[:j]
        # dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i-1] == t[j-1]
        #          = dp[i-1][j] if s[i-1] != t[j-1]
        #          = 1 if j == 0
        #          = 0 if i == 0
        # dp[0][0] = 1
        # dp[0][j] = 0 for j > 0
        # dp[i][0] = 1 for i > 0
        # dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i-1] == t[j-1]
        #          = dp[i-1][j] if s[i-1] != t[j-1]
        #          = 1 if j == 0
        #          = 0 if i == 0
        # dp[0][0] = 1
        # dp[0][j] = 0 for j > 0
        # dp[i][0] = 1 for i > 0
        # dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i-1] == t[j-1]
        #          = dp[i-1][j] if s[i-1] != t[j-1]
        #          = 1 if j == 0
        #          = 0 if i == 0
        # dp[0][0] = 1
        # dp[0][j] = 0 for j > 0
        # dp[i][0] = 1 for i > 0
        # dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i-1] == t[j-1]
        #          = dp[i-1][j] if s[i-1] != t[j-1]
        #          = 1 if j == 0
        #          = 0 if i == 0
        # dp
