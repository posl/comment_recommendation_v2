def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal:
        return True
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
        return False
    def canWin(choices, total, memo):
        if choices[-1] >= total:
            return True
        key = str(choices)
        if key in memo:
            return memo[key]
        for i in range(len(choices)):
            if not canWin(choices[:i] + choices[i+1:], total - choices[i], memo):
                memo[key] = True
                return True
        memo[key] = False
        return False
    return canWin(list(range(1, maxChoosableInteger + 1)), desiredTotal, {})
print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(20, 210))
