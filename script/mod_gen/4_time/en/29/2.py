def longestIncreasingPath(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            if dp[i][j] == 0:
                dfs(matrix, i, j, dp)
    return max([max(i) for i in dp])

if __name__ == '__main__':
    longestIncreasingPath()