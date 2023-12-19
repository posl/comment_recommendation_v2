def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal:
        return True
    if (maxChoosableInteger * (maxChoosableInteger + 1) / 2) < desiredTotal:
        return False
    memo = {}
    def dfs(used, total):
        if total <= 0:
            return False
        key = str(used)
        if key in memo:
            return memo[key]
        for i in range(1, maxChoosableInteger + 1):
            if used & (1 << i) == 0:
                if not dfs(used | (1 << i), total - i):
                    memo[key] = True
                    return True
        memo[key] = False
        return False
    return dfs(0, desiredTotal)
print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(18, 79))
print(canIWin(4, 6))
print(canIWin(20, 210))
