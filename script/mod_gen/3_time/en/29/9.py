def longestIncreasingPath(matrix):
    # Solution 1: Dynamic Programming
    # Time Complexity: O(mn)
    # Space Complexity: O(mn)
    # m, n = len(matrix), len(matrix[0])
    # dp = [[-1]*n for _ in range(m)]
    # def dfs(i, j):
    #     if dp[i][j] != -1:
    #         return dp[i][j]
    #     dp[i][j] = 1
    #     for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    #         x, y = i+dx, j+dy
    #         if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
    #             dp[i][j] = max(dp[i][j], dfs(x, y)+1)
    #     return dp[i][j]
    # return max(dfs(i, j) for i in range(m) for j in range(n))
    # Solution 2: Topological Sort
    # Time Complexity: O(mn)
    # Space Complexity: O(mn)
    m, n = len(matrix), len(matrix[0])
    indegree = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    indegree[i][j] += 1
    q = collections.deque()
    for i in range(m):
        for j in range(n):
            if indegree[i][j] == 0:
                q.append((i, j))
    ans = 0
    while q:
        ans += 1
        for _ in range(len(q)):
            i, j = q.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i+dx, j+

if __name__ == '__main__':
    longestIncreasingPath()