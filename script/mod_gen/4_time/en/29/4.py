def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    if not matrix:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    def dfs(row, col):
        if dp[row][col]:
            return dp[row][col]
        val = matrix[row][col]
        dp[row][col] = 1 + max(
            dfs(row + 1, col) if row + 1 < rows and matrix[row + 1][col] > val else 0,
            dfs(row - 1, col) if row - 1 >= 0 and matrix[row - 1][col] > val else 0,
            dfs(row, col + 1) if col + 1 < cols and matrix[row][col + 1] > val else 0,
            dfs(row, col - 1) if col - 1 >= 0 and matrix[row][col - 1] > val else 0)
        return dp[row][col]
    return max(dfs(x, y) for x in range(rows) for y in range(cols))

if __name__ == '__main__':
    longestIncreasingPath()