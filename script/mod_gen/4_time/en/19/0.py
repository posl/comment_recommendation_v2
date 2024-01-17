class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger >= desiredTotal:
            return True
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        self.memo = {}
        return self.dfs(range(1, maxChoosableInteger + 1), desiredTotal)

if __name__ == '__main__':
    maxChoosableInteger = int(input())
    desiredTotal = int(input())
    a = Solution()
    print(a.canIWin(maxChoosableInteger, desiredTotal))