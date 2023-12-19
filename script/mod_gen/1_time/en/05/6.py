def uniqueSubstringInWraparoundString(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    res = 0
    dp = [0] * 26
    dp[ord(s[0]) - ord('a')] = 1
    count = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i]) - ord(s[i - 1]) == -25:
            count += 1
        else:
            count = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
    return sum(dp)
print(uniqueSubstringInWraparoundString("zab"))
