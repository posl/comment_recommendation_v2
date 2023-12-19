def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal <= maxChoosableInteger:
        return True
    if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
        return False
    if (1 + maxChoosableInteger) * maxChoosableInteger / 2 == desiredTotal:
        return maxChoosableInteger % 2 == 1
    return helper(desiredTotal, [False] * (maxChoosableInteger + 1), {})

if __name__ == '__main__':
    canIWin()