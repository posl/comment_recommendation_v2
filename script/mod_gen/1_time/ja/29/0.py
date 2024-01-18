class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        ret = 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        def dfs(x: int, y: int) -> int:
            if dp[x][y] != 0:
                return dp[x][y]
            ret = 1
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if x + dx >= 0 and x + dx < m and y + dy >= 0 and y + dy < n and matrix[x + dx][y + dy] > matrix[x][y]:
                    ret = max(ret, dfs(x + dx, y + dy) + 1)
            dp[x][y] = ret
            return ret
        for i in range(m):
            for j in range(n):
                ret = max(ret, dfs(i, j))
        return ret

if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    a = Solution()
    print(a.longestIncreasingPath(matrix))