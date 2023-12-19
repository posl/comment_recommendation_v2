def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    if not matrix:
        return 0
    row = len(matrix)
    col = len(matrix[0])
    dp = [[0] * col for _ in range(row)]
    res = 0
    for i in range(row):
        for j in range(col):
            res = max(res, dfs(matrix, i, j, dp))
    return res

if __name__ == '__main__':
    longestIncreasingPath()