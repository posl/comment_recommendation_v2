def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if len(stones) < 2:
        return True
    if stones[1] != 1:
        return False
    if len(stones) == 2:
        return True
    if stones[1] + 1 not in stones[2:]:
        return False
    if stones[1] + 2 not in stones[2:]:
        return False
    if stones[1] + 3 not in stones[2:]:
        return False
    if len(stones) == 3:
        return True
    if stones[1] + 3 == stones[2] and stones[1] + 4 == stones[3]:
        return False
    if stones[1] + 3 == stones[2] and stones[1] + 6 == stones[3]:
        return False
    if stones[1] + 2 == stones[2] and stones[1] + 4 == stones[3]:
        return False
    if stones[1] + 2 == stones[2] and stones[1] + 5 == stones[3]:
        return False
    if stones[1] + 1 == stones[2] and stones[1] + 3 == stones[3]:
        return False
    if stones[1] + 1 == stones[2] and stones[1] + 4 == stones[3]:
        return False
    if stones[1] + 1 == stones[2] and stones[1] + 5 == stones[3]:
        return False
    if stones[1] + 1 == stones[2] and stones[1] + 6 == stones[3]:
        return False
    if stones[1] + 1 == stones[2] and stones[1] + 7 == stones[3]:
        return False
    if stones[1] + 1 == stones[2] and stones[1] + 8 == stones[3]:
        return False
    if stones[1] + 1 == stones[2] and stones[1] + 9 == stones[3]:
        return False
    if stones[1] + 1 == stones[2] and stones[1] + 10 ==

if __name__ == '__main__':
    canCross()