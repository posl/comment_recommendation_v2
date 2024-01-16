Synthesizing 10/10 solutions

=======
Suggestion 1

def numDistinct(self, s: str, t: str) -> int:
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
Suggestion 2

def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i] == t[j]
        #          = dp[i-1][j] if s[i] != t[j]
        # dp[i][j] means the number of distinct subsequences of s[:i] which equals t[:j]
        m, n = len(s), len(t)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = 1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] != t[j-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
        
        return dp[m][n]

=======
Suggestion 3

def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] means the number of distinct subsequences of s[:i] which equals t[:j]
        # if s[i-1] == t[j-1], dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        # else dp[i][j] = dp[i-1][j]
        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

=======
Suggestion 4

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
        for i in range(len(s)+1):
            dp[0][i] = 1
        for i in range(1,len(t)+1):
            for j in range(1,len(s)+1):
                if t[i-1]==s[j-1]:
                    dp[i][j] = dp[i-1][j-1]+dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]

=======
Suggestion 5

def numDistinct(self, s: str, t: str) -> int:
        if not s or not t: return 0
        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1] == t[j-1]: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else: dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

=======
Suggestion 6

def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        if len(t) == len(s):
            return 1 if t == s else 0
        if len(t) == 0:
            return 1
        dp = [[0 for _ in range(len(t))] for _ in range(len(s))]
        dp[0][0] = 1 if s[0] == t[0] else 0
        for i in range(1, len(s)):
            dp[i][0] = dp[i - 1][0] + 1 if s[i] == t[0] else dp[i - 1][0]
        for i in range(1, len(s)):
            for j in range(1, len(t)):
                if i < j:
                    dp[i][j] = 0
                elif i == j:
                    dp[i][j] = 1 if s[i] == t[j] else 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] if s[i] == t[j] else dp[i - 1][j]
        return dp[len(s) - 1][len(t) - 1]

=======
Suggestion 7

def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
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
Suggestion 8

def numDistinct(self, s: str, t: str) -> int:
        #dp[i][j] = number of distinct subsequences of s[0:i] which equals t[0:j]
        #dp[i][j] = dp[i-1][j] + (dp[i-1][j-1] if s[i-1] == t[j-1] else 0)
        #dp[0][j] = 0
        #dp[i][0] = 1
        dp = [[1] + [0]*len(t)] + [[0]*(len(t)+1) for _ in range(len(s))]
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                dp[i][j] = dp[i-1][j] + (dp[i-1][j-1] if s[i-1] == t[j-1] else 0)
        return dp[-1][-1]

=======
Suggestion 9

def numDistinct(self, s: str, t: str) -> int:
        if len(s) == len(t):
            if s == t:
                return 1
            else:
                return 0
        if len(s) == 0:
            return 0
        if len(t) == 0:
            return 1
        return self.numDistinct(s[1:],t) + (self.numDistinct(s[1:],t[1:]) if s[0] == t[0] else 0)

=======
Suggestion 10

def numDistinct(self, s: str, t: str) -> int:
        #Dynamic Programming
        #Time Complexity: O(len(s)*len(t))
        #Space Complexity: O(len(s)*len(t))
        #Algorithm: dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i] == t[j]
        #                         dp[i-1][j] if s[i] != t[j]
        #Base Case: dp[i][0] = 1
        #           dp[0][j] = 0
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for i in range(1,len(s) + 1):
            for j in range(1,len(t) + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else: 
                    dp[i][j] = dp[i-1][j]
        return dp[len(s)][len(t)]
