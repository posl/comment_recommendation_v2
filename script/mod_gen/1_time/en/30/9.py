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
    if stones[2] > 3:
        return False
    if stones[3] > 5:
        return False
    if stones[3] == 5:
        if stones[4] == 7:
            return False
        else:
            return True
    if stones[3] == 4:
        if stones[4] == 6:
            return False
        else:
            return True
    if stones[3] == 3:
        if stones[4] == 5:
            return False
        else:
            return True
    if stones[3] == 2:
        if stones[4] == 4:
            return False
        else:
            return True
    if stones[3] == 1:
        if stones[4] == 3:
            return False
        else:
            return True
    if stones[3] == 0:
        if stones[4] == 2:
            return False
        else:
            return True
    if stones[4] == 6:
        if stones[5] == 9:
            return False
        else:
            return True
    if stones[4] == 5:
        if stones[5] == 8:
            return False
        else:
            return True
    if stones[4] == 4:
        if stones[5] == 7:
            return False
        else:
            return True
    if stones[4] == 3:
        if stones[5] == 6:
            return False
        else:
            return True
    if stones[4] == 2:
        if stones[5] == 5:
            return False
        else:
            return True
    if stones[4] == 1:
        if stones[5] == 4:
            return False
        else:
            return True
    if stones[4] == 0:
        if stones[5] ==

if __name__ == '__main__':
    canCross()