def uniqueSubstringsInWraparoundString(s):
    """
    :type p: str
    :rtype: int
    """
    if not s:
        return 0
    if len(s) == 1:
        return 1
    dp = [0] * len(s)
    dp[0] = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1 or (s[i] == 'a' and s[i-1] == 'z'):
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 1
    return sum(dp)

if __name__ == '__main__':
    uniqueSubstringsInWraparoundString()