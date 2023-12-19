def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal:
        return True
    if (maxChoosableInteger * (maxChoosableInteger + 1)) / 2 < desiredTotal:
        return False
    def helper(choices, desiredTotal):
        if choices[-1] >= desiredTotal:
            return True
        for i in range(len(choices)):
            if not helper(choices[:i] + choices[i + 1:], desiredTotal - choices[i]):
                return True
        return False
    return helper(list(range(1, maxChoosableInteger + 1)), desiredTotal)
print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 40))
print(canIWin(10, 100))
print(canIWin(10, 101))
