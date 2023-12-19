def getMaxRepetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    #s1 = [s1, n1]
    #s2 = [s2, n2]
    #s1 = s1[0]*s1[1]
    #s2 = s2[0]*s2[1]
    #print(s1)
    #print(s2)
    #s2 = list(s2)
    #print(s2)
    #count = 0
    #while s2 != []:
    #    for i in s1:
    #        if i == s2[0]:
    #            s2.pop(0)
    #        if s2 == []:
    #            count += 1
    #            break
    #return count
    s1 = [s1, n1]
    s2 = [s2, n2]
    s1 = s1[0]*s1[1]
    s2 = s2[0]*s2[1]
    print(s1)
    print(s2)
    s2 = list(s2)
    print(s2)
    count = 0
    while s2 != []:
        for i in s1:
            if i == s2[0]:
                s2.pop(0)
            if s2 == []:
                count += 1
                break
    return count
print(getMaxRepetitions(s1 = "acb", n1 = 4, s2 = "ab", n2 = 2))
print(getMaxRepetitions(s1 = "acb", n1 = 1, s2 = "acb", n2 = 1))
print(getMaxRepetitions(s1 = "aaa", n1 = 3, s2 = "aa", n2 = 1))
