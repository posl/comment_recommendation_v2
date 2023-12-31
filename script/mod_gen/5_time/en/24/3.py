def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    #DP
    #dp[i][j] represents the number of distinct subsequences of s[:i] which equals t[:j]
    #dp[i][j] = dp[i-1][j] if s[i-1] != t[j-1]
    #dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i-1] == t[j-1]
    #dp[0][0] = 1
    #dp[0][j] = 0
    #dp[i][0] = 1
    #Time complexity: O(mn)
    #Space complexity: O(mn)
    m = len(s)
    n = len(t)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = 1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1] != t[j-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    return dp[m][n]

if __name__ == '__main__':
    numDistinct()