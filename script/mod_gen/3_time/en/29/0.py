def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    if not matrix:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    memo = [[0 for _ in range(cols)] for _ in range(rows)]
    def dfs(row, col, prev):
        if row < 0 or row >= rows or col < 0 or col >= cols or matrix[row][col] <= prev:
            return 0
        if memo[row][col] > 0:
            return memo[row][col]
        left = dfs(row, col - 1, matrix[row][col])
        right = dfs(row, col + 1, matrix[row][col])
        up = dfs(row - 1, col, matrix[row][col])
        down = dfs(row + 1, col, matrix[row][col])
        memo[row][col] = max(left, right, up, down) + 1
        return memo[row][col]
    max_path = 0
    for row in range(rows):
        for col in range(cols):
            max_path = max(max_path, dfs(row, col, float('-inf')))
    return max_path

if __name__ == '__main__':
    longestIncreasingPath()