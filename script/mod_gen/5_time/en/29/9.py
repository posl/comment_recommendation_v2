def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    if not matrix:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    def dfs(i, j):
        if dp[i][j] != 0:
            return dp[i][j]
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + i, y + j
            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] > matrix[i][j]:
                dp[i][j] = max(dp[i][j], dfs(nx, ny))
        dp[i][j] += 1
        return dp[i][j]
    return max(dfs(i, j) for i in range(rows) for j in range(cols))

if __name__ == '__main__':
    longestIncreasingPath()