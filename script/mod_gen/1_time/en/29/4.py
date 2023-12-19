def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    ans = 0
    def dfs(x, y):
        if not dp[x][y]:
            val = matrix[x][y]
            dp[x][y] = 1 + max(
                dfs(x - 1, y) if x and val > matrix[x - 1][y] else 0,
                dfs(x + 1, y) if x < m - 1 and val > matrix[x + 1][y] else 0,
                dfs(x, y - 1) if y and val > matrix[x][y - 1] else 0,
                dfs(x, y + 1) if y < n - 1 and val > matrix[x][y + 1] else 0)
        return dp[x][y]
    for i in range(m):
        for j in range(n):
            ans = max(ans, dfs(i, j))
    return ans

if __name__ == '__main__':
    longestIncreasingPath()