class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        # https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/288520/Python-DFS-Memoization-with-Explanation
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, i, j, memo))
        return res

if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    a = Solution()
    print(a.longestIncreasingPath(matrix))