def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal == 0:
        return True
    if desiredTotal > (maxChoosableInteger * (maxChoosableInteger + 1)) // 2:
        return False
    return dfs(0, [False] * maxChoosableInteger, desiredTotal, {})

if __name__ == '__main__':
    canIWin()