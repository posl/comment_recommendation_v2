def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    dp = [[0 for j in range(len(s)+1)] for i in range(len(t)+1)]
    for i in range(len(s)+1):
        dp[0][i] = 1
    for i in range(1,len(t)+1):
        for j in range(1,len(s)+1):
            if t[i-1] == s[j-1]:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[-1][-1]
print(numDistinct("rabbbit", "rabbit"))
print(numDistinct("babgbag", "bag"))
print(numDistinct("babgbag", "bag"))
print("The values above should be 3, 5, and 5.")

if __name__ == '__main__':
    numDistinct()