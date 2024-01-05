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
        if stones[2] != 2:
            return False
        else:
            return True
    if stones[2] == 2:
        if stones[3] != 4:
            return False
    if stones[2] == 3:
        if stones[3] != 5:
            return False
    if stones[2] == 4:
        if stones[3] != 7:
            return False
    if stones[2] == 5:
        if stones[3] != 8:
            return False
    if stones[2] == 6:
        if stones[3] != 10:
            return False
    if stones[2] == 7:
        if stones[3] != 11:
            return False
    if stones[2] == 8:
        if stones[3] != 13:
            return False
    if stones[2] == 9:
        if stones[3] != 14:
            return False
    if stones[2] == 10:
        if stones[3] != 16:
            return False
    if stones[2] == 11:
        if stones[3] != 17:
            return False
    if stones[2] == 12:
        if stones[3] != 19:
            return False
    if stones[2] == 13:
        if stones[3] != 20:
            return False
    if stones[2] == 14:
        if stones[3] != 22:
            return False
    if stones[2] == 15:
        if stones[3] != 23:
            return False
    if stones[2] == 16:
        if stones[3] != 25:
            return False
    if stones[2] == 17:
        if stones[3] != 26:
            return False
    if stones[2]

if __name__ == '__main__':
    stones = list(map(int, input().split()))
    a = canCross(stones)
    print(a)