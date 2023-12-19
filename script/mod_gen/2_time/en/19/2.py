def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal:
        return True
    if sum(range(maxChoosableInteger + 1)) < desiredTotal:
        return False
    dp = {}
    def helper(nums, desiredTotal):
        if nums[-1] >= desiredTotal:
            return True
        key = tuple(nums)
        if key in dp:
            return dp[key]
        for i in range(len(nums)):
            if not helper(nums[:i] + nums[i+1:], desiredTotal - nums[i]):
                dp[key] = True
                return True
        dp[key] = False
        return False
    return helper(list(range(1, maxChoosableInteger + 1)), desiredTotal)
print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
