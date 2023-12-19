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

if __name__ == '__main__':
    numDistinct()