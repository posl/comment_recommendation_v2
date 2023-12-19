def numDistinct(s, t):
    m = len(s)
    n = len(t)
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[m][n]
print(numDistinct("rabbbit", "rabbit"))
print(numDistinct("babgbag", "bag"))
print(numDistinct("babgbag", "bagg"))
print(numDistinct("babgbag", "babg"))
print(numDistinct("babgbag", "bbg"))
print(numDistinct("babgbag", "bb"))
print(numDistinct("babgbag", "b"))
print(numDistinct("babgbag", "a"))
print(numDistinct("babgbag", "bbbbb"))
print(numDistinct("babgbag", "bbbb"))
print(numDistinct("babgbag", "bbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbb
