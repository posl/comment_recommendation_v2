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

if __name__ == '__main__':
    longestIncreasingPath()