class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(1,i//2+1):
                dp[i] = max(dp[i],max(j,dp[j])*max(i-j,dp[i-j]))
        return dp[n]

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.integerBreak(n))