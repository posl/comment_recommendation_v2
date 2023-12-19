def getMaxRepetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    #s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
    #s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
    if s1 == s2:
        return n1
    if len(s1) * n1 < len(s2) * n2:
        return 0
    if len(s1) * n1 == len(s2) * n2:
        return 1
    if len(s1) * n1 > len(s2) * n2:
        # find the first char of s2 in s1
        # find the first char of s2 in s1
        # find the first char of s2 in s1
        # find the

if __name__ == '__main__':
    getMaxRepetitions()