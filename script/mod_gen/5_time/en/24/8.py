def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    dp = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
    for i in range(len(dp[0])):
        dp[0][i] = 1
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if t[i-1] == s[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[-1][-1]
print(numDistinct("rabbbit", "rabbit"))
print(numDistinct("babgbag", "bag"))
print(numDistinct("babgbag", "bab"))
print(numDistinct("babgbag", "gb"))
print(numDistinct("babgbag", "g"))
print(numDistinct("babgbag", "a"))
print(numDistinct("babgbag", "b"))
print(numDistinct("babgbag", "bb"))
print(numDistinct("babgbag", "bbb"))
print(numDistinct("babgbag", "bbbb"))
print(numDistinct("babgbag", "bbbbb"))
print(numDistinct("babgbag", "bbbbbb"))
print(numDistinct("babgbag", "bbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbbbbbbbbbbbb
