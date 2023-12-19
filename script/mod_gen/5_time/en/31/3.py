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

if __name__ == '__main__':
    getMaxRepetitions()