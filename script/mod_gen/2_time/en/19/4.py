def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal <= maxChoosableInteger:
        return True
    if sum(range(1, maxChoosableInteger + 1)) < desiredTotal:
        return False
    return helper(list(range(1, maxChoosableInteger + 1)), desiredTotal, {})

if __name__ == '__main__':
    canIWin()