class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        # 二次元配列の行数と列数を取得
        row = len(matrix)
        col = len(matrix[0])
        # 増加経路の長さを保存する二次元配列
        dp = [[0] * col for _ in range(row)]
        # 増加経路の長さの最大値を保存する変数
        max_path = 1
        # 各セルからの増加経路の長さを求める
        for i in range(row):
            for j in range(col):
                # 各セルからの増加経路の長さを求める
                max_path = max(max_path, self.dfs(matrix, i, j, dp))
        return max_path

if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    a = Solution()
    print(a.longestIncreasingPath(matrix))