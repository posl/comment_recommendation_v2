def longestIncreasingPath(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    max_len = 0
    for i in range(m):
        for j in range(n):
            max_len = max(max_len, dfs(matrix, dp, i, j))
    return max_len

if __name__ == '__main__':
    matrix = ==========please modify============
    a = longestIncreasingPath(matrix)
    print(a)