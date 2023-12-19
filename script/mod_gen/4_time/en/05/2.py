def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if len(s) == 0: return 0
    res = 1
    dp = [1] * 26
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i]) - ord(s[i-1]) == -25:
            res += 1
        else:
            res = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], res)
    return sum(dp)
print(findSubstringInWraproundString("zab"))
