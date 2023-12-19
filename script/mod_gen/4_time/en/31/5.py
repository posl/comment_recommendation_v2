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
    s1s = s1 * n1
    s2s = s2 * n2
    s1slen = len(s1s)
    s2slen = len(s2s)
    i = 0
    j = 0
    ans = 0
    while i < s1slen:
        if s1s[i] == s2s[j]:
            j += 1
            if j == s2slen:
                ans += 1
                j = 0
        i += 1
    return ans // n2
print(getMaxRepetitions("acb", 4, "ab", 2))
print(getMaxRepetitions("acb", 1, "acb", 1))
print(getMaxRepetitions("aaa", 3, "aa", 1))
print(getMaxRepetitions("aaa", 3, "aa", 2))
print(getMaxRepetitions("aaa", 3, "aaa", 2))
print(getMaxRepetitions("aaa", 3, "aaa", 3))
print(getMaxRepetitions("aaa", 3, "aaa", 4))
print(getMaxRepetitions("aaa", 3, "aaa", 5))
print(getMaxRepetitions("aaa", 3, "aaa", 6))
print(getMaxRepetitions("aaa", 3, "aaa", 7))
print(getMaxRepetitions("aaa", 3, "aaa", 8))
print(getMaxRepetitions("aaa", 3, "aaa", 9))
print(getMaxRepetitions("aaa", 3, "aaa", 10))
print(getMaxRepetitions("aaa", 3, "aaa", 11))
print(getMaxRepetitions("aaa", 3, "aaa", 12))
print(getMaxRepetitions("aaa", 3, "aaa", 13))
print(getMaxRepetitions("aaa", 3
