def uniqueSubstringsInWraparoundString(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) <= 1:
        return len(s)
    dp = [0] * 26
    dp[ord(s[0]) - ord('a')] = 1
    count = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i - 1]) == 1 or (ord(s[i]) - ord(s[i - 1]) == -25 and s[i] == 'a'):
            count += 1
        else:
            count = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
    return sum(dp)
s = "zab"
print(uniqueSubstringsInWraparoundString(s))
