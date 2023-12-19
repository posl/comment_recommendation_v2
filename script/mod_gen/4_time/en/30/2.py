def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    stones_set = set(stones)
    def dp(position, jump):
        if position == stones[-1]:
            return True
        if position not in stones_set:
            return False
        return dp(position + jump + 1, jump + 1) or dp(position + jump, jump) or dp(position + jump - 1, jump - 1)
    return dp(1, 1)
print(canCross([0,1,3,5,6,8,12,17]))
print(canCross([0,1,2,3,4,8,9,11]))
