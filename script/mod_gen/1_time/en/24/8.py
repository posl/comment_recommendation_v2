def numDistinct(s: str, t: str) -> int:
    if len(s) == 0 or len(t) == 0:
        return 0
    if len(s) < len(t):
        return 0
    if len(s) == len(t):
        if s == t:
            return 1
        else:
            return 0
    dp = [[0 for _ in range(len(s))] for _ in range(len(t))]
    for i in range(len(t)):
        for j in range(len(s)):
            if t[i] == s[j]:
                if i == 0:
                    if j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i][j - 1] + 1
                else:
                    if j == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
            else:
                if j == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j - 1]
    return dp[len(t) - 1][len(s) - 1]
s = "rabbbit"
t = "rabbit"
print(numDistinct(s, t))
s = "babgbag"
t = "bag"
print(numDistinct(s, t))
s = "babgbag"
t = "bag"
print(numDistinct(s, t))
s

if __name__ == '__main__':
    s:str = ==========please modify============
    t:str = ==========please modify============
    a = numDistinct(s: str, t: str)
    print(a)