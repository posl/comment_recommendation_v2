def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    cache = [[0] * n for _ in range(m)]
    ans = 0
    for i in range(m):
        for j in range(n):
            ans = max(ans, dfs(matrix, i, j, cache))
    return ans

if __name__ == '__main__':
    longestIncreasingPath()