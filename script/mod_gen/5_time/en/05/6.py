def uniqueSubstringsInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if not s:
        return 0
    s = list(s)
    count = 0
    s[0] = ord(s[0]) - ord('a')
    for i in range(1,len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1 or (s[i] == 'a' and s[i-1] == 'z'):
            s[i] = s[i-1] + 1
        else:
            s[i] = ord(s[i]) - ord('a')
    temp = [0]*26
    for i in range(len(s)):
        if temp[s[i]] == 0:
            temp[s[i]] = 1
            count += 1
        for j in range(i+1,len(s)):
            if s[j] - s[j-1] == 1 or (s[j] == 0 and s[j-1] == 25):
                if temp[s[j]] == 0:
                    temp[s[j]] = 1
                    count += 1
            else:
                break
    return count
print(uniqueSubstringsInWraproundString("zaba"))
print(uniqueSubstringsInWraproundString("zab"))
print(uniqueSubstringsInWraproundString("cac"))
print(uniqueSubstringsInWraproundString("a"))
print(uniqueSubstringsInWraproundString("z"))
