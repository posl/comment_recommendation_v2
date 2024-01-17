class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 10
        if n == 2: return 91
        if n > 2: return self.countNumbersWithUniqueDigits(n-1) + (self.countNumbersWithUniqueDigits(n-1) - self.countNumbersWithUniqueDigits(n-2))*(11-n)

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.countNumbersWithUniqueDigits(n))