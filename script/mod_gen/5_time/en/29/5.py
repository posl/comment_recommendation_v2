def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    if not matrix:
        return 0
    R = len(matrix)
    C = len(matrix[0])
    dp = [[0 for _ in range(C)] for _ in range(R)]
    def dfs(i, j):
        if dp[i][j]:
            return dp[i][j]
        val = matrix[i][j]
        dp[i][j] = 1 + max(
            dfs(i-1, j) if i and val > matrix[i-1][j] else 0,
            dfs(i+1, j) if i < R-1 and val > matrix[i+1][j] else 0,
            dfs(i, j-1) if j and val > matrix[i][j-1] else 0,
            dfs(i, j+1) if j < C-1 and val > matrix[i][j+1] else 0)
        return dp[i][j]
    return max(dfs(x, y) for x in range(R) for y in range(C))

if __name__ == '__main__':
    longestIncreasingPath()