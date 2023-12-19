def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal:
        return True
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
        return False
    def helper(nums, desiredTotal, memo):
        if nums[-1] >= desiredTotal:
            return True
        if str(nums) in memo:
            return memo[str(nums)]
        for i in range(len(nums)):
            if not helper(nums[:i] + nums[i+1:], desiredTotal - nums[i], memo):
                memo[str(nums)] = True
                return True
        memo[str(nums)] = False
        return False
    return helper([i for i in range(1, maxChoosableInteger + 1)], desiredTotal, {})
print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(20, 200))
print(canIWin(20, 210))
print(canIWin(20, 211))
print(canIWin(20, 300))
print(canIWin(20, 301))
print(canIWin(20, 302))
print(canIWin(20, 303))
print(canIWin(20, 304))
print(canIWin(20, 305))
print(canIWin(20, 306))
print(canIWin(20, 307))
print(canIWin(20, 308))
print(canIWin(20, 309))
print(canIWin(20, 310))
print(canIWin(20, 311))
print(canIWin(20, 312))
print(canIWin(20, 313))
print(canIWin(20, 314))
print(canIWin(20, 315))
print(canIWin(20, 316))
print(canIWin(20, 317))
print(canIWin(20, 318))
print(canIWin(20, 319))
print(canIWin(20, 320))
print(canIWin(20, 321))
print(canIWin(20, 322))
print(canIWin(20, 323))
print(canIWin(20, 324))
print(canIWin(20, 325))
print(canIWin(20
