def longestIncreasingPath(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    def dfs(i,j):
        if dp[i][j] != -1:
            return dp[i][j]
        dp[i][j] = 1
        for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if 0 <= x < m and 0 <= y < n and matrix[i][j] > matrix[x][y]:
                dp[i][j] = max(dp[i][j],dfs(x,y) + 1)
        return dp[i][j]
    ans = 0
    for i in range(m):
        for j in range(n):
            ans = max(ans,dfs(i,j))
    return ans
matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(longestIncreasingPath(matrix))
