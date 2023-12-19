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
