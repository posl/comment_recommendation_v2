def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if len(stones) == 0:
        return False
    if len(stones) == 1:
        return True
    if len(stones) == 2:
        if stones[1] == 1:
            return True
        else:
            return False
    if stones[1] != 1:
        return False
    
    i = 1
    while i < len(stones):
        if stones[i] - stones[i-1] > i:
            return False
        i += 1
    return True

if __name__ == '__main__':
    canCross()