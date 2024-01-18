class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #dp[i][j] = sのi文字目までの部分列のうち、tのj文字目までの部分列と一致するものの数
        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1] == t[j-1]:
                    #sのi文字目とtのj文字目が一致する場合
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    #sのi文字目とtのj文字目が一致しない場合
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

if __name__ == '__main__':
    s = input()
    t = input()
    a = Solution()
    print(a.numDistinct(s, t))