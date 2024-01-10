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

if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    a = longestIncreasingPath(matrix)
    print(a)