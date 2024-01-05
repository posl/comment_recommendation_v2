def numDistinct(s: str, t: str) -> int:
    dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    for i in range(len(s)+1):
        dp[i][0] = 1
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]
 
print(numDistinct("rabbbit", "rabbit"))
print(numDistinct("babgbag", "bag"))
print(numDistinct("babgbag", "bag"))
print("The values above should be 3, 5, and 5.")

if __name__ == '__main__':
    s:str = ==========please modify============
    t:str = ==========please modify============
    a = numDistinct(s: str, t: str)
    print(a)