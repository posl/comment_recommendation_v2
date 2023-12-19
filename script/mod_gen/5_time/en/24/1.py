def numDistinct(s, t):
    #dp[i][j] = number of distinct subsequences of s[0..i] which equals t[0..j]
    #if s[i] == t[j]: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    #else: dp[i][j] = dp[i-1][j]
    #dp[0][0] = 1
    #dp[0][j] = 0
    #dp[i][0] = 1
    dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    for i in range(len(s)+1):
        dp[i][0] = 1
    for j in range(1, len(t)+1):
        dp[0][j] = 0
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(s)][len(t)]

if __name__ == '__main__':
    numDistinct()