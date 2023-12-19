def findSubstringInWraproundString(s: str) -> int:
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    d = dict()
    d[s[0]] = 1
    curr = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i]) - ord(s[i-1]) == -25:
            curr += 1
        else:
            curr = 1
        d[s[i]] = max(d.get(s[i], 0), curr)
    return sum(d.values())
print(findSubstringInWraproundString("zab"))
print(findSubstringInWraproundString("cac"))
print(findSubstringInWraproundString("a"))
print(findSubstringInWraproundString("zabaz"))
print(findSubstringInWraproundString("zaba"))
