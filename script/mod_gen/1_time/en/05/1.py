def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    s = list(s)
    s = [ord(i)-97 for i in s]
    s = [i-26 if i>25 else i for i in s]
    count = 1
    maxCount = [0]*26
    maxCount[s[0]] = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]+1 or (s[i] == 0 and s[i-1] == 25):
            count += 1
        else:
            count = 1
        maxCount[s[i]] = max(maxCount[s[i]],count)
    return sum(maxCount)
print(findSubstringInWraproundString("zab"))
