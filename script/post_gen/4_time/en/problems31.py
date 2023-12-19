Synthesizing 10/10 solutions

=======
Suggestion 1

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
    s1cnt, index, s2cnt = 0, 0, 0
    recall = dict()
    while True:
        s1cnt += 1
        for ch in s1:
            if ch == s2[index]:
                index += 1
                if index == len(s2):
                    s2cnt, index = s2cnt + 1, 0
        if s1cnt == n1:
            return s2cnt // n2
        if index in recall:
            s1cnt_prime, s2cnt_prime = recall[index]
            pre_loop = (s1cnt_prime, s2cnt_prime)
            in_loop = (s1cnt - s1cnt_prime, s2cnt - s2cnt_prime)
            break
        else:
            recall[index] = (s1cnt, s2cnt)
    ans = pre_loop[1] + (n1 - pre_loop[0]) // in_loop[0] * in_loop[1]
    rest = (n1 - pre_loop[0]) % in_loop[0]
    for i in range(rest):
        for ch in s1:
            if ch == s2[index]:
                index += 1
                if index == len(s2):
                    ans, index = ans + 1, 0
    return ans // n2

=======
Suggestion 2

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

=======
Suggestion 3

def getMaxRepetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    # The idea is to find the number of s2's in s1
    # and then divide that number by n2
    # The number of s2's in s1 is the number of
    # times s2 can be repeated in s1
    # This can be done by using a hashmap to keep track
    # of the number of times s2 is repeated in s1
    # and the index at which it is repeated
    # If the index is already present in the hashmap
    # then the pattern repeats and we can find the
    # length of the pattern and the number of times
    # the pattern repeats
    # We can then use this information to find the
    # number of times s2 can be repeated in s1
    # and then divide that number by n2
    # to get the number of times s2 can be repeated
    # in s1
    # We can then use this information to find the
    # number of times s2 can be repeated in s1
    # and then divide that number by n2
    # to get the number of times s2 can be repeated
    # in s1
    # We can then use this information to find the
    # number of times s2 can be repeated in s1
    # and then divide that number by n2
    # to get the number of times s2 can be repeated
    # in s1
    # We can then use this information to find the
    # number of times s2 can be repeated in s1
    # and then divide that number by n2
    # to get the number of times s2 can be repeated
    # in s1
    # We can then use this information to find the
    # number of times s2 can be repeated in s1
    # and then divide that number by n2
    # to get the number of times s2 can be repeated
    # in s1
    # We can then use this information to find the
    # number of times s2

=======
Suggestion 4

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
    #s1 = "aaa", n1 = 3, s2 = "aa", n2 = 1
    #s1 = "aaa", n1 = 3, s2 = "aa", n2 = 2
    #s1 = "aaa", n1 = 3, s2 = "aa", n2 = 3
    #s1 = "aaa", n1 = 3, s2 = "aa", n2 = 4
    #s1 = "aaa", n1 = 3, s2 = "aa", n2 = 5
    #s1 = "aaa", n1 = 3, s2 = "aa", n2 = 6
    #s1 = "aaa", n1 = 3, s2 = "aa", n2 = 7
    #s1 = "aaa", n1 = 3, s2 = "aa", n2 = 8
    #s1 = "aaa", n1 = 3, s2 = "aa", n2 = 9
    #s1 = "aaa", n1 = 3, s2 = "aa", n2 = 10
    #s1 = "aaa", n1 = 3, s2 = "aa", n2 = 11
    #s1 = "aaa", n1 = 3, s2 = "aa", n2 = 12
    #s1 = "aaa", n1 = 3, s2 = "aa", n2 = 13
    #s1 = "aaa", n1 = 3, s2 = "aa", n2 = 14
    #s1 = "aaa", n1 = 3, s2 = "aa", n2 = 15

=======
Suggestion 5

def getMaxRepetitions(s1: str, n1: int, s2: str, n2: int) -> int:
    if n1 == 0:
        return 0
    s1cnt, index, s2cnt = 0, 0, 0
    recall = dict()
    while True:
        s1cnt += 1
        for i in range(len(s1)):
            if s1[i] == s2[index]:
                index += 1
                if index == len(s2):
                    s2cnt, index = s2cnt + 1, 0
        if s1cnt == n1:
            return s2cnt // n2
        if index in recall:
            s1cnt_prime, s2cnt_prime = recall[index]
            pre_loop = (s1cnt_prime, s2cnt_prime)
            in_loop = (s1cnt - s1cnt_prime, s2cnt - s2cnt_prime)
            break
        else:
            recall[index] = (s1cnt, s2cnt)
    ans = pre_loop[1] + (n1 - pre_loop[0]) // in_loop[0] * in_loop[1]
    rest = (n1 - pre_loop[0]) % in_loop[0]
    for i in range(rest):
        for c in s1:
            if c == s2[index]:
                index += 1
                if index == len(s2):
                    ans, index = ans + 1, 0
    return ans // n2

print(getMaxRepetitions("acb", 4, "ab", 2))
print(getMaxRepetitions("acb", 1, "acb", 1))

=======
Suggestion 6

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

=======
Suggestion 7

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

=======
Suggestion 8

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

=======
Suggestion 9

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
    s1cnt, index, s2cnt = 0, 0, 0
    recall = dict()
    while True:
        s1cnt += 1
        for i in range(len(s1)):
            if s1[i] == s2[index]:
                index += 1
                if index == len(s2):
                    s2cnt += 1
                    index = 0
        if s1cnt == n1:
            return s2cnt // n2
        if index in recall:
            s1cnt_prime, s2cnt_prime = recall[index]
            pre_loop = (s1cnt_prime, s2cnt_prime)
            in_loop = (s1cnt - s1cnt_prime, s2cnt - s2cnt_prime)
            break
        else:
            recall[index] = (s1cnt, s2cnt)
    ans = pre_loop[1] + (n1 - pre_loop[0]) // in_loop[0] * in_loop[1]
    rest = (n1 - pre_loop[0]) % in_loop[0]
    for i in range(rest):
        for c in s1:
            if c == s2[index]:
                index += 1
                if index == len(s2):
                    ans += 1
                    index = 0
    return ans // n2

print(getMaxRepetitions("acb", 4, "ab", 2))
print(getMaxRepetitions("acb", 1, "acb", 1))
print(getMaxRepetitions("aaa", 3, "aa", 1))
print("The values above should be 2, 1, and 4.")

=======
Suggestion 10

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
