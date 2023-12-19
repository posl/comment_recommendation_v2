def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal <= maxChoosableInteger:
        return True
    if (maxChoosableInteger*(maxChoosableInteger+1))//2 < desiredTotal:
        return False
    memo = {}
    def helper(maxChoosableInteger, desiredTotal, used):
        if used in memo:
            return memo[used]
        for i in range(1, maxChoosableInteger+1):
            if used & (1 << i) == 0:
                if desiredTotal <= i or not helper(maxChoosableInteger, desiredTotal-i, used | (1 << i)):
                    memo[used] = True
                    return True
        memo[used] = False
        return False
    return helper(maxChoosableInteger, desiredTotal, 0)
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
print(can

if __name__ == '__main__':
    canIWin()