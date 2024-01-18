class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # 1. 全部の数字の合計がdesiredTotalより小さい場合は常にTrue
        if sum(range(1, maxChoosableInteger + 1)) < desiredTotal:
            return True
        # 2. どんなに最適にプレイしても常に負ける場合はFalse
        if maxChoosableInteger >= desiredTotal:
            return False
        # 3. メモ化用の辞書を作成
        self.memo = {}
        # 4. 再帰関数を呼び出す
        return self.dfs(range(1, maxChoosableInteger + 1), desiredTotal)

if __name__ == '__main__':
    maxChoosableInteger = int(input())
    desiredTotal = int(input())
    a = Solution()
    print(a.canIWin(maxChoosableInteger, desiredTotal))