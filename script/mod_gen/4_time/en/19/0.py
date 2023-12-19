def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal:
        return True
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
        return False
    nums = [i for i in range(1, maxChoosableInteger + 1)]
    return dfs(nums, desiredTotal, {})

if __name__ == '__main__':
    canIWin()