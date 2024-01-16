Synthesizing 10/10 solutions

=======
Suggestion 1

def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if s[i] == t[j]:
                return dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                return dfs(i + 1, j)
        return dfs(0, 0)

=======
Suggestion 2

def numDistinct(self, s: str, t: str) -> int:
        if not s or not t:
            return 0
        if len(s) < len(t):
            return 0
        dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(s)][len(t)]

=======
Suggestion 3

def numDistinct(self, s: str, t: str) -> int:
        #dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i] = t[j]
        #dp[i][j] = dp[i-1][j] if s[i] != t[j]
        #dp[0][0] = 1
        #dp[i][0] = 1
        #dp[0][j] = 0
        #dp[i][j] = 0 if i < j
        #dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i] = t[j]
        #dp[i][j] = dp[i-1][j] if s[i] != t[j]
        #dp[0][0] = 1
        #dp[i][0] = 1
        #dp[0][j] = 0
        #dp[i][j] = 0 if i < j
        m = len(s)
        n = len(t)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1
        for j in range(1,n+1):
            dp[0][j] = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                elif i < j:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m][n]

=======
Suggestion 4

def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(n+1):
            dp[0][i] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i][j-1] + (dp[i-1][j-1] if t[i-1] == s[j-1] else 0)
        return dp[m][n]

=======
Suggestion 5

def numDistinct(self, s: str, t: str) -> int:
        s_len = len(s)
        t_len = len(t)
        dp = [[0 for i in range(s_len+1)] for j in range(t_len+1)]
        for i in range(s_len+1):
            dp[0][i] = 1
        for i in range(1,t_len+1):
            for j in range(1,s_len+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[t_len][s_len]

=======
Suggestion 6

def numDistinct(self, s: str, t: str) -> int:
        m = len(t)
        n = len(s)
        dp = [[0 for x in range(n+1)] for x in range(m+1)]
        for i in range(n+1):
            dp[0][i] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if t[i-1] != s[j-1]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j-1]
        return dp[-1][-1]

=======
Suggestion 7

def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        if m<n:
            return 0
        dp=[[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            dp[i][0]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[m][n]

=======
Suggestion 8

def numDistinct(self, s: str, t: str) -> int:
        #Dynamic Programming
        #Time: O(m*n)
        #Space: O(m*n)
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
        for i in range(len(s)+1):
            dp[0][i] = 1
        for i in range(1,len(t)+1):
            for j in range(1,len(s)+1):
                if s[j-1]==t[i-1]:
                    dp[i][j] = dp[i-1][j-1]+dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]

=======
Suggestion 9

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
        for i in range(len(s)+1):
            dp[0][i] = 1
        for i in range(1, len(t)+1):
            for j in range(1, len(s)+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]

=======
Suggestion 10

def numDistinct(self, s: str, t: str) -> int:
        # create a table to store results of subproblems
        # table[i][j] will be the number of distinct subsequences of s[0..i-1] that equals t[0..j-1]
        # initialize all values as 0
        table = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

        # fill the entries for the 0th row with 1
        for j in range(len(t) + 1):
            table[0][j] = 0

        # fill the entries for the 0th column with 0
        for i in range(len(s) + 1):
            table[i][0] = 1

        # fill the rest of the table entries in a bottom up manner
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):

                # if the current characters match, then add the result of the previous row and column
                if s[i - 1] == t[j - 1]:
                    table[i][j] = table[i - 1][j - 1] + table[i - 1][j]

                # else the current characters don't match, then copy the result from the previous row
                else:
                    table[i][j] = table[i - 1][j]

        return table[len(s)][len(t)]
