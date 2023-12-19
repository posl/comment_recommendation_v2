def canIWin(maxChoosableInteger, desiredTotal):
    if (maxChoosableInteger * (maxChoosableInteger + 1) // 2) < desiredTotal:
        return False
    if desiredTotal <= 0:
        return True
    memo = {}
    def helper(nums, desiredTotal):
        hash = str(nums)
        if hash in memo:
            return memo[hash]
        if nums[-1] >= desiredTotal:
            return True
        for i in range(len(nums)):
            if not helper(nums[:i] + nums[i+1:], desiredTotal - nums[i]):
                memo[hash] = True
                return True
        memo[hash] = False
        return False
    return helper(list(range(1, maxChoosableInteger + 1)), desiredTotal)
    
print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 40))
print(canIWin(10, 54))
print(canIWin(10, 100))
