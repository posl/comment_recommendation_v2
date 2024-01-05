def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    # dp[i][j] is the number of distinct subsequences of s[:i] which equals t[:j]
    # dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i-1] == t[j-1]
    # dp[i][j] = dp[i-1][j] if s[i-1] != t[j-1]
    # dp[0][j] = 0 for all j
    # dp[i][0] = 1 for all i
    # return dp[-1][-1]
    # dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    # for i in range(len(s)+1):
    #     dp[i][0] = 1
    # for i in range(1, len(s)+1):
    #     for j in range(1, len(t)+1):
    #         if s[i-1] == t[j-1]:
    #             dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    #         else:
    #             dp[i][j] = dp[i-1][j]
    # return dp[-1][-1]
    dp = [0 for _ in range(len(t)+1)]
    dp[0] = 1
    for i in range(1, len(s)+1):
        for j in range(len(t), 0, -1):
            if s[i-1] == t[j-1]:
                dp[j] = dp[j-1] + dp[j]
    return dp[-1]
print(numDistinct("rabbbit", "rabbit"))
print(numDistinct("babgbag", "bag"))
print(numDistinct("babgbag", "bag"))
print(num

if __name__ == '__main__':
    s = int(input())
    t = int(input())
    a = numDistinct(s, t)
    print(a)