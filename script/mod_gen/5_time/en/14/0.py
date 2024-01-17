class Solution:
    def integerBreak(self, n: int) -> int:
        def dfs(n, k):
            if n == 0:
                return 1
            if k == 1:
                return n
            res = 0
            for i in range(1, n):
                res = max(res, i * dfs(n - i, k - 1))
            return res
        res = 0
        for k in range(2, n + 1):
            res = max(res, dfs(n, k))
        return res

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.integerBreak(n))