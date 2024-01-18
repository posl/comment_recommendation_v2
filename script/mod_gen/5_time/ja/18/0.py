class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 0
        for i in range(1, n + 1):
            ans += 9 * self.permutation(9, i - 1)
        return ans + 1

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.countNumbersWithUniqueDigits(n))