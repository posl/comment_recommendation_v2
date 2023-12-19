def longestIncreasingPath(matrix):
    m = len(matrix)
    n = len(matrix[0])
    visited = [[0 for _ in range(n)] for _ in range(m)]
    longestPath = 0
    for i in range(m):
        for j in range(n):
            longestPath = max(longestPath, dfs(matrix, i, j, visited))
    return longestPath

if __name__ == '__main__':
    longestIncreasingPath()