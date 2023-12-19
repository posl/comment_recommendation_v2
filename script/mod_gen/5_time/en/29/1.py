def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    if not matrix:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    cache = [[0 for _ in range(cols)] for _ in range(rows)]
    def dfs(i,j):
        if cache[i][j]:
            return cache[i][j]
        val = matrix[i][j]
        maxPath = 0
        for direction in directions:
            newI = i + direction[0]
            newJ = j + direction[1]
            if 0 <= newI < rows and 0 <= newJ < cols and val < matrix[newI][newJ]:
                maxPath = max(maxPath, dfs(newI, newJ))
        cache[i][j] = maxPath + 1
        return cache[i][j]
    ans = 0
    for i in range(rows):
        for j in range(cols):
            ans = max(ans, dfs(i,j))
    return ans
print(longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
print(longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
print(longestIncreasingPath([[1]]))
print("The values above should be 4, 4, and 1.")

if __name__ == '__main__':
    longestIncreasingPath()