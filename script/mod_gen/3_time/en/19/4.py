def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal:
        return True
    if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
        return False
    def canIWinHelper(nums, desiredTotal, cache):
        if nums[-1] >= desiredTotal:
            return True
        key = tuple(nums)
        if key in cache:
            return cache[key]
        for i in range(len(nums)):
            if not canIWinHelper(nums[:i] + nums[i + 1:], desiredTotal - nums[i], cache):
                cache[key] = True
                return True
        cache[key] = False
        return False
    return canIWinHelper(list(range(1, maxChoosableInteger + 1)), desiredTotal, {})
print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 40))
print(canIWin(10, 50))
print(canIWin(10, 100))
print(canIWin(10, 150))
print(canIWin(10, 200))
print(canIWin(10, 250))
print(canIWin(10, 300))
print(canIWin(10, 350))
print(canIWin(10, 400))
print(canIWin(10, 450))
print(canIWin(10, 500))
print(canIWin(10, 550))
print(canIWin(10, 600))
print(canIWin(10, 650))
print(canIWin(10, 700))
print(canIWin(10, 750))
print(canIWin(10, 800))
print(canIWin(10, 850))
print(canIWin(10, 900))
print(canIWin(10, 950))
print(canIWin(10, 1000))
print(canIWin(10, 1050))
print(canIWin(10, 1100))
print(canIWin(10, 1150))
print(canIWin(10, 1200))
print(canIWin(10, 1250))
print(canIWin(10, 1300))
print(canIWin(10, 1350))
print(can

if __name__ == '__main__':
    canIWin()