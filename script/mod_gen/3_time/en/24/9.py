def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    if len(s) < len(t):
        return 0
    # Initialize a 2D array of size (len(t) + 1) * (len(s) + 1)
    # dp[i][j] represents the number of distinct subsequences of s[:j] which equals t[:i]
    dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]
    # Initialize the first row with 1s
    # This is because when t is empty, the empty string is a subsequence of s
    for j in range(len(s) + 1):
        dp[0][j] = 1
    # Iterate through the 2D array
    for i in range(1, len(t) + 1):
        for j in range(1, len(s) + 1):
            # If the last characters of s[:j] and t[:i] are equal,
            # we can choose to include or exclude the last character of s[:j]
            # If we include the last character, the number of distinct subsequences is dp[i - 1][j - 1]
            # If we exclude the last character, the number of distinct subsequences is dp[i][j - 1]
            # Therefore, dp[i][j] is the sum of the above two values
            if s[j - 1] == t[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            # If the last characters of s[:j] and t[:i] are not equal,
            # we can only exclude the last character of s[:j]
            # Therefore, dp[i][j] is the same as dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]
    # The answer is dp[-1][-1]
    return dp[-1][-1]

if __name__ == '__main__':
    numDistinct()