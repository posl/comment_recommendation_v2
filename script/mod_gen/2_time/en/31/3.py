def getMaxRepetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    if len(s1) * n1 < len(s2) * n2:
        return 0
    s1 = s1 * n1
    s2 = s2 * n2
    i = 0
    j = 0
    count = 0
    while i < len(s1):
        if s1[i] == s2[j]:
            j += 1
            if j == len(s2):
                count += 1
                j = 0
        i += 1
    return count // n2

if __name__ == '__main__':
    getMaxRepetitions()