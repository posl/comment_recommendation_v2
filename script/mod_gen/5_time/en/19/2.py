def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal: return True
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal: return False
    def helper(nums, desiredTotal):
        if nums[-1] >= desiredTotal: return True
        for i in range(len(nums)):
            if not helper(nums[:i] + nums[i + 1:], desiredTotal - nums[i]): return True
        return False
    return helper(list(range(1, maxChoosableInteger + 1)), desiredTotal)

if __name__ == '__main__':
    canIWin()