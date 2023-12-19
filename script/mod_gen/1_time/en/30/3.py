def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if len(stones) == 0:
        return False
    if len(stones) == 1:
        return True
    if stones[1] != 1:
        return False
    if len(stones) == 2:
        return True
    if stones[2] != 3:
        return False
    if len(stones) == 3:
        return True
    if stones[3] != 6:
        return False
    if len(stones) == 4:
        return True
    if stones[4] != 10:
        return False
    if len(stones) == 5:
        return True
    if stones[5] != 15:
        return False
    if len(stones) == 6:
        return True
    if stones[6] != 21:
        return False
    if len(stones) == 7:
        return True
    if stones[7] != 28:
        return False
    if len(stones) == 8:
        return True
    if stones[8] != 36:
        return False
    if len(stones) == 9:
        return True
    if stones[9] != 45:
        return False
    if len(stones) == 10:
        return True
    if stones[10] != 55:
        return False
    if len(stones) == 11:
        return True
    if stones[11] != 66:
        return False
    if len(stones) == 12:
        return True
    if stones[12] != 78:
        return False
    if len(stones) == 13:
        return True
    if stones[13] != 91:
        return False
    if len(stones) == 14:
        return True
    if stones[14] != 105:
        return False
    if len(stones) == 15:
        return True
    if stones[15] != 120:
        return False
    if len(stones) == 16:
        return True
    if stones[16] != 136:
        return False
    if len(stones) == 17:
        return True

if __name__ == '__main__':
    canCross()