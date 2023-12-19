Synthesizing 10/10 solutions

=======
Suggestion 1

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    if len(s) == 0 or len(t) == 0:
        return 0
    dp = [[0 for _ in range(len(t))] for _ in range(len(s))]
    for i in range(len(s)):
        for j in range(i, len(t)):
            if s[i] == t[j]:
                if i == 0:
                    dp[i][j] = 1
                else:
                    for k in range(i):
                        dp[i][j] += dp[k][j-1]
    return dp[-1][-1]

=======
Suggestion 2

def numDistinct(s, t):
    #dp[i][j] = number of distinct subsequences of s[0..i] which equals t[0..j]
    #if s[i] == t[j]: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    #else: dp[i][j] = dp[i-1][j]
    #dp[0][0] = 1
    #dp[0][j] = 0
    #dp[i][0] = 1
    dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    for i in range(len(s)+1):
        dp[i][0] = 1
    for j in range(1, len(t)+1):
        dp[0][j] = 0
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(s)][len(t)]

=======
Suggestion 3

def distinctSubsequences(s,t):
    n = len(s)
    m = len(t)
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1]==t[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][m]

s = "babgbag"
t = "bag"
print(distinctSubsequences(s,t))

=======
Suggestion 4

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    #DP
    #dp[i][j] represents the number of distinct subsequences of s[:i] which equals t[:j]
    #dp[i][j] = dp[i-1][j] if s[i-1] != t[j-1]
    #dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i-1] == t[j-1]
    #dp[0][0] = 1
    #dp[0][j] = 0
    #dp[i][0] = 1
    #Time complexity: O(mn)
    #Space complexity: O(mn)
    m = len(s)
    n = len(t)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = 1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1] != t[j-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    return dp[m][n]

=======
Suggestion 5

def numDistinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    if m < n:
        return 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[m][n]

=======
Suggestion 6

def numDistinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]

print(numDistinct("rabbbit", "rabbit"))
print(numDistinct("babgbag", "bag"))
print(numDistinct("babgbag", "ba"))
print(numDistinct("babgbag", "b"))
print(numDistinct("babgbag", "a"))
print(numDistinct("babgbag", "g"))
print(numDistinct("babgbag", "bab"))
print(numDistinct("babgbag", "babg"))
print(numDistinct("babgbag", "babgb"))
print(numDistinct("babgbag", "babgba"))
print(numDistinct("babgbag", "babgbag"))
print(numDistinct("babgbag", "babgbaga"))
print(numDistinct("babgbag", "babgbagab"))
print(numDistinct("babgbag", "babgbagaba"))
print(numDistinct("babgbag", "babgbagabab"))
print(numDistinct("babgbag", "babgbagababb"))
print(numDistinct("babgbag", "babgbagababba"))
print(numDistinct("babgbag", "babgbagababbab"))
print(numDistinct("babgbag", "babgbagababbabb"))
print(numDistinct("babgbag", "babgbagababbabba"))
print(numDistinct("babgbag", "babgbagababbabbab"))
print(numDistinct("babgbag", "babgbagababbabbabb"))
print(numDistinct("babgbag", "babgbagababbabbabba"))
print(numDistinct("babgbag", "babgbagababbabbabbab"))
print(numDistinct("babgbag",

=======
Suggestion 7

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    #base cases
    if len(t) == 0:
        return 1
    if len(s) == 0:
        return 0

    #create a 2D array
    dp = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]

    #initialization
    for i in range(len(s)):
        dp[i][0] = 1

    #fill the table
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[len(s)][len(t)]

=======
Suggestion 8

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    if len(s) < len(t):
        return 0
    if len(s) == len(t):
        if s == t:
            return 1
        else:
            return 0
    dp = [[0 for i in range(len(t))] for j in range(len(s))]
    dp[0][0] = 1 if s[0] == t[0] else 0
    for i in range(1, len(s)):
        for j in range(len(t)):
            if j > i:
                break
            if i == j:
                if s[i] == t[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i - 1][j]
            elif j == 0:
                if s[i] == t[j]:
                    dp[i][j] = dp[i - 1][j] + 1
                else:
                    dp[i][j] = dp[i - 1][j]
            else:
                if s[i] == t[j]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
    return dp[len(s) - 1][len(t) - 1]

=======
Suggestion 9

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    dp = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
    for i in range(len(dp[0])):
        dp[0][i] = 1
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if t[i-1] == s[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[-1][-1]

print(numDistinct("rabbbit", "rabbit"))
print(numDistinct("babgbag", "bag"))
print(numDistinct("babgbag", "bab"))
print(numDistinct("babgbag", "gb"))
print(numDistinct("babgbag", "g"))
print(numDistinct("babgbag", "a"))
print(numDistinct("babgbag", "b"))
print(numDistinct("babgbag", "bb"))
print(numDistinct("babgbag", "bbb"))
print(numDistinct("babgbag", "bbbb"))
print(numDistinct("babgbag", "bbbbb"))
print(numDistinct("babgbag", "bbbbbb"))
print(numDistinct("babgbag", "bbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbbbbbbbbb

=======
Suggestion 10

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    m = len(s)
    n = len(t)
    if m < n:
        return 0
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for j in range(m+1):
        dp[0][j] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if t[i-1] == s[j-1]:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[n][m]

s = "rabbbit"
t = "rabbit"
print(numDistinct(s, t))
s = "babgbag"
t = "bag"
print(numDistinct(s, t))
