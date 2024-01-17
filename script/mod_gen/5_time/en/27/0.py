class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n < 10:
            return 1
        res = 0
        s = str(n)
        length = len(s)
        for i in range(length):
            res += self.helper(s, i, n)
        return res

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.countDigitOne(n))