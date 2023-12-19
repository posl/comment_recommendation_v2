def canIWin(maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """
    if maxChoosableInteger >= desiredTotal:
        return True
    if (maxChoosableInteger+1)*maxChoosableInteger < desiredTotal*2:
        return False
    def helper(nums, desiredTotal, cache):
        if nums[-1] >= desiredTotal:
            return True
        key = tuple(nums)
        if key in cache:
            return cache[key]
        for i in range(len(nums)):
            if not helper(nums[:i]+nums[i+1:], desiredTotal-nums[i], cache):
                cache[key] = True
                return True
        cache[key] = False
        return False
    return helper(list(range(1, maxChoosableInteger+1)), desiredTotal, {})

if __name__ == '__main__':
    canIWin()