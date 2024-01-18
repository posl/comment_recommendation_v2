class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # DP
        # dp[i][j] = sのi番目までの文字列からtのj番目までの文字列を作る方法の数
        # dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i] == t[j]
        #          = dp[i-1][j] if s[i] != t[j]
        m, n = len(s), len(t)
        # dp = [[0] * (n + 1) for _ in range(m + 1)]
        # for i in range(m + 1):
        #     dp[i][0] = 1
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if s[i - 1] == t[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        #         else:
        #             dp[i][j] = dp[i - 1][j]
        # return dp[m][n]
        # dp = [1] * (n + 1)
        # for i in range(1, m + 1):
        #     prev = 1
        #     for j in range(1, n + 1):
        #         tmp = dp[j]
        #         if s[i - 1] == t[j - 1]:
        #             dp[j] += prev
        #         prev = tmp
        # return dp[n]
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, m + 1):
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[n]

if __name__ == '__main__':
    s = input()
    t = input()
    a = Solution()
    print(a.numDistinct(s, t))