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
    # get the count of s1 in s2
    s1Count = 0
    s2Count = 0
    i = 0
    j = 0
    while i < n1:
        if s1[j] == s2[i]:
            j += 1
            if j == len(s1):
                s1Count += 1
                j = 0
        i += 1
    i = 0
    j = 0
    while i < n2:
        if s2[j] == s1[i]:
            j += 1
            if j == len(s2):
                s2Count += 1
                j = 0
        i += 1
    return s1Count // s2Count

=======
Suggestion 2

def getMaxRepetitions(s1, n1, s2, n2):
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

s1 = "acb"
n1 = 4
s2 = "ab"
n2 = 2
print(getMaxRepetitions(s1, n1, s2, n2))

=======
Suggestion 3

def getMaxRepetitions(s1, n1, s2, n2):
    pass

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
print(getMaxRepetitions("aaa", 3, "aaa", 14))
print(getMaxRepetitions("aaa", 3, "aaa", 15))
print(getMaxRepetitions("aaa", 3, "aaa", 16))
print(getMaxRepetitions("aaa", 3, "aaa", 17))
print(getMaxRepetitions("aaa", 3, "aaa", 18))
print(getMaxRepetitions("aaa", 3, "aaa", 19))
print(getMaxRepetitions("aaa", 3, "aaa", 20))
print(getMaxRepetitions("aaa", 3, "aaa", 21))
print(getMaxRepetitions("aaa", 3, "aaa", 22))
print(getMaxRepetitions("aaa", 3, "aaa", 23))
print(getMaxRepetitions("aaa", 3, "

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
    if n1 == 0:
        return 0
    s1cnt, index, s2cnt = 0, 0, 0
    # recall 是我们用来找循环节的变量，它是一个哈希映射
    # 我们如何找循环节呢？假设我们遍历了 s1cnt 个 s1，此时匹配到了第 s2cnt 个 s2 中的第 index 个字符
    # 如果我们之前遍历了 s1cnt' 个 s1 时，匹配到的是第 s2cnt' 个 s2 中同样的第 index 个字符，就有循环节了！
    # 我们用 (s1cnt', s2cnt', index) 和 (s1cnt, s2cnt, index) 表示两次包含相同 index 的匹配结果
    # 那么显然有 s1cnt - s1cnt'个 s1 包含了一个循环节
    # 我们记这个循环节为 repeat，其包含 s2cnt' 个 s2
    # 我们把前 s1cnt' 个 s1 称为 prefix
    # 把 [s1cnt', s1cnt) 区间内的称为循环节 part
    s1cnt_map, s2cnt_map = {}, {}
    while True:
        # 我们多遍历一个 s1，看看能不能找到循环节
        s1cnt += 1
        for i in range(len(s1)):
            if s1[i] == s2[index]:
                index += 1
                if index == len(s2):
                    s2cnt += 1
                    index = 0
        if s1cnt == n1:
            return s2cnt // n2
        if index in s2cnt

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
    if n1 == 0:
        return 0
    s1cnt, index, s2cnt = 0, 0, 0
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
        # 出现了之前的 index，表示找到了循环节
        if index in recall:
            s1cnt_prime, s2cnt_prime = recall[index]
            # 前 s1cnt' 个 s1 包含了 s2cnt' 个 s2
            pre_loop = (s1cnt_prime, s2cnt_prime)
            # 以后的每 (s1cnt - s1cnt') 个 s1 包含了 (s2cnt - s2cnt') 个 s2
            in_loop = (s1cnt - s1cnt_prime, s2cnt - s2cnt_prime)
            break
        else:
            recall[index] = (s1cnt, s2cnt)
    # ans 存储的是 S1 包含的 s2 的数量，考虑的之前的 pre_loop 和 in_loop
    ans = pre_loop[1] + (n1 - pre_loop[0]) // in_loop[0] * in_loop[1]
    # S1 的末尾还剩下一些 s1，我们暴力进行匹配
    rest = (n1 - pre_loop[0]) % in_loop[0]
    for i in range(rest):
        for ch in s

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
    if n1 == 0:
        return 0
    s1cnt, index, s2cnt = 0, 0, 0
    # recall 是我们用来找循环节的变量，它是一个哈希映射
    # 我们如何找循环节？假设我们遍历了 s1cnt 个 s1，此时匹配到了第 s2cnt 个 s2 中的第 index 个字符
    # 如果我们之前遍历了 s1cnt' 个 s1 时，匹配到的是第 s2cnt' 个 s2 中同样的第 index 个字符，就有循环节了
    # 我们用 (s1cnt', s2cnt', index) 和 (s1cnt, s2cnt, index) 表示两次包含相同 index 的匹配结果
    # 那么显然有 s1cnt - s1cnt'个 s1 包含了一个循环节
    # 我们记 cost = (s1cnt - s1cnt', s2cnt - s2cnt', index) 表示这个循环节的长度是多少
    # 那么就有 s1cnt' = s1cnt - cost.s1cnt，s2cnt' = s2cnt - cost.s2cnt，此时 s1 和 s2 分别匹配了 s1cnt - s1cnt'和 s2cnt - s2cnt'个字符
    # 我们对于所有的 index = 0...n-1 都计算出 cost(index)，表示的是匹配到第 index 个字符时，s1 和 s2 的循环节长度
    # 注意到 index 是有 n 个取值的，但是 s1cnt' 和 s2cnt' 的取值可能是相同的，所以我们

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
    #s1 = "acb" * 4 = "acbacbacbacb"
    #s2 = "ab" * 2 = "abab"
    #s2 = "ab" * 2 =
