def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal == 0:
        return True
    if (maxChoosableInteger * (maxChoosableInteger + 1)) / 2 < desiredTotal:
        return False
    memo = {}
    def helper(choices, desiredTotal):
        if choices[-1] >= desiredTotal:
            return True
        if str(choices) in memo:
            return memo[str(choices)]
        for i in range(len(choices)):
            if not helper(choices[:i] + choices[i+1:], desiredTotal - choices[i]):
                memo[str(choices)] = True
                return True
        memo[str(choices)] = False
        return False
    return helper(list(range(1, maxChoosableInteger + 1)), desiredTotal)
print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
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
print(canIWin(20, 326))
print(canIWin(20, 327))
print(canIWin(20, 328))
print(canIWin(20, 329))
print(canIWin
