def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    # 0. base case
    if len(s) == 0:
        return 0
    # 1. init
    dp = [0] * 26
    dp[ord(s[0]) - ord('a')] = 1
    count = 1
    # 2. loop
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i]) - ord(s[i-1]) == -25:
            count += 1
        else:
            count = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
    # 3. return
    return sum(dp)

if __name__ == '__main__':
    findSubstringInWraproundString()