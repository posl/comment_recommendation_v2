def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if not s:
        return 0
    substr = set()
    i = 0
    while i < len(s):
        j = i + 1
        while j < len(s) and (ord(s[j]) - ord(s[j-1]) == 1 or ord(s[j-1]) - ord(s[j]) == 25):
            j += 1
        for k in range(i, j):
            for l in range(k, j):
                substr.add(s[k:l+1])
        i = j
    return len(substr)

if __name__ == '__main__':
    findSubstringInWraproundString()