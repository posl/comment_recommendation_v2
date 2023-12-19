def canCross(stones):
    if stones[1] != 1:
        return False
    if len(stones) == 2:
        return True
    if len(stones) == 3:
        return stones[2] == 2
    if stones[2] > 3:
        return False
    if stones[-1] > stones[1] * 2:
        return False
    if stones[-1] == stones[1] * 2:
        return True
    if stones[-1] == stones[1] * 2 - 1:
        return True
    if stones[-1] == stones[1] * 2 + 1:
        return True
    if stones[-1] == stones[1] * 2 - 2:
        return True
    if stones[-1] == stones[1] * 2 + 2:
        return True
    if stones[-1] == stones[1] * 2 - 3:
        return True
    if stones[-1] == stones[1] * 2 + 3:
        return True
    if stones[-1] == stones[1] * 2 - 4:
        return True
    if stones[-1] == stones[1] * 2 + 4:
        return True
    if stones[-1] == stones[1] * 2 - 5:
        return True
    if stones[-1] == stones[1] * 2 + 5:
        return True
    if stones[-1] == stones[1] * 2 - 6:
        return True
    if stones[-1] == stones[1] * 2 + 6:
        return True
    if stones[-1] == stones[1] * 2 - 7:
        return True
    if stones[-1] == stones[1] * 2 + 7:
        return True
    if stones[-1] == stones[1] * 2 - 8:
        return True
    if stones[-1] == stones[1] * 2 + 8:
        return True
    if stones[-1] == stones[1] * 2 - 9:
        return True
    if stones[-1] == stones[1] * 2 + 9:
        return True

if __name__ == '__main__':
    canCross()