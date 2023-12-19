def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    def dfs(i, j):
        if dp[i][j] != 0: return dp[i][j]
        val = matrix[i][j]
        dp[i][j] = 1 + max(
            dfs(i - 1, j) if i > 0 and matrix[i - 1][j] > val else 0,
            dfs(i + 1, j) if i < m - 1 and matrix[i + 1][j] > val else 0,
            dfs(i, j - 1) if j > 0 and matrix[i][j - 1] > val else 0,
            dfs(i, j + 1) if j < n - 1 and matrix[i][j + 1] > val else 0
        )
        return dp[i][j]
    return max(dfs(x, y) for x in range(m) for y in range(n))

if __name__ == '__main__':
    longestIncreasingPath()