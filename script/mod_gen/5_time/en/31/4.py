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

if __name__ == '__main__':
    getMaxRepetitions()