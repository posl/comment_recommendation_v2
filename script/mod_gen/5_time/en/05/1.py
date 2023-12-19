def uniqueSubstringsInWraparoundString(s):
    """
    :type p: str
    :rtype: int
    """
    if not s:
        return 0
    count = 0
    length = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i - 1]) == 1 or (s[i] == 'a' and s[i - 1] == 'z'):
            length += 1
        else:
            count += length * (length + 1) // 2
            length = 1
    count += length * (length + 1) // 2
    return count
print(uniqueSubstringsInWraparoundString("zab"))
