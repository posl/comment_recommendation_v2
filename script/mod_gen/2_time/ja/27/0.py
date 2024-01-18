class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            ans += str(i).count('1')
        return ans

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.countDigitOne(n))