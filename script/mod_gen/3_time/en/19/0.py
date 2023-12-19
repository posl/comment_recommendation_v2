def canIWin(maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """
    if maxChoosableInteger >= desiredTotal:
        return True
    if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
        return False
    return canIWinHelper(range(1, maxChoosableInteger + 1), desiredTotal)

if __name__ == '__main__':
    canIWin()