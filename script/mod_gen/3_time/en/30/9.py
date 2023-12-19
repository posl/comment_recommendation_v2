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
        if stones[2] == 2:
            return True
        else:
            return False
    if stones[2] != 2:
        return False
    if len(stones) == 4:
        if stones[3] == 3:
            return True
        else:
            return False
    if stones[3] != 3:
        return False
    if len(stones) == 5:
        if stones[4] == 5:
            return True
        else:
            return False
    if stones[4] != 5:
        return False
    if len(stones) == 6:
        if stones[5] == 6:
            return True
        else:
            return False
    if stones[5] != 6:
        return False
    if len(stones) == 7:
        if stones[6] == 8:
            return True
        else:
            return False
    if stones[6] != 8:
        return False
    if len(stones) == 8:
        if stones[7] == 12:
            return True
        else:
            return False
    if stones[7] != 12:
        return False
    if len(stones) == 9:
        if stones[8] == 17:
            return True
        else:
            return False
    if stones[8] != 17:
        return False
    if len(stones) == 10:
        if stones[9] == 23:
            return True
        else:
            return False
    if stones[9] != 23:
        return False
    if len(stones) == 11:
        if stones[10] == 30:
            return True
        else:
            return False
    if stones[10] != 30:
        return False
    if len(stones) == 12:
        if stones[11] == 38:
            return True
        else:
            return False
    if stones[11] != 38:
        return False

if __name__ == '__main__':
    canCross()