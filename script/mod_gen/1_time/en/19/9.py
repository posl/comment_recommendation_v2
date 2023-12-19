def canIWin(maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """
    if desiredTotal == 0:
        return True
    if maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal:
        return False
    return canIWinHelper(list(range(1, maxChoosableInteger + 1)), desiredTotal, {})

if __name__ == '__main__':
    canIWin()