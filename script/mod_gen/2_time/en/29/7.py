def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    def dfs(i, j):
        if dp[i][j]:
            return dp[i][j]
        for x, y in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                dp[i][j] = max(dp[i][j], dfs(x, y))
        dp[i][j] += 1
        return dp[i][j]
    return max(dfs(i, j) for i in range(m) for j in range(n))

if __name__ == '__main__':
    longestIncreasingPath()