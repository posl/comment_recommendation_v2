def numDistinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]
print(numDistinct("rabbbit", "rabbit"))
print(numDistinct("babgbag", "bag"))
print(numDistinct("babgbag", "ba"))
print(numDistinct("babgbag", "b"))
print(numDistinct("babgbag", "a"))
print(numDistinct("babgbag", "g"))
print(numDistinct("babgbag", "bab"))
print(numDistinct("babgbag", "babg"))
print(numDistinct("babgbag", "babgb"))
print(numDistinct("babgbag", "babgba"))
print(numDistinct("babgbag", "babgbag"))
print(numDistinct("babgbag", "babgbaga"))
print(numDistinct("babgbag", "babgbagab"))
print(numDistinct("babgbag", "babgbagaba"))
print(numDistinct("babgbag", "babgbagabab"))
print(numDistinct("babgbag", "babgbagababb"))
print(numDistinct("babgbag", "babgbagababba"))
print(numDistinct("babgbag", "babgbagababbab"))
print(numDistinct("babgbag", "babgbagababbabb"))
print(numDistinct("babgbag", "babgbagababbabba"))
print(numDistinct("babgbag", "babgbagababbabbab"))
print(numDistinct("babgbag", "babgbagababbabbabb"))
print(numDistinct("babgbag", "babgbagababbabbabba"))
print(numDistinct("babgbag", "babgbagababbabbabbab"))
print(numDistinct("babgbag",
