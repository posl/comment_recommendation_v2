def getMaxRepetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    if s1 == s2:
        return n1 // n2
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
print(getMaxRepetitions("acb", 4, "ab", 2))
print(getMaxRepetitions("acb", 1, "acb", 1))
print(getMaxRepetitions("aaa", 3, "aa", 1))
print(getMaxRepetitions("aaa", 3, "aa", 2))
print(getMaxRepetitions("aaa", 3, "aaa", 2))
print(getMaxRepetitions("lovelive", 1, "lovelive", 2))
print(getMaxRepetitions("lovelive", 2, "lovelive", 1))
print(getMaxRepetitions("lovelive", 2, "lovelive", 2))
print(getMaxRepetitions("lovelive", 3, "lovelive", 2))
print(getMaxRepetitions("lovelive", 4, "lovelive", 2))
print(getMaxRepetitions("lovelive", 5, "lovelive", 2))
print(getMaxRepetitions("lovelive", 6, "lovelive", 2))
print(getMaxRepetitions("lovelive", 7, "lovelive", 2))
print(getMaxRepetitions("lovelive", 8, "lovelive", 2))
print(getMaxRepetitions("lovelive", 9, "lovelive",
