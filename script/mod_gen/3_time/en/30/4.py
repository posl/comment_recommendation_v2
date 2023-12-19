def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if stones[1] != 1:
        return False
    if len(stones) == 2:
        return True
    if stones[2] != 3:
        return False
    
    steps = [set() for _ in range(len(stones))]
    steps[1].add(1)
    for i in range(1, len(stones)):
        for j in range(i):
            if stones[i] - stones[j] in steps[j]:
                steps[i].add(stones[i] - stones[j])
                steps[i].add(stones[i] - stones[j] + 1)
                steps[i].add(stones[i] - stones[j] - 1)
    if len(steps[-1]) == 0:
        return False
    return True

if __name__ == '__main__':
    canCross()