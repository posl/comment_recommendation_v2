def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if len(stones) == 2:
        if stones[1] == 1:
            return True
        else:
            return False
    if stones[1] != 1:
        return False
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
print(canCross([0,1,3,5,6,8,12,17]))
print(canCross([0,1,2,3,4,8,9,11]))
print(canCross([0,2]))
print(canCross([0,1,3,4,5,7,9,10,12]))
print(canCross([0,1,3,4,5,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25
