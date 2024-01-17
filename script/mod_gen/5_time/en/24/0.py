class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        dp=[[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            dp[i][0]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(s[i-1]==t[j-1]):
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return(dp[m][n])

if __name__ == '__main__':
    s = input()
    t = input()
    a = Solution()
    print(a.numDistinct(s, t))