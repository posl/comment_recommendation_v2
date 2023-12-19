def getMaxRepetitions(s1: str, n1: int, s2: str, n2: int) -> int:
    if n1 == 0:
        return 0
    s1cnt, index, s2cnt = 0, 0, 0
    # recall 是我们用来找循环节的变量，它是一个哈希映射
    # 我们如何找循环节？假设我们遍历了 s1cnt 个 s1，此时匹配到了第 s2cnt 个 s2 中的第 index 个字符
    # 如果我们之前遍历了 s1cnt' 个 s1 时，匹配到的是第 s2cnt' 个 s2 中同样的第 index 个字符，那么就有循环节了
    # 我们用 (s1cnt', s2cnt', index) 和 (s1cnt, s2cnt, index) 表示两次匹配到的位置
    # 那么循环节就是 (s1cnt, s2cnt, index) - (s1cnt', s2cnt', index)，
    # 注意这里 s1cnt - s1cnt' 不能为 0，因为 s2cnt - s2cnt' = 0 时，index 的计算是没有意义的
    # 因为如果 s2cnt - s2cnt' = 0，我们无法得知 index 是多少
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

if __name__ == '__main__':
    getMaxRepetitions()