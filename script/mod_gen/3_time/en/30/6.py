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
        return True if stones[2] == 2 else False
    if stones[2] != 2:
        return False
    if len(stones) == 4:
        return True
    if stones[3] != 4:
        return False
    if len(stones) == 5:
        return True if stones[4] == 7 else False
    if stones[4] != 7:
        return False
    if len(stones) == 6:
        return True if stones[5] == 11 else False
    if stones[5] != 11:
        return False
    if len(stones) == 7:
        return True if stones[6] == 16 else False
    if stones[6] != 16:
        return False
    if len(stones) == 8:
        return True if stones[7] == 22 else False
    if stones[7] != 22:
        return False
    if len(stones) == 9:
        return True if stones[8] == 29 else False
    if stones[8] != 29:
        return False
    if len(stones) == 10:
        return True if stones[9] == 37 else False
    if stones[9] != 37:
        return False
    if len(stones) == 11:
        return True if stones[10] == 46 else False
    if stones[10] != 46:
        return False
    if len(stones) == 12:
        return True if stones[11] == 56 else False
    if stones[11] != 56:
        return False
    if len(stones) == 13:
        return True if stones[12] == 67 else False
    if stones[12] != 67:
        return False
    if len(stones) == 14:
        return True if stones[13] == 79 else False
    if stones[13] != 79:
        return False
    if len

if __name__ == '__main__':
    canCross()