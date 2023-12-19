def longestIncreasingPath(matrix):
    if len(matrix) == 0:
        return 0
    rows = len(matrix)
    columns = len(matrix[0])
    dp = [[0 for i in range(columns)] for j in range(rows)]
    def dfs(matrix, i, j, rows, columns, dp):
        if dp[i][j] != 0:
            return dp[i][j]
        maxPath = 0
        if i > 0 and matrix[i - 1][j] > matrix[i][j]:
            maxPath = max(maxPath, dfs(matrix, i - 1, j, rows, columns, dp))
        if i < rows - 1 and matrix[i + 1][j] > matrix[i][j]:
            maxPath = max(maxPath, dfs(matrix, i + 1, j, rows, columns, dp))
        if j > 0 and matrix[i][j - 1] > matrix[i][j]:
            maxPath = max(maxPath, dfs(matrix, i, j - 1, rows, columns, dp))
        if j < columns - 1 and matrix[i][j + 1] > matrix[i][j]:
            maxPath = max(maxPath, dfs(matrix, i, j + 1, rows, columns, dp))
        dp[i][j] = maxPath + 1
        return dp[i][j]
    for i in range(rows):
        for j in range(columns):
            dp[i][j] = dfs(matrix, i, j, rows, columns, dp)
    maxPath = 0
    for i in range(rows):
        for j in range(columns):
            maxPath = max(maxPath, dp[i][j])
    return maxPath

if __name__ == '__main__':
    longestIncreasingPath()