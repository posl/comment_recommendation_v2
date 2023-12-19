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
