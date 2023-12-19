def getMaxRepetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    s1, s2 = list(s1), list(s2)
    count1, count2 = 0, 0
    idx = 0
    while count1 < n1:
        if s1[idx] == s2[count2]:
            count2 += 1
            if count2 == len(s2):
                count2 = 0
                count1 += 1
        idx += 1
        if idx == len(s1):
            idx = 0
    return count1 // n2
print(getMaxRepetitions('acb', 4, 'ab', 2))
print(getMaxRepetitions('acb', 1, 'acb', 1))
print(getMaxRepetitions('aaa', 3, 'aa', 1))
print(getMaxRepetitions("aaa", 1000000, "a", 1000000))
print(getMaxRepetitions('baba', 11, 'baab', 1))
print(getMaxRepetitions('bacaba', 3, 'abacab', 1))
print(getMaxRepetitions('baba', 11, 'baab', 2))
print(getMaxRepetitions('baba', 11, 'baab', 3))
print(getMaxRepetitions('baba', 11, 'baab', 4))
print(getMaxRepetitions('baba', 11, 'baab', 5))
print(getMaxRepetitions('baba', 11, 'baab', 6))
print(getMaxRepetitions('baba', 11, 'baab', 7))
print(getMaxRepetitions('baba', 11, 'baab', 8))
print(getMaxRepetitions('baba', 11, 'baab', 9))
print(getMaxRepetitions('baba', 11, 'baab', 10))
print(getMaxRepetitions('baba', 11, 'baab', 11))
print(getMaxRepetitions('baba', 11,
