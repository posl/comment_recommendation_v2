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

if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    a = longestIncreasingPath(matrix)
    print(a)