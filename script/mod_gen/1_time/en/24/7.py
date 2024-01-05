def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    #if s == t:
    #    return 1
    #if len(s) < len(t):
    #    return 0
    #if len(t) == 0:
    #    return 1
    #if len(s) == 0:
    #    return 0
    #if s[0] == t[0]:
    #    return numDistinct(s[1:], t[1:]) + numDistinct(s[1:], t)
    #else:
    #    return numDistinct(s[1:], t)
    #dp = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
    #for i in range(len(s)+1):
    #    dp[0][i] = 1
    #for i in range(1, len(t)+1):
    #    for j in range(1, len(s)+1):
    #        if t[i-1] == s[j-1]:
    #            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    #        else:
    #            dp[i][j] = dp[i][j-1]
    #return dp[-1][-1]
    dp = [0 for _ in range(len(t)+1)]
    dp[0] = 1
    for i in range(1, len(s)+1):
        for j in range(len(t), 0, -1):
            if s[i-1] == t[j-1]:
                dp[j] += dp[j-1]
    return dp[-1]

if __name__ == '__main__':
    s = int(input())
    t = int(input())
    a = numDistinct(s, t)
    print(a)