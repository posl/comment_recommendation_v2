Synthesizing 10/10 solutions

=======
Suggestion 1

def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        ret = 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(x: int, y: int) -> int:
            if dp[x][y] != 0:
                return dp[x][y]
            ret = 1
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if x + dx >= 0 and x + dx < m and y + dy >= 0 and y + dy < n and matrix[x + dx][y + dy] > matrix[x][y]:
                    ret = max(ret, dfs(x + dx, y + dy) + 1)
            dp[x][y] = ret
            return ret

        for i in range(m):
            for j in range(n):
                ret = max(ret, dfs(i, j))
        return ret

=======
Suggestion 2

    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        # 1. DFS + Memoization
        # Time: O(mn)
        # Space: O(mn)
        # m, n = len(matrix), len(matrix[0])
        # memo = [[0] * n for _ in range(m)]
        # def dfs(i: int, j: int) -> int:
        #     if memo[i][j]: return memo[i][j]
        #     val = matrix[i][j]
        #     memo[i][j] = 1 + max(
        #         dfs(i + 1, j) if i + 1 < m and val < matrix[i + 1][j] else 0,
        #         dfs(i - 1, j) if i - 1 >= 0 and val < matrix[i - 1][j] else 0,
        #         dfs(i, j + 1) if j + 1 < n and val < matrix[i][j + 1] else 0,
        #         dfs(i, j - 1) if j - 1 >= 0 and val < matrix[i][j - 1] else 0
        #     )
        #     return memo[i][j]
        # return max(dfs(i, j) for i in range(m) for j in range(n))

        # 2. Topological Sort
        # Time: O(mn)
        # Space: O(mn)
        m, n = len(matrix), len(matrix[0])
        indegrees = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                val = matrix[i][j]
                for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= ni < m and 0 <= nj < n and val < matrix[ni][nj]:
                        indegrees[ni][nj] += 1
        queue = collections.deque([(i, j) for i in range(m) for j in range(n) if indegrees[i][j] == 0])
        ans = 0
        while queue:
            ans += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for

=======
Suggestion 3

def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        def dfs(i: int, j: int) -> int:
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < m - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < n - 1 and val > matrix[i][j + 1] else 0
                )
            return dp[i][j]

        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        return max(dfs(x, y) for x in range(m) for y in range(n))

=======
Suggestion 4

def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        # DFS + Memoization
        # Time Complexity: O(mn)
        # Space Complexity: O(mn)
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]
        def dfs(i, j):
            if memo[i][j] > 0:
                return memo[i][j]
            res = 0
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if 0 <= i + di < m and 0 <= j + dj < n and matrix[i][j] < matrix[i + di][j + dj]:
                    res = max(res, dfs(i + di, j + dj))
            memo[i][j] = res + 1
            return res + 1
        return max(dfs(i, j) for i in range(m) for j in range(n))

=======
Suggestion 5

def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        def dfs(i,j):
            if dp[i][j]: return dp[i][j]
            dp[i][j] = 1
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=x<m and 0<=y<n and matrix[i][j] < matrix[x][y]:
                    dp[i][j] = max(dp[i][j],dfs(x,y)+1)
            return dp[i][j]
        return max(dfs(i,j) for i in range(m) for j in range(n))

=======
Suggestion 6

def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        def dfs(i: int, j: int) -> int:
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0
                )
            return dp[i][j]

        if not matrix or not matrix[0]:
            return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for _ in range(M)]
        return max(dfs(x, y) for x in range(M) for y in range(N))

=======
Suggestion 7

def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
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

=======
Suggestion 8

def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        def dfs(i: int, j: int) -> int:
            if dp[i][j]:
                return dp[i][j]
            val = matrix[i][j]
            dp[i][j] = 1 + max(
                dfs(i - 1, j) if i and val < matrix[i - 1][j] else 0,
                dfs(i + 1, j) if i < M - 1 and val < matrix[i + 1][j] else 0,
                dfs(i, j - 1) if j and val < matrix[i][j - 1] else 0,
                dfs(i, j + 1) if j < N - 1 and val < matrix[i][j + 1] else 0
            )
            return dp[i][j]

        if not matrix:
            return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for _ in range(M)]
        return max(dfs(x, y) for x in range(M) for y in range(N))

=======
Suggestion 9

def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        memo = [[0 for _ in range(n)] for _ in range(m)]
        def dfs(i,j):
            if memo[i][j] != 0:
                return memo[i][j]
            memo[i][j] = 1
            for dx,dy in zip([0,0,1,-1],[1,-1,0,0]):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and matrix[i][j] < matrix[x][y]:
                    memo[i][j] = max(memo[i][j],dfs(x,y) + 1)
            return memo[i][j]

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans,dfs(i,j))
        return ans

=======
Suggestion 10

def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        # DFS
        def dfs(i: int, j: int) -> int:
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < m - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < n - 1 and val > matrix[i][j + 1] else 0
                )
            return dp[i][j]

        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        return max(dfs(x, y) for x in range(m) for y in range(n))
