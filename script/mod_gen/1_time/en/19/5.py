def canIWin(maxChoosableInteger, desiredTotal):
    def canWin(maxChoosableInteger, desiredTotal, used):
        if desiredTotal <= 0:
            return False
        key = str(used)
        if key in dp:
            return dp[key]
        for i in range(maxChoosableInteger):
            if not used[i]:
                used[i] = True
                if not canWin(maxChoosableInteger, desiredTotal - (i + 1), used):
                    dp[key] = True
                    used[i] = False
                    return True
                used[i] = False
        dp[key] = False
        return False
    dp = {}
    used = [False] * maxChoosableInteger
    return canWin(maxChoosableInteger, desiredTotal, used)

if __name__ == '__main__':
    canIWin()