class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        
        dp = [0] * (n + 1)
        dp[2] = 2
        dp[3] = 3
        
        for i in range(4, n + 1):
            dp[i] = max(3 * dp[i - 3], 2 * dp[i - 2])
            
        return dp[n]

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.integerBreak(n))