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
    count = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i]) - ord(s[i - 1]) == -25:
            count += 1
        else:
            count = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
    return sum(dp)
print(findSubstringInWraproundString("zab"))
print(findSubstringInWraproundString("cac"))
print(findSubstringInWraproundString("a"))
print(findSubstringInWraproundString("zaba"))
print(findSubstringInWraproundString("zabca"))
print(findSubstringInWraproundString("zabcad"))
print(findSubstringInWraproundString("zabcade"))
print(findSubstringInWraproundString("zabcadef"))
print(findSubstringInWraproundString("zabcadefg"))
print(findSubstringInWraproundString("zabcadefgh"))
print(findSubstringInWraproundString("zabcadefghi"))
print(findSubstringInWraproundString("zabcadefghij"))
print(findSubstringInWraproundString("zabcadefghijk"))
print(findSubstringInWraproundString("zabcadefghijkl"))
print(findSubstringInWraproundString("zabcadefghijklm"))
print(findSubstringInWraproundString("zabcadefghijklmn"))
print(findSubstringInWraproundString("zabcadefghijklmno"))
print(findSubstringInWraproundString("zabcadefghijklmnop"))
print(findSubstringInWraproundString("zabcadefghijklmnopq"))
print(findSubstringInWraproundString("zabcadefghijklmnopqr"))
print(findSubstringInWraproundString("zabcadefghijklmnopqrs"))
print(findSubstringInWraproundString("zabcadefghijklmnopqrst"))
print(findSubstringInWraproundString("zabcadefgh
