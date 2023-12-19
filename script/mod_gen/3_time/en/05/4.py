def uniqueSubstringsInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    dp = [0] * 26
    dp[ord(s[0]) - ord('a')] = 1
    currentMax = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1 or (ord(s[i]) - ord(s[i-1]) == -25 and s[i] != 'a'):
            currentMax += 1
        else:
            currentMax = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], currentMax)
    return sum(dp)
print(uniqueSubstringsInWraproundString("zab"))
print(uniqueSubstringsInWraproundString("cac"))
print(uniqueSubstringsInWraproundString("a"))
print(uniqueSubstringsInWraproundString("zababc"))
print(uniqueSubstringsInWraproundString("zababca"))
print(uniqueSubstringsInWraproundString("zababcab"))
print(uniqueSubstringsInWraproundString("zababcabc"))
print(uniqueSubstringsInWraproundString("zababcabca"))
print(uniqueSubstringsInWraproundString("zababcabcab"))
print(uniqueSubstringsInWraproundString("zababcabcabc"))
print(uniqueSubstringsInWraproundString("zababcabcabca"))
print(uniqueSubstringsInWraproundString("zababcabcabcab"))
print(uniqueSubstringsInWraproundString("zababcabcabcabc"))
print(uniqueSubstringsInWraproundString("zababcabcabcabca"))
print(uniqueSubstringsInWraproundString("zababcabcabcabcab"))
print(uniqueSubstringsInWraproundString("zababcabcabcabcabc"))
print(uniqueSubstringsInWraproundString("zababcabcabcabcabca"))
print(uniqueSubstringsInWraproundString("zababcabcabcabcabcab"))
print(uniqueSubstringsInWraproundString("zababcabcabcabcabcabc"))
print(uniqueSubstringsInWraproundString("zababcabcabcabcabcabca"))
print(uniqueSubstringsInWraproundString("zababcabcabcabcabcabcab
