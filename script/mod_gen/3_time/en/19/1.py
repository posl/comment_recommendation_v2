def canIWin(maxChoosableInteger: int, desiredTotal: int) -> bool:
    if desiredTotal <= maxChoosableInteger:
        return True
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
        return False
    return canIWinHelper(maxChoosableInteger, desiredTotal, 0, {})

if __name__ == '__main__':
    canIWin()