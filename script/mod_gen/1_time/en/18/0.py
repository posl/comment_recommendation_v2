class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        dp = [0] * (n + 1)
        dp[1] = 10
        dp[2] = 81
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] * (10 - i + 1)
        return sum(dp)

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.countNumbersWithUniqueDigits(n))