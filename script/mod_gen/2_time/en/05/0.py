class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dp = [0]*26
        dp[ord(s[0])-ord('a')] = 1
        count = 1
        for i in range(1,len(s)):
            if ord(s[i])-ord(s[i-1]) == 1 or (s[i-1] == 'z' and s[i] == 'a'):
                count += 1
            else:
                count = 1
            dp[ord(s[i])-ord('a')] = max(dp[ord(s[i])-ord('a')],count)
        return sum(dp)

if __name__ == '__main__':
    s = input()
    a = Solution()
    print(a.findSubstringInWraproundString(s))