def findSubstringInWraproundString(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    if n <= 1:
        return n
    res = [0]*26
    res[ord(s[0])-ord('a')] = 1
    count = 1
    for i in range(1, n):
        if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i]) - ord(s[i-1]) == -25:
            count += 1
        else:
            count = 1
        res[ord(s[i])-ord('a')] = max(res[ord(s[i])-ord('a')], count)
    return sum(res)
    
print(findSubstringInWraproundString("zab"))
