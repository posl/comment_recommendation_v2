class Solution:
    def integerReplacement(self, n: int) -> int:
        return self.rec(n, 0)

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.integerReplacement(n))