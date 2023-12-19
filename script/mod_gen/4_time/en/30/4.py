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
    stones = stones[1:]
    last = stones[-1]
    stones = stones[:-1]
    setStones = set(stones)
    stones = [0] + stones
    #print(stones)
    #print(setStones)
    #print(last)
    def canJump(stone, jump):
        #print(stone, jump)
        if stone == last:
            return True
        if stone + jump + 1 in setStones:
            if canJump(stone + jump + 1, jump + 1):
                return True
        if stone + jump in setStones:
            if canJump(stone + jump, jump):
                return True
        if jump - 1 > 0 and stone + jump - 1 in setStones:
            if canJump(stone + jump - 1, jump - 1):
                return True
        return False
    return canJump(0, 1)

if __name__ == '__main__':
    canCross()