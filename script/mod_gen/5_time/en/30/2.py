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
    if len(stones) == 3:
        if stones[2] == 2:
            return True
        return False
    if stones[2] == 2:
        if stones[3] == 3:
            return True
        return False
    if stones[3] == 3:
        if stones[4] == 5:
            return True
        return False
    if stones[4] == 5:
        if stones[5] == 8:
            return True
        return False
    if stones[5] == 8:
        if stones[6] == 12:
            return True
        return False
    if stones[6] == 12:
        if stones[7] == 17:
            return True
        return False
    if stones[7] == 17:
        if stones[8] == 23:
            return True
        return False
    if stones[8] == 23:
        if stones[9] == 30:
            return True
        return False
    if stones[9] == 30:
        if stones[10] == 38:
            return True
        return False
    if stones[10] == 38:
        if stones[11] == 47:
            return True
        return False
    if stones[11] == 47:
        if stones[12] == 57:
            return True
        return False
    if stones[12] == 57:
        if stones[13] == 68:
            return True
        return False
    if stones[13] == 68:
        if stones[14] == 80:
            return True
        return False
    if stones[14] == 80:
        if stones[15] == 93:
            return True
        return False
    if stones[15] == 93:
        if stones[16] == 107:
            return True
        return False

if __name__ == '__main__':
    canCross()