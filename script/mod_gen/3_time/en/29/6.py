def longestIncreasingPath(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    def dfs(matrix, dp, i, j, m, n):
        if dp[i][j] != 0:
            return dp[i][j]
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        maxPath = 1
        for d in directions:
            x = i + d[0]
            y = j + d[1]
            if x >= 0 and x < m and y >= 0 and y < n and matrix[x][y] > matrix[i][j]:
                maxPath = max(maxPath, 1 + dfs(matrix, dp, x, y, m, n))
        dp[i][j] = maxPath
        return dp[i][j]
    for i in range(m):
        for j in range(n):
            if dp[i][j] == 0:
                dfs(matrix, dp, i, j, m, n)
    return max([max(x) for x in dp])
matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(longestIncreasingPath(matrix))
matrix = [[3,4,5],[3,2,6],[2,2,1]]
print(longestIncreasingPath(matrix))
matrix = [[1]]
print(longestIncreasingPath(matrix))
