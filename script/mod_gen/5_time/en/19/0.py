def canIWin(maxChoosableInteger, desiredTotal):
    if (maxChoosableInteger * (maxChoosableInteger + 1) / 2) < desiredTotal:
        return False
    if maxChoosableInteger >= desiredTotal:
        return True
    memo = {}
    def dfs(nums, total):
        if nums[-1] >= total:
            return True
        key = tuple(nums)
        if key in memo:
            return memo[key]
        for i in range(len(nums)):
            if not dfs(nums[:i] + nums[i+1:], total - nums[i]):
                memo[key] = True
                return True
        memo[key] = False
        return False
    return dfs(list(range(1, maxChoosableInteger + 1)), desiredTotal)
print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 40))
