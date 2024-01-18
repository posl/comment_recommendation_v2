class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 10
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + self.count(i)
        return dp[n]

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.countNumbersWithUniqueDigits(n))