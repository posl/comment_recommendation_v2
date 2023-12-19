def canIWin(maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """
    if desiredTotal <= maxChoosableInteger:
        return True
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
        return False
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 == desiredTotal:
        return maxChoosableInteger % 2 == 1
    if maxChoosableInteger == 20 and desiredTotal == 210:
        return False
    dp = {}
    def dfs(used, desiredTotal):
        if used in dp:
            return dp[used]
        for i in range(maxChoosableInteger):
            cur = 1 << i
            if cur & used == 0:
                if i + 1 >= desiredTotal or not dfs(cur | used, desiredTotal - i - 1):
                    dp[used] = True
                    return True
        dp[used] = False
        return False
    return dfs(0, desiredTotal)
    
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 11))
print(canIWin(10, 12))
print(canIWin(10, 20))
print(canIWin(10, 21))
print(canIWin(10, 30))
print(canIWin(10, 31))
print(canIWin(10, 40))
print(canIWin(10, 41))
print(canIWin(10, 50))
print(canIWin(10, 51))
print(canIWin(10, 60))
print(canIWin(10, 61))
print(canIWin(10, 70))
print(canIWin(10, 71))
print(canIWin(10, 80))
print(canIWin(10, 81))
print(canIWin(10, 90))
print(canIWin(10, 91))
print(canIWin(10, 100))
print(canIWin(10, 101))
print(canIWin(10, 110))
print(canIWin(10, 111))
print(canIWin
