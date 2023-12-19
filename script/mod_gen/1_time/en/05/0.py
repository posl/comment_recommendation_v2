def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if not s:
        return 0
    dp = [0] * 26
    dp[ord(s[0]) - ord('a')] = 1
    count = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i - 1]) == 1 or (s[i] == 'a' and s[i - 1] == 'z'):
            count += 1
        else:
            count = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
    return sum(dp)

if __name__ == '__main__':
    findSubstringInWraproundString()