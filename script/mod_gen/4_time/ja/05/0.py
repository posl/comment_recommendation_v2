class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        def get_index(s):
            return ord(s) - ord('a')
        def get_char(i):
            return chr(i + ord('a'))
        # dp[i] = 以i文字目で終わる場合の最長の部分文字列の長さ
        dp = [0] * 26
        # dp[i] = max(dp[i], dp[i-1] + 1) if s[i] - s[i-1] = 1
        # dp[i] = 1 if s[i] - s[i-1] != 1
        # ただし、s[i] - s[i-1] = 1 は、s[i] = 'a' and s[i-1] = 'z'の場合も含む
        for i in range(len(s)):
            if i == 0:
                dp[get_index(s[i])] = 1
            else:
                if get_index(s[i]) - get_index(s[i-1]) == 1 or (s[i] == 'a' and s[i-1] == 'z'):
                    dp[get_index(s[i])] = max(dp[get_index(s[i])], dp[get_index(s[i-1])] + 1)
                else:
                    dp[get_index(s[i])] = max(dp[get_index(s[i])], 1)
        return sum(dp)

if __name__ == '__main__':
    s = input()
    a = Solution()
    print(a.findSubstringInWraproundString(s))