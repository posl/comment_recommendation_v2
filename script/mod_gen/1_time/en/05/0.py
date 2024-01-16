class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        # dp[i] = max length of substring ends at i
        dp = [0] * len(s)
        dp[0] = 1
        # count[i] = max number of unique substrings ends at i
        count = [0] * len(s)
        count[0] = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i - 1]) == 1 or (ord(s[i]) == 97 and ord(s[i - 1]) == 122):
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1
            count[i] = max(count[i - 1], dp[i])
        return sum(count)

if __name__ == '__main__':
    s = input()
    a = Solution()
    print(a.findSubstringInWraproundString(s))