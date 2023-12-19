def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    #base cases
    if len(t) == 0:
        return 1
    if len(s) == 0:
        return 0
    #create a 2D array
    dp = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]
    #initialization
    for i in range(len(s)):
        dp[i][0] = 1
    #fill the table
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(s)][len(t)]

if __name__ == '__main__':
    numDistinct()