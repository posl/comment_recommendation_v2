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

if __name__ == '__main__':
    numDistinct()