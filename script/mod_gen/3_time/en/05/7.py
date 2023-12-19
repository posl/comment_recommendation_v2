def findSubstringInWraproundString(s):
	"""
	:type s: str
	:rtype: int
	"""
	if not s:
		return 0
	res = 1
	dp = [0] * 26
	dp[ord(s[0]) - ord('a')] = 1
	maxLen = 1
	for i in range(1, len(s)):
		if ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i]) - ord(s[i - 1]) == -25:
			maxLen += 1
		else:
			maxLen = 1
		dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], maxLen)
	for i in range(26):
		res += dp[i]
	return res

if __name__ == '__main__':
    findSubstringInWraproundString()