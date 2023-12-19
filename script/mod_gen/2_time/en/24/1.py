def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    if len(s) < len(t):
        return 0
    if len(t) == 0:
        return 1
    dp = [[0 for _ in range(len(t))] for _ in range(len(s))]
    dp[0][0] = 1 if s[0] == t[0] else 0
    for i in range(1, len(s)):
        if s[i] == t[0]:
            dp[i][0] = dp[i-1][0] + 1
        else:
            dp[i][0] = dp[i-1][0]
    for i in range(1, len(s)):
        for j in range(1, len(t)):
            if s[i] == t[j]:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(s)-1][len(t)-1]
print(numDistinct("rabbbit", "rabbit"))
print(numDistinct("babgbag", "bag"))
