def canIWin(maxChoosableInteger, desiredTotal):
    if (maxChoosableInteger * (maxChoosableInteger + 1)) / 2 < desiredTotal:
        return False
    if maxChoosableInteger >= desiredTotal:
        return True
    if maxChoosableInteger + 1 == desiredTotal:
        return False
    def helper(used, desiredTotal):
        if desiredTotal <= 0:
            return False
        key = str(used)
        if key in dp:
            return dp[key]
        for i in range(1, maxChoosableInteger + 1):
            if used & (1 << i):
                continue
            if not helper(used | (1 << i), desiredTotal - i):
                dp[key] = True
                return True
        dp[key] = False
        return False
    dp = {}
    return helper(0, desiredTotal)
print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 2))
print(canIWin(10, 3))
print(canIWin(10, 4))
print(canIWin(10, 5))
print(canIWin(10, 6))
print(canIWin(10, 7))
print(canIWin(10, 8))
print(canIWin(10, 9))
print(canIWin(10, 10))
print(canIWin(10, 11))
print(canIWin(10, 12))
print(canIWin(10, 13))
print(canIWin(10, 14))
print(canIWin(10, 15))
print(canIWin(10, 16))
print(canIWin(10, 17))
print(canIWin(10, 18))
print(canIWin(10, 19))
print(canIWin(10, 20))
print(canIWin(10, 21))
print(canIWin(10, 22))
print(canIWin(10, 23))
print(canIWin(10, 24))
print(canIWin(10, 25))
print(canIWin(10, 26))
print(canIWin(10, 27))
print(canIWin(10, 28))
print(canIWin(
