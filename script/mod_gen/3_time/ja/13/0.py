class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 2147483647:
            return 32
        if n % 2 == 0:
            return self.integerReplacement(n/2) + 1
        else:
            return min(self.integerReplacement(n+1), self.integerReplacement(n-1)) + 1

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.integerReplacement(n))