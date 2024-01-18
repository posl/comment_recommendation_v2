class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        # dp[i] := s[i]で終わる最長の部分文字列の長さ
        dp = [0] * 26
        # 最初の文字は1文字の文字列であるから、dp[0] = 1
        dp[ord(s[0]) - ord('a')] = 1
        # 今までに登場した部分文字列を管理するためのセット
        substrings = set(s[0])
        # 答え
        ans = 1
        # sの各文字について
        for i in range(1, len(s)):
            # s[i]で終わる最長の部分文字列の長さを求める
            if s[i - 1] == 'z' and s[i] == 'a':
                # 文字列が循環しているため、s[i - 1] == 'z'かつs[i] == 'a'のとき、
                # s[i]で終わる最長の部分文字列の長さは1
                dp[0] = 1
            elif ord(s[i - 1]) + 1 == ord(s[i]):
                # s[i - 1]とs[i]が隣り合う文字のとき、
                # s[i]で終わる最長の部分文字列の長さはs[i - 1]で終わる最長の部分文字列の長さ + 1
                dp[ord(s[i]) - ord('a')] = dp[ord(s[i - 1]) - ord('a')] + 1
            else:
                # それ以外のとき、s[i]で終わる最長の部分文字列の長さは1
                dp[ord(s[i]) - ord('a')] = 1
            # s[i]で終わる最長の部分文字列をセットに追加する
            substrings.add(s[i - dp[ord(s[i]) - ord('a')]:i + 1])
            # 答

if __name__ == '__main__':
    s = input()
    a = Solution()
    print(a.findSubstringInWraproundString(s))