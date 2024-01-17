class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 1:
            return 0
        if n < 10:
            return 1
        res = 0
        for i in range(1, len(str(n))+1):
            res += self.count(n, i)
        return res

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.countDigitOne(n))