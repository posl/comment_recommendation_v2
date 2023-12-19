def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal == 0:
        return True
    if sum(range(1, maxChoosableInteger + 1)) < desiredTotal:
        return False
    memo = {}
    def canWin(choices, total):
        if choices[-1] >= total:
            return True
        key = tuple(choices)
        if key in memo:
            return memo[key]
        for i in range(len(choices)):
            if not canWin(choices[:i] + choices[i+1:], total - choices[i]):
                memo[key] = True
                return True
        memo[key] = False
        return False
    return canWin(list(range(1, maxChoosableInteger + 1)), desiredTotal)
print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 40))
print(canIWin(10, 100))
print(canIWin(10, 300))
print(canIWin(20, 200))
print(canIWin(20, 210))
print(canIWin(20, 211))
print(canIWin(20, 300))
print(canIWin(20, 0))
