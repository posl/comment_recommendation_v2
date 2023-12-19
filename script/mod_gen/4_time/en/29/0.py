def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    if not matrix:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    max_path = 0
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                max_path = max(max_path, dfs(matrix, visited, i, j))
    return max_path

if __name__ == '__main__':
    longestIncreasingPath()