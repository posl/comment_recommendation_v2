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

if __name__ == '__main__':
    getMaxRepetitions()