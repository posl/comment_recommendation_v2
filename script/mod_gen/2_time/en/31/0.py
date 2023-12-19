def getMaxRepetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    i = j = 0
    count = 0
    while i < n1 * len(s1):
        if s1[i % len(s1)] == s2[j]:
            j += 1
            if j == len(s2):
                j = 0
                count += 1
        i += 1
    return count / n2
print(getMaxRepetitions("acb", 4, "ab", 2))
print(getMaxRepetitions("acb", 1, "acb", 1))
print(getMaxRepetitions("aaa", 3, "aa", 1))
print(getMaxRepetitions("baba", 11, "baab", 1))
print(getMaxRepetitions("aaa", 1000000, "a", 1))
print(getMaxRepetitions("a", 1000000, "a", 1))
print(getMaxRepetitions("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
