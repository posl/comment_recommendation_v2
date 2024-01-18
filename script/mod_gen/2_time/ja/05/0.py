class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        dp = [0]*26
        cnt = 1
        dp[ord(s[0])-ord('a')] = 1
        for i in range(1, len(s)):
            if ord(s[i])-ord(s[i-1])==1 or ord(s[i-1])-ord(s[i])==25:
                cnt += 1
            else:
                cnt = 1
            dp[ord(s[i])-ord('a')] = max(dp[ord(s[i])-ord('a')], cnt)
        return sum(dp)

if __name__ == '__main__':
    s = input()
    a = Solution()
    print(a.findSubstringInWraproundString(s))