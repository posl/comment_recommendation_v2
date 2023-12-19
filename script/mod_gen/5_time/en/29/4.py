def longestIncreasingPath(matrix):
    if not matrix:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    def dfs(matrix, i, j, dp):
        if dp[i][j] != 0:
            return dp[i][j]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for direction in directions:
            x = i + direction[0]
            y = j + direction[1]
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
                continue
            dp[i][j] = max(dp[i][j], dfs(matrix, x, y, dp))
        dp[i][j] += 1
        return dp[i][j]
    for i in range(m):
        for j in range(n):
            dfs(matrix, i, j, dp)
    return max([max(row) for row in dp])

if __name__ == '__main__':
    longestIncreasingPath()