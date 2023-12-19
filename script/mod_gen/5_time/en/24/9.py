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
