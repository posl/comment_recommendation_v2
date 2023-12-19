def canIWin(maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """
    if maxChoosableInteger >= desiredTotal:
        return True
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
        return False
    if maxChoosableInteger == 1:
        return desiredTotal == 1
    if maxChoosableInteger == 2:
        return desiredTotal % 2 == 0
    if maxChoosableInteger == 3:
        return desiredTotal % 3 != 0
    return canIWin(maxChoosableInteger - 3, desiredTotal - 3) or canIWin(maxChoosableInteger - 2, desiredTotal - 2) or canIWin(maxChoosableInteger - 1, desiredTotal - 1)

if __name__ == '__main__':
    canIWin()