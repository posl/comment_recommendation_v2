def longestIncreasingPath(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    cache = [[None for j in range(cols)] for i in range(rows)]
    maxPath = 0
    for i in range(rows):
        for j in range(cols):
            path = dfs(i, j, matrix, cache)
            maxPath = max(maxPath, path)
    return maxPath

if __name__ == '__main__':
    longestIncreasingPath()