class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        ans = 1
        while n > 4:
            ans *= 3
            n -= 3
        ans *= n
        return ans

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.integerBreak(n))