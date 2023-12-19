def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if len(stones) == 0:
        return True
    if len(stones) == 1:
        return True
    if stones[1] != 1:
        return False
    
    stones_set = set(stones)
    last = stones[-1]
    stack = [(1, 1)]
    while stack:
        pos, jump = stack.pop()
        for i in range(jump-1, jump+2):
            if i <= 0:
                continue
            next_pos = pos + i
            if next_pos == last:
                return True
            elif next_pos in stones_set:
                stack.append((next_pos, i))
    return False

if __name__ == '__main__':
    canCross()