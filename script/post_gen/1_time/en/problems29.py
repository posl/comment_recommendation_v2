Synthesizing 10/10 solutions

=======
Suggestion 1

def longestIncreasingPath(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for i in range(n)] for j in range(m)]
    def dfs(i,j):
        if dp[i][j] != 0:
            return dp[i][j]
        for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
            if 0 <= x < m and 0 <= y < n and matrix[x][y] < matrix[i][j]:
                dp[i][j] = max(dp[i][j],dfs(x,y))
        dp[i][j] += 1
        return dp[i][j]
    for i in range(m):
        for j in range(n):
            dfs(i,j)
    return max([max(i) for i in dp])

=======
Suggestion 2

def longestIncreasingPath(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    maxPath = 0
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                maxPath = max(maxPath, dfs(matrix, visited, i, j))
    return maxPath

=======
Suggestion 3

def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    rows = len(matrix)
    cols = len(matrix[0])
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    cache = [[-1 for _ in range(cols)] for _ in range(rows)]
    def dfs(x,y):
        if cache[x][y] != -1:
            return cache[x][y]
        maxLen = 0
        for d in dirs:
            nx = x + d[0]
            ny = y + d[1]
            if nx >= 0 and nx < rows and ny >= 0 and ny < cols and matrix[nx][ny] > matrix[x][y]:
                maxLen = max(maxLen, dfs(nx,ny))
        cache[x][y] = maxLen + 1
        return cache[x][y]
    maxLen = 0
    for i in range(rows):
        for j in range(cols):
            maxLen = max(maxLen, dfs(i,j))
    return maxLen

matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(longestIncreasingPath(matrix))

matrix = [[3,4,5],[3,2,6],[2,2,1]]
print(longestIncreasingPath(matrix))

matrix = [[1]]
print(longestIncreasingPath(matrix))

=======
Suggestion 4

def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    if matrix == []:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for j in range(n)] for i in range(m)]
    def dfs(i,j):
        if dp[i][j] != 0:
            return dp[i][j]
        for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if 0<=x<m and 0<=y<n and matrix[x][y] > matrix[i][j]:
                dp[i][j] = max(dp[i][j],dfs(x,y))
        dp[i][j] += 1
        return dp[i][j]
    res = 0
    for i in range(m):
        for j in range(n):
            res = max(res,dfs(i,j))
    return res

=======
Suggestion 5

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

=======
Suggestion 6

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
        res = 1
        for x, y in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                res = max(res, 1 + dfs(x,y))
        dp[i][j] = res
        return res
    res = 0
    for i in range(m):
        for j in range(n):
            res = max(res, dfs(i, j))
    return res

=======
Suggestion 7

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

=======
Suggestion 8

def longestIncreasingPath(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    max_len = 0
    for i in range(m):
        for j in range(n):
            max_len = max(max_len, dfs(matrix, dp, i, j))
    return max_len

=======
Suggestion 9

def longestIncreasingPath(matrix):
    if not matrix:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    max_len = 0
    for i in range(m):
        for j in range(n):
            max_len = max(max_len, dfs(matrix, i, j, dp))
    return max_len

=======
Suggestion 10

def longestIncreasingPath(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for i in range(n)] for j in range(m)]
    def dfs(i, j):
        if dp[i][j] != 0:
            return dp[i][j]
        res = 1
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= i + x < m and 0 <= j + y < n and matrix[i + x][j + y] > matrix[i][j]:
                res = max(res, dfs(i + x, j + y) + 1)
        dp[i][j] = res
        return res
    ans = 0
    for i in range(m):
        for j in range(n):
            ans = max(ans, dfs(i, j))
    return ans

matrix = [[9,9,4],[6,6,8],[2,1,1]]
result = longestIncreasingPath(matrix)
print(result)
