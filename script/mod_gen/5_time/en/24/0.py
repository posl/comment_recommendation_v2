def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    if len(s) == 0 or len(t) == 0:
        return 0
    dp = [[0 for _ in range(len(t))] for _ in range(len(s))]
    for i in range(len(s)):
        for j in range(i, len(t)):
            if s[i] == t[j]:
                if i == 0:
                    dp[i][j] = 1
                else:
                    for k in range(i):
                        dp[i][j] += dp[k][j-1]
    return dp[-1][-1]

if __name__ == '__main__':
    numDistinct()