def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal <= maxChoosableInteger:
        return True
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
        return False
    memo = {}
    def dfs(used, desiredTotal):
        if desiredTotal <= 0:
            return False
        if used in memo:
            return memo[used]
        for i in range(maxChoosableInteger):
            if used & (1 << i) == 0:
                if not dfs(used | (1 << i), desiredTotal - i - 1):
                    memo[used] = True
                    return True
        memo[used] = False
        return False
    return dfs(0, desiredTotal)
print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 40))
print(canIWin(10, 100))
print(canIWin(10, 200))
print(canIWin(10, 300))
print(canIWin(10, 301))
print(canIWin(20, 210))
print(canIWin(20, 211))
print(canIWin(20, 220))
print(canIWin(20, 230))
print(canIWin(20, 240))
print(canIWin(20, 250))
print(canIWin(20, 260))
print(canIWin(20, 270))
print(canIWin(20, 280))
print(canIWin(20, 290))
print(canIWin(20, 300))
print(canIWin(20, 301))
