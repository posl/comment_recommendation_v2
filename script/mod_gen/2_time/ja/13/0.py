class Solution:
    def integerReplacement(self, n: int) -> int:
        def dfs(n: int) -> int:
            if n == 1:
                return 0
            elif n % 2 == 0:
                return dfs(n // 2) + 1
            else:
                return min(dfs(n + 1), dfs(n - 1)) + 1
        return dfs(n)

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.integerReplacement(n))