def longestIncreasingPath(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for i in range(n)] for j in range(m)]
    def dfs(i, j):
        if dp[i][j] > 0:
            return dp[i][j]
        for x, y in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                dp[i][j] = max(dp[i][j], dfs(x, y))
        dp[i][j] += 1
        return dp[i][j]
    return max(dfs(i, j) for i in range(m) for j in range(n))
matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(longestIncreasingPath(matrix))
matrix = [[3,4,5],[3,2,6],[2,2,1]]
print(longestIncreasingPath(matrix))
matrix = [[1]]
print(longestIncreasingPath(matrix))
