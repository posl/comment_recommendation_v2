def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal:
        return True
    if (1+maxChoosableInteger)*maxChoosableInteger/2 < desiredTotal:
        return False
    def helper(nums, desiredTotal, memo):
        if nums[-1] >= desiredTotal:
            return True
        key = str(nums)
        if key in memo:
            return memo[key]
        for i in range(len(nums)):
            if not helper(nums[:i]+nums[i+1:], desiredTotal-nums[i], memo):
                memo[key] = True
                return True
        memo[key] = False
        return False
    memo = {}
    return helper(list(range(1, maxChoosableInteger+1)), desiredTotal, memo)
print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(18, 79))
print(canIWin(20, 209))
print(canIWin(20, 210))
print(canIWin(19, 190))
print(canIWin(19, 191))
print(canIWin(19, 192))
print(canIWin(19, 193))
print(canIWin(19, 194))
print(canIWin(19, 195))
print(canIWin(19, 196))
print(canIWin(19, 197))
print(canIWin(19, 198))
print(canIWin(19, 199))
print(canIWin(19, 200))
print(canIWin(19, 201))
print(canIWin(19, 202))
print(canIWin(19, 203))
print(canIWin(19, 204))
print(canIWin(19, 205))
print(canIWin(19, 206))
print(canIWin(19, 207))
print(canIWin(19, 208))
print(canIWin(19, 209))
print(canIWin(19, 210))
print(canIWin(19, 211))
print(canIWin(19, 212))
print(canIWin(19, 213))
print(canIWin(19, 214))
print(canIWin(19, 215))
print(canIWin(19, 216))
