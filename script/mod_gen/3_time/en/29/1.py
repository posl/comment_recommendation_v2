def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    if not matrix:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    def dfs(i, j):
        if dp[i][j]:
            return dp[i][j]
        val = matrix[i][j]
        dp[i][j] = 1 + max(
            dfs(i - 1, j) if i > 0 and val > matrix[i - 1][j] else 0,
            dfs(i + 1, j) if i < m - 1 and val > matrix[i + 1][j] else 0,
            dfs(i, j - 1) if j > 0 and val > matrix[i][j - 1] else 0,
            dfs(i, j + 1) if j < n - 1 and val > matrix[i][j + 1] else 0,
        )
        return dp[i][j]
    return max(dfs(x, y) for x in range(m) for y in range(n))
matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
print(longestIncreasingPath(matrix))
matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
print(longestIncreasingPath(matrix))
matrix = [[1]]
print(longestIncreasingPath(matrix))
matrix = [[1, 2]]
print(longestIncreasingPath(matrix))
matrix = [[1], [2]]
print(longestIncreasingPath(matrix))
matrix = [[1, 2, 3]]
print(longestIncreasingPath(matrix))
matrix = [[1], [2], [3]]
print(longestIncreasingPath(matrix))
matrix = [[1, 2], [3, 4]]
print(longestIncreasingPath(matrix))
matrix = [[1, 2, 3], [4, 5, 6]]
print(longestIncreasingPath(matrix))
matrix = [[1, 2], [3, 4], [5, 6]]
print(longestIncreasingPath(matrix))
matrix = [[1, 2, 3], [4, 5, 6

if __name__ == '__main__':
    longestIncreasingPath()