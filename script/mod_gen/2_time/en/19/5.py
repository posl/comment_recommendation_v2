def canIWin(maxChoosableInteger, desiredTotal):
    if sum(range(maxChoosableInteger+1)) < desiredTotal:
        return False
    elif desiredTotal <= 0:
        return True
    else:
        return dfs(maxChoosableInteger, desiredTotal, 0, {})

if __name__ == '__main__':
    canIWin()