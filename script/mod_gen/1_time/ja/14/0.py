class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 2 or n > 58:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        dp[4] = 4
        for i in range(5, n + 1):
            max = 0
            for j in range(1, i // 2 + 1):
                temp = dp[j] * dp[i - j]
                if temp > max:
                    max = temp
            dp[i] = max
        return dp[n]

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.integerBreak(n))