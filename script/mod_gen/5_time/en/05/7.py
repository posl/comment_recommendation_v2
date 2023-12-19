def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    d = {}
    i = 0
    while i < len(s):
        j = i + 1
        while j < len(s) and (ord(s[j]) - ord(s[j - 1]) == 1 or ord(s[j]) - ord(s[j - 1]) == -25):
            j += 1
        for k in range(i, j):
            if s[k] not in d:
                d[s[k]] = j - k
            else:
                d[s[k]] = max(d[s[k]], j - k)
        i = j
    return sum(d.values())
print(findSubstringInWraproundString("zab"))
