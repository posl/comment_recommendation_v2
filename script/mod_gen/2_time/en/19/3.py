def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal == 0:
        return True
    elif desiredTotal > maxChoosableInteger * (maxChoosableInteger + 1) / 2:
        return False
    elif desiredTotal == maxChoosableInteger * (maxChoosableInteger + 1) / 2:
        return maxChoosableInteger % 2 == 1
    else:
        return canIWinHelper(maxChoosableInteger, desiredTotal, 0, {})

if __name__ == '__main__':
    canIWin()