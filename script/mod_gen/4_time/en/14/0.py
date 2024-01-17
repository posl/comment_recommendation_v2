class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n==3:
            return 2
        if n%3 == 0:
            return 3**(n//3)
        if n%3 == 1:
            return 3**(n//3-1)*4
        if n%3 == 2:
            return 3**(n//3)*2

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.integerBreak(n))