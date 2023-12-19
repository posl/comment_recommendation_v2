def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if stones[1] != 1:
        return False
    if len(stones) == 2:
        return True
    if len(stones) == 3:
        return stones[2] == 2
    if stones[2] != 2:
        return False
    if len(stones) == 4:
        return stones[3] == 3
    if stones[3] != 3:
        return False
    if len(stones) == 5:
        return stones[4] == 4
    if stones[4] != 4:
        return False
    if len(stones) == 6:
        return stones[5] == 5
    if stones[5] != 5:
        return False
    if len(stones) == 7:
        return stones[6] == 6
    if stones[6] != 6:
        return False
    if len(stones) == 8:
        return stones[7] == 7
    if stones[7] != 7:
        return False
    if len(stones) == 9:
        return stones[8] == 8
    if stones[8] != 8:
        return False
    if len(stones) == 10:
        return stones[9] == 9
    if stones[9] != 9:
        return False
    if len(stones) == 11:
        return stones[10] == 10
    if stones[10] != 10:
        return False
    if len(stones) == 12:
        return stones[11] == 11
    if stones[11] != 11:
        return False
    if len(stones) == 13:
        return stones[12] == 12
    if stones[12] != 12:
        return False
    if len(stones) == 14:
        return stones[13] == 13
    if stones[13] != 13:
        return False
    if len(stones) == 15:
        return stones[14] == 14
    if stones[14] != 14:
        return False
    if len(stones) ==

if __name__ == '__main__':
    canCross()