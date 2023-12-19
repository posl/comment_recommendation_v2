def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    if not matrix:
        return 0
    R, C = len(matrix), len(matrix[0])
    dp = [[0] * C for _ in range(R)]
    def dfs(r, c):
        if dp[r][c] != 0:
            return dp[r][c]
        val = matrix[r][c]
        dp[r][c] = 1 + max(
            dfs(r - 1, c) if r > 0 and val > matrix[r - 1][c] else 0,
            dfs(r + 1, c) if r < R - 1 and val > matrix[r + 1][c] else 0,
            dfs(r, c - 1) if c > 0 and val > matrix[r][c - 1] else 0,
            dfs(r, c + 1) if c < C - 1 and val > matrix[r][c + 1] else 0
        )
        return dp[r][c]
    return max(dfs(r, c) for r in range(R) for c in range(C))

if __name__ == '__main__':
    longestIncreasingPath()