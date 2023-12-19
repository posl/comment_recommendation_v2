def longestIncreasingPath(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for i in range(n)] for j in range(m)]
    def dfs(i, j):
        if dp[i][j] != 0:
            return dp[i][j]
        res = 1
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                res = max(res, dfs(x, y) + 1)
        dp[i][j] = res
        return res
    return max(dfs(i, j) for i in range(m) for j in range(n))

if __name__ == '__main__':
    longestIncreasingPath()