def getMaxRepetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    #get the length of s1 and s2
    l1 = len(s1)
    l2 = len(s2)
    #initialize the number of times s1 and s2 have been repeated
    count1 = 0
    count2 = 0
    #initialize the index of s1 and s2
    i = 0
    j = 0
    #initialize the number of times s2 can be repeated in s1
    rep = 0
    #initialize the number of times s2 can be repeated in s1
    rep1 = 0
    #while the number of times s1 has been repeated is less than n1
    while count1 < n1:
        #if the character at index i in s1 is equal to the character at index j in s2
        if s1[i] == s2[j]:
            #increment i and j
            i += 1
            j += 1
            #if j is equal to the length of s2
            if j == l2:
                #reset j to 0
                j = 0
                #increment the number of times s2 has been repeated
                count2 += 1
        #otherwise, the character at index i in s1 is not equal to the character at index j in s2
        else:
            #increment i
            i += 1
        #if i is equal to the length of s1
        if i == l1:
            #reset i to 0
            i = 0
            #increment the number of times s1 has been repeated
            count1 += 1
    #return the number of times s2 can be repeated in s1 divided by n2
    return count2 // n2

if __name__ == '__main__':
    getMaxRepetitions()