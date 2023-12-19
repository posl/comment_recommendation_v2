def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if stones[1] != 1:
        return False
    if len(stones) == 2:
        return True
    return canCrossHelper(stones, 1, 1)

if __name__ == '__main__':
    canCross()