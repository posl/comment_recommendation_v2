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
        return True
    if stones[3] != 4:
        return False
    if len(stones) == 5:
        return stones[4] == 5
    if stones[4] != 5:
        return False
    if len(stones) == 6:
        return True
    if stones[5] != 8:
        return False
    if len(stones) == 7:
        return stones[6] == 12
    if stones[6] != 12:
        return False
    if len(stones) == 8:
        return stones[7] == 17
    if stones[7] != 17:
        return False
    if len(stones) == 9:
        return True
    if stones[8] != 23:
        return False
    if len(stones) == 10:
        return stones[9] == 30
    if stones[9] != 30:
        return False
    if len(stones) == 11:
        return stones[10] == 38
    if stones[10] != 38:
        return False
    if len(stones) == 12:
        return stones[11] == 47
    if stones[11] != 47:
        return False
    if len(stones) == 13:
        return stones[12] == 57
    if stones[12] != 57:
        return False
    if len(stones) == 14:
        return stones[13] == 68
    if stones[13] != 68:
        return False
    if len(stones) == 15:
        return stones[14] == 80
    if stones[14] != 80:
        return False
    if len(stones) == 16:
        return stones[15] == 93
    if stones[15

if __name__ == '__main__':
    canCross()