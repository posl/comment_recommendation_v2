def getMaxRepetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    if not set(s2).issubset(set(s1)):
        return 0
    # s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
    # s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
    # s1 = "aaa", n1 = 3, s2 = "aa", n2 = 1
    s1 = s1*n1
    s2 = s2*n2
    i = 0
    j = 0
    count = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            j += 1
        i += 1
        if j == len(s2):
            j = 0
            count += 1
    return count
s1 = "acb"
n1 = 4
s2 = "ab"
n2 = 2
print(getMaxRepetitions(s1, n1, s2, n2))
s1 = "acb"
n1 = 1
s2 = "acb"
n2 = 1
print(getMaxRepetitions(s1, n1, s2, n2))
s1 = "aaa"
n1 = 3
s2 = "aa"
n2 = 1
print(getMaxRepetitions(s1, n1, s2, n2))
