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

if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    a = longestIncreasingPath(matrix)
    print(a)