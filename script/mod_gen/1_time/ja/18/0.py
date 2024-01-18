class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 10
        for i in range(2, n + 1):
            tmp = 9
            for j in range(9, 9 - i + 1, -1):
                tmp *= j
            ans += tmp
        return ans

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.countNumbersWithUniqueDigits(n))