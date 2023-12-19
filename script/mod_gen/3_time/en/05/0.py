def unique_substrings_in_wraparound_string(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    dp = [0] * 26
    dp[ord(s[0]) - ord('a')] = 1
    length = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i - 1]) - ord(s[i]) == 25:
            length += 1
        else:
            length = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], length)
    return sum(dp)

if __name__ == '__main__':
    unique_substrings_in_wraparound_string()