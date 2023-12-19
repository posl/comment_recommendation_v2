def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    if len(s) < len(t):
        return 0
    if len(s) == len(t):
        if s == t:
            return 1
        else:
            return 0
    dp = [[0 for i in range(len(t))] for j in range(len(s))]
    dp[0][0] = 1 if s[0] == t[0] else 0
    for i in range(1, len(s)):
        for j in range(len(t)):
            if j > i:
                break
            if i == j:
                if s[i] == t[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i - 1][j]
            elif j == 0:
                if s[i] == t[j]:
                    dp[i][j] = dp[i - 1][j] + 1
                else:
                    dp[i][j] = dp[i - 1][j]
            else:
                if s[i] == t[j]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
    return dp[len(s) - 1][len(t) - 1]

if __name__ == '__main__':
    numDistinct()