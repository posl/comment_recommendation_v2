def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    # Time Complexity: O(mn)
    # Space Complexity: O(mn)
    if not matrix:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    cache = [[0 for _ in range(n)] for _ in range(m)]
    max_len = 0
    for i in range(m):
        for j in range(n):
            curr_len = dfs(matrix, cache, i, j)
            max_len = max(max_len, curr_len)
    return max_len

if __name__ == '__main__':
    matrix = ==========please modify============
    a = longestIncreasingPath(matrix)
    print(a)