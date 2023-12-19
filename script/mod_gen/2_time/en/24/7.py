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

if __name__ == '__main__':
    numDistinct()