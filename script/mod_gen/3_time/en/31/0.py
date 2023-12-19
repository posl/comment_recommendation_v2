def getMaxRepetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    s1 = s1 * n1
    s2 = s2 * n2
    i = 0
    j = 0
    count = 0
    while i < len(s1):
        if s1[i] == s2[j]:
            j += 1
            if j == len(s2):
                j = 0
                count += 1
        i += 1
    return count // n2
print(getMaxRepetitions("acb", 4, "ab", 2))
print(getMaxRepetitions("acb", 1, "acb", 1))
print(getMaxRepetitions("aaa", 3, "aa", 1))
print(getMaxRepetitions("aaa", 3, "aa", 2))
print(getMaxRepetitions("aaa", 3, "aaa", 2))
print(getMaxRepetitions("baba", 11, "baab", 1))
print(getMaxRepetitions("bacaba", 3, "abacab", 1))
print(getMaxRepetitions("bacaba", 3, "abacab", 1000000))
print(getMaxRepetitions("bacaba", 3, "abacab", 10000000))
print(getMaxRepetitions("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
