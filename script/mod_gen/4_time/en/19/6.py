def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal <= 0:
        return True
    if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
        return False
    if maxChoosableInteger >= desiredTotal:
        return True
    if maxChoosableInteger == desiredTotal - 1:
        return False
    return canIWinHelper(maxChoosableInteger, desiredTotal, 0, {})

if __name__ == '__main__':
    canIWin()