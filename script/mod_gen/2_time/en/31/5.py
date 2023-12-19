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

if __name__ == '__main__':
    getMaxRepetitions()