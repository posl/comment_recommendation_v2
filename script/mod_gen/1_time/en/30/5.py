def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if len(stones) == 2:
        return stones[1] == 1
    elif len(stones) == 3:
        return stones[2] == 2
    elif stones[1] != 1:
        return False
    stones_set = set(stones)
    stones_set.remove(0)
    memo = {}
    def can_cross(stone, k):
        if stone == stones[-1]:
            return True
        if (stone, k) in memo:
            return memo[(stone, k)]
        if k > 1 and stone + k - 1 in stones_set:
            if can_cross(stone + k - 1, k - 1):
                memo[(stone, k)] = True
                return True
        if stone + k in stones_set:
            if can_cross(stone + k, k):
                memo[(stone, k)] = True
                return True
        if stone + k + 1 in stones_set:
            if can_cross(stone + k + 1, k + 1):
                memo[(stone, k)] = True
                return True
        memo[(stone, k)] = False
        return False
    return can_cross(1, 1)

if __name__ == '__main__':
    stones = list(map(int, input().split()))
    a = canCross(stones)
    print(a)