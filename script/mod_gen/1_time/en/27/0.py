class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n < 10:
            return 1
        count = 0
        for i in range(1, n+1):
            for j in str(i):
                if j == '1':
                    count += 1
        return count

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.countDigitOne(n))