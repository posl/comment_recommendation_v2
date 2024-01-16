from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if s[i] == t[j]:
                return dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                return dfs(i + 1, j)
        return dfs(0, 0)

if __name__ == '__main__':
    s = input()
    t = input()
    a = Solution()
    print(a.numDistinct(s, t))