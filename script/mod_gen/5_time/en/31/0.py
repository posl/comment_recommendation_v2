def getMaxRepetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    # get the count of s1 in s2
    s1Count = 0
    s2Count = 0
    i = 0
    j = 0
    while i < n1:
        if s1[j] == s2[i]:
            j += 1
            if j == len(s1):
                s1Count += 1
                j = 0
        i += 1
    i = 0
    j = 0
    while i < n2:
        if s2[j] == s1[i]:
            j += 1
            if j == len(s2):
                s2Count += 1
                j = 0
        i += 1
    return s1Count // s2Count

if __name__ == '__main__':
    getMaxRepetitions()