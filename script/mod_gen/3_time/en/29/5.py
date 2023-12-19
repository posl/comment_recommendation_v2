def longestIncreasingPath(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            dp[i][j] = dfs(matrix,dp,i,j,m,n)
    return max(max(x) for x in dp)

if __name__ == '__main__':
    longestIncreasingPath()