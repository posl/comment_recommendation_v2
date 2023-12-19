def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if len(stones) == 2:
        if stones[1] != 1:
            return False
        else:
            return True
    if stones[1] != 1:
        return False
    if stones[-1] > (stones[-2] + len(stones) - 1):
        return False
    if stones[-1] == (stones[-2] + len(stones) - 1):
        return True
    if stones[-1] < (stones[-2] + len(stones) - 1):
        return True
    return False

if __name__ == '__main__':
    canCross()