def longestIncreasingPath(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for i in range(n)] for j in range(m)]
    def dfs(i,j):
        if dp[i][j] != 0:
            return dp[i][j]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        for dir in directions:
            x = dir[0] + i
            y = dir[1] + j
            if x < 0 or y < 0 or x >= m or y >= n or matrix[x][y] <= matrix[i][j]:
                continue
            dp[i][j] = max(dp[i][j],dfs(x,y))
        dp[i][j] += 1
        return dp[i][j]
    max_length = 0
    for i in range(m):
        for j in range(n):
            max_length = max(max_length,dfs(i,j))
    return max_length
matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(longestIncreasingPath(matrix))
matrix = [[3,4,5],[3,2,6],[2,2,1]]
print(longestIncreasingPath(matrix))
matrix = [[1]]
print(longestIncreasingPath(matrix))
