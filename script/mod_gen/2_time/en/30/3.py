def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if stones[1] != 1:
        return False
    if len(stones) == 2:
        return True
    jump = {}
    for i in range(1, len(stones)):
        jump[stones[i]] = set()
    jump[1].add(1)
    for i in range(1, len(stones)):
        for j in jump[stones[i]]:
            if j - 1 > 0:
                if stones[i] + j - 1 in jump:
                    jump[stones[i] + j - 1].add(j - 1)
            if stones[i] + j in jump:
                jump[stones[i] + j].add(j)
            if stones[i] + j + 1 in jump:
                jump[stones[i] + j + 1].add(j + 1)
    return len(jump[stones[-1]]) > 0
print(canCross([0,1,3,5,6,8,12,17]))
print(canCross([0,1,2,3,4,8,9,11]))
