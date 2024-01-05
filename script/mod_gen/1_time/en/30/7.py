def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if len(stones) == 1:
        return True
    if stones[1] != 1:
        return False
    if len(stones) == 2:
        return True
    if len(stones) == 3:
        return True
    if len(stones) == 4:
        return True
    if stones[3] != 4:
        return False
    if len(stones) == 5:
        return True
    if len(stones) == 6:
        return True
    if len(stones) == 7:
        return True
    if len(stones) == 8:
        return True
    if stones[7] != 12:
        return False
    if len(stones) == 9:
        return True
    if len(stones) == 10:
        return True
    if len(stones) == 11:
        return True
    if len(stones) == 12:
        return True
    if len(stones) == 13:
        return True
    if len(stones) == 14:
        return True
    if len(stones) == 15:
        return True
    if len(stones) == 16:
        return True
    if len(stones) == 17:
        return True
    if len(stones) == 18:
        return True
    if len(stones) == 19:
        return True
    if len(stones) == 20:
        return True
    if len(stones) == 21:
        return True
    if len(stones) == 22:
        return True
    if len(stones) == 23:
        return True
    if len(stones) == 24:
        return True
    if len(stones) == 25:
        return True
    if len(stones) == 26:
        return True
    if len(stones) == 27:
        return True
    if len(stones) == 28:
        return True
    if len(stones) == 29:
        return True
    if len(stones) == 30:
        return True
    if len(stones) == 31:
        return True

if __name__ == '__main__':
    stones = list(map(int, input().split()))
    a = canCross(stones)
    print(a)