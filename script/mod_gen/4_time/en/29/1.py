def longestIncreasingPath(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    def dfs(i, j):
        if dp[i][j] != 0:
            return dp[i][j]
        for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            xi = i + x
            yj = j + y
            if 0 <= xi < rows and 0 <= yj < cols and matrix[i][j] < matrix[xi][yj]:
                dp[i][j] = max(dp[i][j], dfs(xi, yj))
        dp[i][j] += 1
        return dp[i][j]
    res = 0
    for i in range(rows):
        for j in range(cols):
            res = max(res, dfs(i, j))
    return res
matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(longestIncreasingPath(matrix))
