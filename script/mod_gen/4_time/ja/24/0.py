class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] := Sのi文字目までとTのj文字目までの部分列の数
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        # dp[0][0] = 1
        dp[0][0] = 1
        for i in range(len(s)):
            for j in range(len(t) + 1):
                # Sのi文字目を使わない場合
                dp[i + 1][j] += dp[i][j]
                # Sのi文字目を使う場合
                if j < len(t) and s[i] == t[j]:
                    dp[i + 1][j + 1] += dp[i][j]
        return dp[-1][-1]

if __name__ == '__main__':
    s = input()
    t = input()
    a = Solution()
    print(a.numDistinct(s, t))