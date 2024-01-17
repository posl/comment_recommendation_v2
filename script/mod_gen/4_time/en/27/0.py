class Solution:
    def countDigitOne(self, n: int) -> int:
        if n == 0: return 0
        if n < 10: return 1
        if n < 20: return 2
        if n < 100: return 20 + 1 * (n - 10)
        if n < 200: return 20 + self.countDigitOne(n - 100) + 100
        if n < 1000: return 300 + 2 * self.countDigitOne(n - 200)
        if n < 2000: return 300 + self.countDigitOne(n - 1000) + 1000
        if n < 10000: return 4000 + 3 * self.countDigitOne(n - 2000)
        if n < 20000: return 4000 + self.countDigitOne(n - 10000) + 10000
        if n < 100000: return 50000 + 4 * self.countDigitOne(n - 20000)
        if n < 200000: return 50000 + self.countDigitOne(n - 100000) + 100000
        if n < 1000000: return 600000 + 5 * self.countDigitOne(n - 200000)
        if n < 2000000: return 600000 + self.countDigitOne(n - 1000000) + 1000000
        if n < 10000000: return 7000000 + 6 * self.countDigitOne(n - 2000000)
        if n < 20000000: return 7000000 + self.countDigitOne(n - 10000000) + 10000000
        if n < 100000000: return 80000000 + 7 * self.countDigitOne(n - 20000000)
        if n < 200000000: return 80000000 + self.countDigitOne(n - 100000000) + 100000000
        if n < 1000000000: return 900000000 + 8 * self.countDigitOne(n - 200000000)
        if n < 2000000000: return 900000000 + self.countDigitOne(n - 1000000000) + 1000000000
        return 0

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.countDigitOne(n))