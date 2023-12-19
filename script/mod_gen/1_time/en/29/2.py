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
