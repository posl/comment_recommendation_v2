class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 10
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + (dp[i-1]-dp[i-2])*(11-i)
        
        return dp[-1]

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.countNumbersWithUniqueDigits(n))