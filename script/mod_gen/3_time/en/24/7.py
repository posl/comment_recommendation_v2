def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    m, n = len(s), len(t)
    dp = [[1] * (n + 1) for _ in range(m + 1)]
    for j in range(1, n + 1):
        dp[0][j] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j]
            if s[i - 1] == t[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]
    return dp[m][n]

if __name__ == '__main__':
    numDistinct()