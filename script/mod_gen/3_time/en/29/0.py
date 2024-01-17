class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        cache = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, i, j, cache))
        return res

if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    a = Solution()
    print(a.longestIncreasingPath(matrix))