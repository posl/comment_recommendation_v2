def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal:
        return True
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
        return False
    memo = {}
    def helper(nums, desiredTotal):
        if nums[-1] >= desiredTotal:
            return True
        key = str(nums)
        if key in memo:
            return memo[key]
        for i in range(len(nums)):
            if not helper(nums[:i] + nums[i+1:], desiredTotal - nums[i]):
                memo[key] = True
                return True
        memo[key] = False
        return False
    return helper(list(range(1, maxChoosableInteger + 1)), desiredTotal)
print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 40))
print(canIWin(10, 55))
print(canIWin(10, 56))
print(canIWin(10, 57))
print(canIWin(10, 58))
print(canIWin(10, 59))
print(canIWin(10, 60))
print(canIWin(10, 61))
print(canIWin(10, 62))
print(canIWin(10, 63))
print(canIWin(10, 64))
print(canIWin(10, 65))
print(canIWin(10, 66))
print(canIWin(10, 67))
print(canIWin(10, 68))
print(canIWin(10, 69))
print(canIWin(10, 70))
print(canIWin(10, 71))
print(canIWin(10, 72))
print(canIWin(10, 73))
print(canIWin(10, 74))
print(canIWin(10, 75))
print(canIWin(10, 76))
print(canIWin(10, 77))
print(canIWin(10, 78))
print(canIWin(10, 79))
print(canIWin(10, 80))
print(canIWin(10, 81))
print(canIWin(10, 82))
print(canIWin(10, 83))
print

if __name__ == '__main__':
    canIWin()