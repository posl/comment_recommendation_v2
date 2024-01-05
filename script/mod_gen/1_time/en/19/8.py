def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal == 0:
        return True
    if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
        return False
    if maxChoosableInteger >= desiredTotal:
        return True
    return canIWinRec(maxChoosableInteger, desiredTotal, 0, {})

if __name__ == '__main__':
    maxChoosableInteger = int(input())
    desiredTotal = int(input())
    a = canIWin(maxChoosableInteger, desiredTotal)
    print(a)