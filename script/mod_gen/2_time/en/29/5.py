def longestIncreasingPath(matrix):
    if not matrix:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    cache = [[0 for _ in range(cols)] for _ in range(rows)]
    max_length = 0
    for i in range(rows):
        for j in range(cols):
            length = dfs(matrix, i, j, cache)
            max_length = max(max_length, length)
    return max_length

if __name__ == '__main__':
    longestIncreasingPath()