def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    
    count = [0] * 26
    count[ord(s[0]) - ord('a')] = 1
    maxLen = 1
    
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25:
            maxLen += 1
        else:
            maxLen = 1
        count[ord(s[i]) - ord('a')] = max(count[ord(s[i]) - ord('a')], maxLen)
    
    return sum(count)

if __name__ == '__main__':
    findSubstringInWraproundString()