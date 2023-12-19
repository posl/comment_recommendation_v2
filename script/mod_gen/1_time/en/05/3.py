def uniqueSubstringsInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    substrings = set()
    substrings.add(s[0])
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i]) - ord(s[i - 1]) == -25:
            substrings.add(s[i])
            substrings.add(s[i - 1] + s[i])
        else:
            substrings.add(s[i])
    return len(substrings)
print(uniqueSubstringsInWraproundString("zab"))
