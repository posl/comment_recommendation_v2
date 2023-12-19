def findSubstringInWraproundString(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    prev = s[0]
    curr = 1
    count = 0
    for i in range(1, len(s)):
        if ord(s[i]) - ord(prev) == 1 or (s[i] == "a" and prev == "z"):
            curr += 1
        else:
            curr = 1
        count += curr
        prev = s[i]
    return count
print(findSubstringInWraproundString("a"))
print(findSubstringInWraproundString("cac"))
print(findSubstringInWraproundString("zab"))
print(findSubstringInWraproundString("zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd"))
