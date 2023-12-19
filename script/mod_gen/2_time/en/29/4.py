def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    if len(matrix) == 0:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for i in range(n)] for j in range(m)]
    def dfs(i, j):
        if dp[i][j] != 0:
            return dp[i][j]
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        for d in directions:
            x = i + d[0]
            y = j + d[1]
            if x >= 0 and x < m and y >= 0 and y < n and matrix[x][y] > matrix[i][j]:
                dp[i][j] = max(dp[i][j], dfs(x, y))
        dp[i][j] += 1
        return dp[i][j]
    res = 0
    for i in range(m):
        for j in range(n):
            res = max(res, dfs(i, j))
    return res
print(longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
print(longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
print(longestIncreasingPath([[1]]))
