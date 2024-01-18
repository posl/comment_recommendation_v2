class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger: return True
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal: return False
        memo = {}
        def dfs(used, total):
            if total <= 0: return False
            key = tuple(used)
            if key in memo: return memo[key]
            for i in range(maxChoosableInteger):
                if used[i]: continue
                used[i] = True
                if not dfs(used, total - (i + 1)):
                    memo[key] = True
                    used[i] = False
                    return True
                used[i] = False
            memo[key] = False
            return False
        return dfs([False] * maxChoosableInteger, desiredTotal)

if __name__ == '__main__':
    maxChoosableInteger = int(input())
    desiredTotal = int(input())
    a = Solution()
    print(a.canIWin(maxChoosableInteger, desiredTotal))