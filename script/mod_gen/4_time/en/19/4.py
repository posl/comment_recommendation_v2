def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal:
        return True
    if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
        return False
    dp = {}
    def dfs(used, desiredTotal):
        if used in dp:
            return dp[used]
        for i in range(maxChoosableInteger):
            cur = 1 << i
            if cur & used == 0:
                if desiredTotal <= i + 1 or not dfs(used | cur, desiredTotal - i - 1):
                    dp[used] = True
                    return True
        dp[used] = False
        return False
    return dfs(0, desiredTotal)
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
print(canIWin(10, 20))
print(canIWin(10, 30))
print(canIWin(10, 40))
print(canIWin(10, 50))
print(canIWin(10, 60))
print(canIWin(10, 70))
print(canIWin(10, 80))
print(canIWin(10, 90))
print(canIWin(10, 100))
print(canIWin(10, 110))
print(canIWin(10, 120))
print(canIWin(10, 130))
print(canIWin(10, 140))
print(canIWin(10, 150))
print(canIWin(10, 160))
print(canIWin(10, 170))
print(canIWin(10, 180))
print(canIWin(10, 190))
print(canIWin(10, 200))
print(canIWin(10, 210))
print(canIWin(10, 220))
print(canI

if __name__ == '__main__':
    canIWin()