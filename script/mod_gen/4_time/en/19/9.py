def canIWin(maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """
    if maxChoosableInteger >= desiredTotal:
        return True
    if (maxChoosableInteger+1)*maxChoosableInteger//2 < desiredTotal:
        return False
    def helper(used, desiredTotal):
        if desiredTotal <= 0:
            return False
        key = tuple(used)
        if key in memo:
            return memo[key]
        for i in range(1, maxChoosableInteger+1):
            if used[i]:
                continue
            used[i] = True
            if not helper(used, desiredTotal-i):
                memo[key] = True
                used[i] = False
                return True
            used[i] = False
        memo[key] = False
        return False
    memo = {}
    used = [False]*(maxChoosableInteger+1)
    return helper(used, desiredTotal)
print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 40))
print(canIWin(20, 210))
print("The booleans above should be False, True, True, True, and False.")

if __name__ == '__main__':
    canIWin()