Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def longestIncreasingPath(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    def dfs(i, j):
        if dp[i][j] != 0:
            return dp[i][j]
        for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            xi = i + x
            yj = j + y
            if 0 <= xi < rows and 0 <= yj < cols and matrix[i][j] < matrix[xi][yj]:
                dp[i][j] = max(dp[i][j], dfs(xi, yj))
        dp[i][j] += 1
        return dp[i][j]

    res = 0
    for i in range(rows):
        for j in range(cols):
            res = max(res, dfs(i, j))
    return res


matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(longestIncreasingPath(matrix))

=======
Suggestion 3

def longestIncreasingPath(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            if dp[i][j] == 0:
                dfs(matrix, i, j, dp)
    return max([max(i) for i in dp])

=======
Suggestion 4

def longestIncreasingPath(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    cache = [[None for j in range(cols)] for i in range(rows)]
    maxPath = 0
    for i in range(rows):
        for j in range(cols):
            path = dfs(i, j, matrix, cache)
            maxPath = max(maxPath, path)
    return maxPath

=======
Suggestion 5

def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    def dfs(row, col):
        if dp[row][col]:
            return dp[row][col]

        val = matrix[row][col]

        dp[row][col] = 1 + max(
            dfs(row + 1, col) if row + 1 < rows and matrix[row + 1][col] > val else 0,
            dfs(row - 1, col) if row - 1 >= 0 and matrix[row - 1][col] > val else 0,
            dfs(row, col + 1) if col + 1 < cols and matrix[row][col + 1] > val else 0,
            dfs(row, col - 1) if col - 1 >= 0 and matrix[row][col - 1] > val else 0)

        return dp[row][col]

    return max(dfs(x, y) for x in range(rows) for y in range(cols))

=======
Suggestion 6

def longestIncreasingPath(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for i in range(n)] for j in range(m)]
    def dfs(i, j):
        if dp[i][j] > 0:
            return dp[i][j]
        for x, y in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                dp[i][j] = max(dp[i][j], dfs(x, y))
        dp[i][j] += 1
        return dp[i][j]
    return max(dfs(i, j) for i in range(m) for j in range(n))

matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(longestIncreasingPath(matrix))
matrix = [[3,4,5],[3,2,6],[2,2,1]]
print(longestIncreasingPath(matrix))
matrix = [[1]]
print(longestIncreasingPath(matrix))

=======
Suggestion 7

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

=======
Suggestion 8

def longestIncreasingPath(matrix):
    def dfs(i, j):
        if not dp[i][j]:
            val = matrix[i][j]
            dp[i][j] = 1 + max(
                dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
        return dp[i][j]

    if not matrix or not matrix[0]: return 0
    M, N = len(matrix), len(matrix[0])
    dp = [[0] * N for i in range(M)]
    return max(dfs(x, y) for x in range(M) for y in range(N))

matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(longestIncreasingPath(matrix))
matrix = [[3,4,5],[3,2,6],[2,2,1]]
print(longestIncreasingPath(matrix))
matrix = [[1]]
print(longestIncreasingPath(matrix))
matrix = []
print(longestIncreasingPath(matrix))
matrix = [[]]
print(longestIncreasingPath(matrix))
matrix = [[2,2],[1,1]]
print(longestIncreasingPath(matrix))
matrix = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]]
print(longestIncreasingPath(matrix))
matrix = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15]]
print(longestIncreasingPath(matrix))
matrix = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]]
print(longestIncreasingPath(matrix))
matrix = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15]]
print(longestIncreasingPath(matrix))
matrix = [[1,2,3,4

=======
Suggestion 9

def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    def dfs(i,j):
        if not dp[i][j]:
            val = matrix[i][j]
            dp[i][j] = 1 + max(
                dfs(i-1, j) if i and val > matrix[i-1][j] else 0,
                dfs(i+1, j) if i < M-1 and val > matrix[i+1][j] else 0,
                dfs(i, j-1) if j and val > matrix[i][j-1] else 0,
                dfs(i, j+1) if j < N-1 and val > matrix[i][j+1] else 0
            )
        return dp[i][j]
    
    if not matrix or not matrix[0]:
        return 0
    
    M, N = len(matrix), len(matrix[0])
    dp = [[0] * N for i in range(M)]
    return max(dfs(x,y) for x in range(M) for y in range(N))

=======
Suggestion 10

def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    if not matrix:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    def dfs(i, j):
        if dp[i][j] != 0:
            return dp[i][j]
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                dp[i][j] = max(dp[i][j], dfs(x, y))
        dp[i][j] += 1
        return dp[i][j]
    return max(dfs(i, j) for i in range(m) for j in range(n))
