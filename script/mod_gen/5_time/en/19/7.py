def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal == 0 or maxChoosableInteger >= desiredTotal:
        return True
    if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
        return False
    def helper(nums, desiredTotal, memo):
        if memo[nums] != None:
            return memo[nums]
        if nums[-1] >= desiredTotal:
            return True
        for i in range(len(nums)):
            if not helper(nums[:i] + nums[i+1:], desiredTotal - nums[i], memo):
                memo[nums] = True
                return True
        memo[nums] = False
        return False
    memo = {}
    nums = [i for i in range(1, maxChoosableInteger + 1)]
    return helper(tuple(nums), desiredTotal, memo)
print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 2))
print(canIWin(10, 3))
print(canIWin(10, 4))
print(canIWin(10, 5))
print(canIWin(10, 6))
print(canIWin(10, 7))
print(canIWin(10, 8))
print(canIWin(10, 9))
print(canIWin(10, 10))
print(canIWin(10, 11))
print(canIWin(10, 12))
print(canIWin(10, 13))
print(canIWin(10, 14))
print(canIWin(10, 15))
print(canIWin(10, 16))
print(canIWin(10, 17))
print(canIWin(10, 18))
print(canIWin(10, 19))
print(canIWin(10, 20))
print(canIWin(10, 21))
print(canIWin(10, 22))
print(canIWin(10, 23))
print(canIWin(10, 24))
print(canIWin(10, 25))
print(canIWin(10, 26))
print(canIWin(10, 27))
print(canIWin(10, 28))
print(canIWin(10, 29))
