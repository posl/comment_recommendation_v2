class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger*(maxChoosableInteger+1)/2 < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True
        self.memo = {}
        return self.dfs([i for i in range(1, maxChoosableInteger+1)], desiredTotal)

if __name__ == '__main__':
    maxChoosableInteger = int(input())
    desiredTotal = int(input())
    a = Solution()
    print(a.canIWin(maxChoosableInteger, desiredTotal))