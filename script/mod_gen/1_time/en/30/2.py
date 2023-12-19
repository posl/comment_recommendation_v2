def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if len(stones) == 2:
        return stones[1] == 1
    elif stones[1] != 1:
        return False
    else:
        if stones[2] == 2:
            return True
        else:
            return False
    return True
stones = [0,1,3,5,6,8,12,17]
print(canCross(stones))
stones = [0,1,2,3,4,8,9,11]
print(canCross(stones))
stones = [0,2]
print(canCross(stones))
stones = [0,1,3,6,10,15,16,21]
print(canCross(stones))
stones = [0,1,3,6,10,15,16,21]
print(canCross(stones))
stones = [0,1,3,6,10,15,16,21]
print(canCross(stones))
stones = [0,1,3,6,10,15,16,21]
print(canCross(stones))
stones = [0,1,3,6,10,15,16,21]
print(canCross(stones))
stones = [0,1,3,6,10,15,16,21]
print(canCross(stones))
stones = [0,1,3,6,10,15,16,21]
print(canCross(stones))
stones = [0,1,3,6,10,15,16,21]
print(canCross(stones))
stones = [0,1,3,6,10,15,16,21]
print(canCross(stones))
stones = [0,1,3,6,10,15,16,21]
print(canCross(stones))
