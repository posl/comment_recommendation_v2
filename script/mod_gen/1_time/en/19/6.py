def canIWin(maxChoosableInteger, desiredTotal):
    def helper(maxChoosableInteger, desiredTotal, used, cache):
        if used in cache:
            return cache[used]
        for i in range(maxChoosableInteger):
            if not (used & (1 << i)):
                if desiredTotal <= i + 1 or not helper(maxChoosableInteger, desiredTotal - (i + 1), used | (1 << i), cache):
                    cache[used] = True
                    return True
        cache[used] = False
        return False
    if maxChoosableInteger >= desiredTotal:
        return True
    if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
        return False
    return helper(maxChoosableInteger, desiredTotal, 0, {})
print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
