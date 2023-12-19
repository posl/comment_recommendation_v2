def canIWin(maxChoosableInteger, desiredTotal):
    def helper(nums, desiredTotal, cache):
        if nums[-1] >= desiredTotal:
            return True
        key = str(nums)
        if key in cache:
            return cache[key]
        for i, num in enumerate(nums):
            if not helper(nums[:i] + nums[i+1:], desiredTotal - num, cache):
                cache[key] = True
                return True
        cache[key] = False
        return False
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
        return False
    return helper(list(range(1, maxChoosableInteger + 1)), desiredTotal, {})
print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 40))
print(canIWin(10, 100))
print(canIWin(10, 150))
print(canIWin(10, 300))
print(canIWin(20, 200))
print(canIWin(20, 210))
print(canIWin(20, 300))
print(canIWin(20, 310))
print(canIWin(20, 400))
print(canIWin(20, 410))
print(canIWin(20, 500))
print(canIWin(20, 510))
print(canIWin(20, 600))
print(canIWin(20, 610))
print(canIWin(20, 700))
print(canIWin(20, 710))
print(canIWin(20, 800))
print(canIWin(20, 810))
print(canIWin(20, 900))
print(canIWin(20, 910))
print(canIWin(20, 1000))
print(canIWin(20, 1010))
print(canIWin(20, 1100))
print(canIWin(20, 1110))
print(canIWin(20, 1200))
print(canIWin(20, 1210))
print(canIWin(20, 1300))
print(canIWin(20, 1310))
print(canIWin(20, 1400))
print(canIWin(20, 1410))
print(canIWin
