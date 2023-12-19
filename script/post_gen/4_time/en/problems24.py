Synthesizing 10/10 solutions

=======
Suggestion 1

def numDistinct(s: str, t: str) -> int:
    if len(s) < len(t):
        return 0
    if s == t:
        return 1
    if len(t) == 0:
        return 1
    if len(s) == 1:
        if s == t:
            return 1
        else:
            return 0
    if s[0] == t[0]:
        return numDistinct(s[1:], t[1:]) + numDistinct(s[1:], t)
    else:
        return numDistinct(s[1:], t)

=======
Suggestion 2

def numDistinct(s,t):
    dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    for i in range(len(s)+1):
        dp[i][0] = 1
    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]
s = "rabbbit"
t = "rabbit"
print(numDistinct(s,t))
s = "babgbag"
t = "bag"
print(numDistinct(s,t))

=======
Suggestion 3

def numDistinct(s, t):
    if len(s) < len(t):
        return 0

    dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]

    for i in range(len(s) + 1):
        dp[0][i] = 1

    for i in range(1, len(t) + 1):
        for j in range(1, len(s) + 1):
            if s[j - 1] == t[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]

    return dp[len(t)][len(s)]

s = "rabbbit"
t = "rabbit"
print(numDistinct(s, t))

s = "babgbag"
t = "bag"
print(numDistinct(s, t))

s = "babgbag"
t = "bag"
print(numDistinct(s, t))

=======
Suggestion 4

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    if len(s) < len(t):
        return 0
    dp = [[0 for _ in range(len(s))] for _ in range(len(t))]
    for i in range(len(t)):
        for j in range(i, len(s)):
            if i == j:
                dp[i][j] = 1 if s[j] == t[i] else 0
            else:
                if s[j] == t[i]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
    return dp[-1][-1]

=======
Suggestion 5

def distinctSubsequences(s, t):
    m = len(s)
    n = len(t)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = 1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[m][n]

s = "rabbbit"
t = "rabbit"
print(distinctSubsequences(s,t))
s = "babgbag"
t = "bag"
print(distinctSubsequences(s,t))

=======
Suggestion 6

def numDistinct(s,t):
    m = len(s)
    n = len(t)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = 1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1]==t[j-1]:
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[m][n]

s = "rabbbit"
t = "rabbit"
print(numDistinct(s,t))

=======
Suggestion 7

def numDistinct(s,t):
    m = len(s)
    n = len(t)
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        dp[i][0] = 1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[m][n]

s = "rabbbit"
t = "rabbit"
print(numDistinct(s,t))

=======
Suggestion 8

def numDistinct(s, t):
    if not s or not t:
        return 0
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[m][n]

s = "rabbbit"
t = "rabbit"
print(numDistinct(s, t))

s = "babgbag"
t = "bag"
print(numDistinct(s, t))

=======
Suggestion 9

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    dp = [[0]*(len(s)+1) for _ in range(len(t)+1)]
    for j in range(len(s)+1):
        dp[0][j] = 1
    for i in range(1, len(t)+1):
        for j in range(1, len(s)+1):
            if t[i-1] == s[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[-1][-1]

print(numDistinct("rabbbit", "rabbit"))
print(numDistinct("babgbag", "bag"))
print(numDistinct("babgbag", "bagb"))
print(numDistinct("babgbag", "bagbb"))
print(numDistinct("babgbag", "bagbbb"))
print(numDistinct("babgbag", "bagbbbb"))
print(numDistinct("babgbag", "bagbbbbb"))
print(numDistinct("babgbag", "bagbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbbbbbbbbbbbb"))
print(numDistinct("bab

=======
Suggestion 10

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    dp = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
    for i in range(len(s) + 1):
        dp[i][0] = 1
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]

s = "rabbbit"
t = "rabbit"
print(numDistinct(s, t))
