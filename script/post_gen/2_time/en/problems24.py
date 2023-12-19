Synthesizing 10/10 solutions

=======
Suggestion 1

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    #Recursion
    # if not t:
    #     return 1
    # if not s:
    #     return 0
    # if s[0] == t[0]:
    #     return numDistinct(s[1:], t[1:]) + numDistinct(s[1:], t)
    # else:
    #     return numDistinct(s[1:], t)

    #DP
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

=======
Suggestion 2

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    if len(s) < len(t):
        return 0
    if len(t) == 0:
        return 1
    dp = [[0 for _ in range(len(t))] for _ in range(len(s))]
    dp[0][0] = 1 if s[0] == t[0] else 0
    for i in range(1, len(s)):
        if s[i] == t[0]:
            dp[i][0] = dp[i-1][0] + 1
        else:
            dp[i][0] = dp[i-1][0]
    for i in range(1, len(s)):
        for j in range(1, len(t)):
            if s[i] == t[j]:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(s)-1][len(t)-1]

print(numDistinct("rabbbit", "rabbit"))
print(numDistinct("babgbag", "bag"))

=======
Suggestion 3

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    if len(s) < len(t):
        return 0
    dp = [[0 for _ in range(len(s))] for _ in range(len(t))]
    dp[0][0] = 1 if s[0] == t[0] else 0
    for i in range(1, len(s)):
        if s[i] == t[0]:
            dp[0][i] = dp[0][i-1] + 1
        else:
            dp[0][i] = dp[0][i-1]
    for i in range(1, len(t)):
        for j in range(i, len(s)):
            if s[j] == t[i]:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[len(t)-1][len(s)-1]

=======
Suggestion 4

def numDistinct(s, t):
    m = len(s)
    n = len(t)
    if m < n:
        return 0
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = 1
    for i in range(1, m+1):
        for j in range(1, min(i, n)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[m][n]

s = "rabbbit"
t = "rabbit"
print(numDistinct(s, t))

s = "babgbag"
t = "bag"
print(numDistinct(s, t))

=======
Suggestion 5

def numDistinct(s, t):
    # if the length of s is less than the length of t, there is no way to make t from s
    if len(s) < len(t):
        return 0
    # if the length of s is the same as the length of t
    if len(s) == len(t):
        # if s and t are the same, there is one way to make t from s
        if s == t:
            return 1
        # if s and t are not the same, there is no way to make t from s
        else:
            return 0
    # if the length of s is greater than the length of t
    if len(s) > len(t):
        # if t is empty, there is one way to make t from s
        if t == "":
            return 1
        # if t is not empty
        else:
            # if the first character of s is the same as the first character of t
            if s[0] == t[0]:
                # there are two ways to make t from s:
                # 1. by keeping the first character of s and removing the first character of t
                # 2. by removing the first character of s and keeping t
                return numDistinct(s[1:], t[1:]) + numDistinct(s[1:], t)
            # if the first character of s is not the same as the first character of t
            else:
                # there is one way to make t from s:
                # by removing the first character of s and keeping t
                return numDistinct(s[1:], t)

=======
Suggestion 6

def distinctSubseqII(s):
    """
    :type s: str
    :rtype: int
    """
    mod = 10**9 + 7
    dp = [1] * (len(s) + 1)
    last = {}
    for i, c in enumerate(s):
        dp[i + 1] = dp[i] * 2 % mod
        if c in last:
            dp[i + 1] -= dp[last[c]]
        last[c] = i
    return (dp[-1] - 1) % mod

print(distinctSubseqII("rabbbit"))
print(distinctSubseqII("babgbag"))
print(distinctSubseqII("ab"))
print(distinctSubseqII("abc"))
print(distinctSubseqII("aba"))
print(distinctSubseqII("aaa"))
print(distinctSubseqII("aaaa"))
print(distinctSubseqII("aaaaa"))
print(distinctSubseqII("aaaaaa"))
print(distinctSubseqII("aaaaaaa"))
print(distinctSubseqII("aaaaaaaa"))
print(distinctSubseqII("aaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(distinct

=======
Suggestion 7

def numDistinct(s, t):
    dp = [[0 for i in range(len(s) + 1)] for j in range(len(t) + 1)]
    for i in range(len(s) + 1):
        dp[0][i] = 1
    for i in range(1, len(t) + 1):
        for j in range(1, len(s) + 1):
            if t[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]
    return dp[-1][-1]

s = "rabbbit"
t = "rabbit"
print(numDistinct(s, t))

=======
Suggestion 8

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    if not s or not t:
        return 0

    n = len(s)
    m = len(t)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for j in range(n+1):
        dp[0][j] = 1

    for i in range(1, m+1):
        for j in range(1, n+1):
            if t[i-1] == s[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1]

    return dp[-1][-1]

=======
Suggestion 9

def numDistinct(s: str, t: str) -> int:
    return 0

=======
Suggestion 10

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    dp = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]
    for i in range(len(s)+1):
        dp[0][i] = 1
    for i in range(1, len(t)+1):
        for j in range(1, len(s)+1):
            if t[i-1] == s[j-1]:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[-1][-1]
