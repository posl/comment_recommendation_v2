def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if len(stones) == 0:
        return True
    if len(stones) == 1:
        return True
    if len(stones) == 2:
        if stones[1] == 1:
            return True
        else:
            return False
    if stones[1] != 1:
        return False
    stone_set = set(stones)
    target = stones[-1]
    queue = [(1, 1)]
    while queue:
        stone, step = queue.pop(0)
        for i in range(step - 1, step + 2):
            if i <= 0:
                continue
            if stone + i == target:
                return True
            if stone + i in stone_set:
                queue.append((stone + i, i))
    return False

if __name__ == '__main__':
    canCross()