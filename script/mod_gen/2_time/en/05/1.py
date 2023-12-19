def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if not s:
        return 0
    if len(s) == 1:
        return 1
    dp = [0] * 26
    dp[ord(s[0]) - ord('a')] = 1
    cur_len = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i - 1]) == 1 or (s[i] == 'a' and s[i - 1] == 'z'):
            cur_len += 1
        else:
            cur_len = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], cur_len)
    return sum(dp)
print(findSubstringInWraproundString("zab"))
print(findSubstringInWraproundString("cac"))
print(findSubstringInWraproundString("a"))
print(findSubstringInWraproundString("zaba"))
print(findSubstringInWraproundString("zabaz"))
print(findSubstringInWraproundString("zabazab"))
print(findSubstringInWraproundString("zabazaba"))
print(findSubstringInWraproundString("zabazabaz"))
print(findSubstringInWraproundString("zabazabaza"))
print(findSubstringInWraproundString("zabazabazab"))
print(findSubstringInWraproundString("zabazabazaba"))
print(findSubstringInWraproundString("zabazabazabaz"))
print(findSubstringInWraproundString("zabazabazabaza"))
print(findSubstringInWraproundString("zabazabazabazab"))
print(findSubstringInWraproundString("zabazabazabazaba"))
print(findSubstringInWraproundString("zabazabazabazabaz"))
print(findSubstringInWraproundString("zabazabazabazabaza"))
print(findSubstringInWraproundString("zabazabazabazabazab"))
print(findSubstringInWraproundString("zabazabazabazabazaba"))
print(findSubstringInWraproundString("zabazabazabazabazabaz"))
print(findSubstringInWraproundString("zabazabazabazabazabaza"))
