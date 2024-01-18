class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # メモ化再帰
        memo = {}
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if s[i] == t[j]:
                memo[(i, j)] = dfs(i+1, j) + dfs(i+1, j+1)
            else:
                memo[(i, j)] = dfs(i+1, j)
            return memo[(i, j)]
        return dfs(0, 0)

if __name__ == '__main__':
    s = input()
    t = input()
    a = Solution()
    print(a.numDistinct(s, t))