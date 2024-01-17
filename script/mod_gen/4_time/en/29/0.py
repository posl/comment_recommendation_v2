class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        def dfs(i, j, prev):
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] <= prev:
                return 0
            if dp[i][j]:
                return dp[i][j]
            up = dfs(i-1, j, matrix[i][j])
            down = dfs(i+1, j, matrix[i][j])
            left = dfs(i, j-1, matrix[i][j])
            right = dfs(i, j+1, matrix[i][j])
            dp[i][j] = max(up, down, left, right) + 1
            return dp[i][j]
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dfs(i, j, -1))
        return res

if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    a = Solution()
    print(a.longestIncreasingPath(matrix))