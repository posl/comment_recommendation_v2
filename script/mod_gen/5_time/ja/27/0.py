class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        for i in range(n+1):
            for j in str(i):
                if j == "1":
                    count += 1
        return count

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.countDigitOne(n))