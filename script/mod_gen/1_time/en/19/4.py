def canIWin(maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """
    if desiredTotal <= maxChoosableInteger:
        return True
    elif (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
        return False
    else:
        return canIWinHelper(list(range(1, maxChoosableInteger + 1)), 0, desiredTotal, {})

if __name__ == '__main__':
    canIWin()