def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    dp = [[0]*(len(s)+1) for _ in range(len(t)+1)]
    for j in range(len(s)+1):
        dp[0][j] = 1
    for i in range(1, len(t)+1):
        for j in range(1, len(s)+1):
            if t[i-1] == s[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[-1][-1]
print(numDistinct("rabbbit", "rabbit"))
print(numDistinct("babgbag", "bag"))
print(numDistinct("babgbag", "bagb"))
print(numDistinct("babgbag", "bagbb"))
print(numDistinct("babgbag", "bagbbb"))
print(numDistinct("babgbag", "bagbbbb"))
print(numDistinct("babgbag", "bagbbbbb"))
print(numDistinct("babgbag", "bagbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag", "bagbbbbbbbbbbbbbbbbbbbbbb"))
print(numDistinct("bab
