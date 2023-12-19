def findSubstringInWraproundString(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    if len(s) == 2:
        if ord(s[1]) - ord(s[0]) == 1 or ord(s[1]) - ord(s[0]) == -25:
            return 3
        else:
            return 2
    dp = [0] * len(s)
    dp[0] = 1
    if ord(s[1]) - ord(s[0]) == 1 or ord(s[1]) - ord(s[0]) == -25:
        dp[1] = 3
    else:
        dp[1] = 2
    for i in range(2, len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i]) - ord(s[i-1]) == -25:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 1
        if ord(s[i]) - ord(s[i-1]) == 1 and dp[i-1] == 2:
            dp[i] += 1
    return sum(dp)
print(findSubstringInWraproundString("zab"))
