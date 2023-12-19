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

if __name__ == '__main__':
    numDistinct()