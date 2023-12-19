def getMaxRepetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    if n1 == 0:
        return 0
    # idx2 is the index of s2
    # count1 is the number of s1
    # count2 is the number of s2
    idx2, count1, count2 = 0, 0, 0
    # record the count of s1 and s2
    record = []
    while count1 < n1:
        for i in range(len(s1)):
            if s1[i] == s2[idx2]:
                idx2 += 1
            if idx2 == len(s2):
                idx2 = 0
                count2 += 1
        count1 += 1
        if idx2 == 0:
            break
    # if s2 is not a substring of s1
    if count2 == 0:
        return 0
    # find the count of s1 and s2 in the remaining s1
    for i in range(count1, n1):
        for j in range(len(s1)):
            if s1[j] == s2[idx2]:
                idx2 += 1
            if idx2 == len(s2):
                idx2 = 0
                count2 += 1
    return count2 // n2

if __name__ == '__main__':
    getMaxRepetitions()