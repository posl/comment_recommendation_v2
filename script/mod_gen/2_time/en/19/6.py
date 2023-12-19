def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal <= maxChoosableInteger:
        return True
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
        return False
    def canWin(choices, desiredTotal, cache):
        if choices[-1] >= desiredTotal:
            return True
        key = str(choices)
        if key in cache:
            return cache[key]
        for i in range(len(choices)):
            if not canWin(choices[:i] + choices[i + 1:], desiredTotal - choices[i], cache):
                cache[key] = True
                return True
        cache[key] = False
        return False
    return canWin(list(range(1, maxChoosableInteger + 1)), desiredTotal, {})
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
print(canIWin(
