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
    # if s1 is empty or n1 is 0, return 0
    if not s1 or not n1:
        return 0

    # if s2 is empty or n2 is 0, return n1
    if not s2 or not n2:
        return n1

    # initialize the current index of s2, the number of repetitions
    # of s1 and s2, and the next index of s1
    curr_s2_index = 0
    s1_repetitions = 0
    s2_repetitions = 0
    next_s1_index = 0

    # while we haven't reached the end of s1
    while next_s1_index < len(s1):
        # if the current character of s1 is the same as the current
        # character of s2, move to the next character of s2
        if s1[next_s1_index] == s2[curr_s2_index]:
            curr_s2_index += 1

            # if we have reached the end of s2, we have found a repetition
            # of s2 in s1, so reset the index of s2 and increment the number
            # of repetitions of s2
            if curr_s2_index == len(s2):
                curr_s2_index = 0
                s2_repetitions += 1

        # move to the next index of s1
        next_s1_index += 1

        # if we have reached the end of s1, increment the number of
        # repetitions of s1 and reset the index of s1
        if next_s1_index == len(s1):
            next_s1_index = 0
            s1_repetitions += 1

    # return the number of repetitions of s2 in s1 divided by n2
    return s2_repetitions // n2

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
Suggestion 4

def getMaxRepetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
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

=======
Suggestion 5

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
    #s1 = "aaa", n1 = 3, s2 = "aaa", n2 = 2
    #s1 = "aaa", n1 = 3, s2 = "aaa", n2 = 3
    #s1 = "aaa", n1 = 3, s2 = "aaa", n2 = 4
    #s1 = "aaa", n1 = 3, s2 = "aaaa", n2 = 4
    #s1 = "aaa", n1 = 3, s2 = "aaaaaaaaaa", n2 = 4
    #s1 = "aaa", n1 = 3, s2 = "aaaaaaaaaaaa", n2 = 4
    #s1 = "aaa", n1 = 3, s2 = "aaaaaaaaaaaaa", n2 = 4
    #s1 = "aaa", n1 = 3, s2 = "aaaaaaaaaaaaaa", n2 = 4
    #s1 = "aaa", n1 = 3, s2 = "aaaaaaaaaaaaaaa", n2 = 4
    #s1 = "aaa", n1 = 3, s2 = "aaaaaaaaaaaaaaaa", n2 = 4
    #s1 = "aaa", n1 = 3, s2 = "aaaaaaaaaaaaaaaaa", n2 = 4
    #s1 = "aaa", n1 = 3, s2 = "aaaaaaaaaaaaaaaaaa", n2 = 4
    #s1 = "aaa", n1 = 3

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
    if n1 == 0:
        return 0
    s1cnt, index, s2cnt = 0, 0, 0
    # recall 是我们用来找循环节的变量，它是一个哈希映射
    # 我们如何找循环节？假设我们遍历了 s1cnt 个 s1，此时匹配到了第 s2cnt 个 s2 中的第 index 个字符
    # 如果我们之前遍历了 s1cnt' 个 s1 时，匹配到的是第 s2cnt' 个 s2 中同样的第 index 个字符，那么就有循环节了
    # 我们用 (s1cnt', s2cnt', index) 和 (s1cnt, s2cnt, index) 表示两次包含相同 index 的匹配结果
    # 那么显然有 s1cnt' = s1cnt，s2cnt' - s2cnt = n * (s1cnt - s1cnt')，其中 n >= 1
    # 我们就找到了循环节，对于找到循环节以后的字符串部分就不需要计算了
    # 注意 s2 是可以在中间任意位置开始匹配的
    recall = dict()
    while True:
        # 我们多遍历一个 s1，看看能不能找到循环节
        s1cnt += 1
        for ch in s1:
            if ch == s2[index]:
                index += 1
                if index == len(s2):
                    s2cnt, index = s2cnt + 1, 0
        # 还没有找到循环节，所有的 s1 就用完了
        if s1cnt == n1:
            return s2cnt // n2

=======
Suggestion 7

def getMaxRepetitions(s1,n1,s2,n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    # s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
    # s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
    # s1 = "aaa", n1 = 3, s2 = "aa", n2 = 1
    # s1 = "aaa", n1 = 3, s2 = "aa", n2 = 2
    # s1 = "aaa", n1 = 3, s2 = "aa", n2 = 3
    # s1 = "aaa", n1 = 3, s2 = "aa", n2 = 4
    # s1 = "aaa", n1 = 3, s2 = "aa", n2 = 5
    # s1 = "aaa", n1 = 3, s2 = "aa", n2 = 6
    # s1 = "aaa", n1 = 3, s2 = "aa", n2 = 7
    # s1 = "aaa", n1 = 3, s2 = "aa", n2 = 8
    # s1 = "aaa", n1 = 3, s2 = "aa", n2 = 9
    # s1 = "aaa", n1 = 3, s2 = "aa", n2 = 10
    # s1 = "aaa", n1 = 3, s2 = "aa", n2 = 11
    # s1 = "aaa", n1 = 3, s2 = "aa", n2 = 12
    # s1 = "aaa", n1 = 3, s2 = "aa", n2 = 13
    # s1 = "aaa", n1 = 3, s2 = "aa", n2 = 14
    # s1 = "aaa", n1 = 3, s2 = "aa", n2 = 15
    # s

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
    #s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
    #s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
    #s1 = "aaa", n1 = 3, s2 = "aa", n2 = 1
    #s1 = "aaa", n1 = 3, s2 = "aa", n2 = 2
    #s1 = "aaa", n1 = 3, s2 = "aa", n2 = 3
    #s1 = "aaa", n1 = 3, s2 = "aaa", n2 = 3
    #s1 = "aaa", n1 = 3, s2 = "aaaa", n2 = 3
    #s1 = "aaa", n1 = 3, s2 = "aaaaa", n2 = 3
    #s1 = "aaa", n1 = 3, s2 = "aaaaaa", n2 = 3
    #s1 = "aaa", n1 = 3, s2 = "aaaaaaa", n2 = 3
    #s1 = "aaa", n1 = 3, s2 = "aaaaaaaa", n2 = 3
    #s1 = "aaa", n1 = 3, s2 = "aaaaaaaaa", n2 = 3
    #s1 = "aaa", n1 = 3, s2 = "aaaaaaaaaa", n2 = 3
    #s1 = "aaa", n1 = 3, s2 = "aaaaaaaaaaa", n2 = 3
    #s1 = "aaa", n1 = 3, s2 = "aaaaaaaaaaaa", n2 = 3
    #s1 = "aaa", n1 = 3, s2 = "aaaaaaaaaaaaa", n2 = 3
    #s1 = "aaa", n1 = 3, s2 =

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
print(getMaxRepetitions("aaa", 3, "aa", 1))
print(getMaxRepetitions("aaa", 3, "aa", 2))
print(getMaxRepetitions("aaa", 3, "aaa", 1))
print(getMaxRepetitions("aaa", 3, "aaa", 2))
print(getMaxRepetitions("aaa", 3, "aaa", 3))
print(getMaxRepetitions("aaa", 3, "aaa",
