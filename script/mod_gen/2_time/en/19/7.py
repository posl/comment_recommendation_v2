def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal <= maxChoosableInteger:
        return True
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
        return False
    memo = {}
    return canIWinHelper(range(1, maxChoosableInteger + 1), desiredTotal, memo)

if __name__ == '__main__':
    canIWin()