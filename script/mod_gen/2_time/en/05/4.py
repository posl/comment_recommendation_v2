def unique_substrings_in_wraparound_string(s):
    """
    :type s: str
    :rtype: int
    """
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    # Explanation: We can use dynamic programming to solve this problem.
    # Let dp[i] be the number of unique substrings in s that ends with letter chr(i).
    # We can see that dp[i] = 1 + dp[i-1] if s[i] - s[i-1] = 1 or -25,
    # otherwise dp[i] = 1.
    # Finally, we return the sum of dp[i] for i in range(26).
    dp = [0] * 26
    count = 0
    for i in range(len(s)):
        if i > 0 and (ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i]) - ord(s[i-1]) == -25):
            count += 1
        else:
            count = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
    return sum(dp)

if __name__ == '__main__':
    unique_substrings_in_wraparound_string()