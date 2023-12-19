Synthesizing 10/10 solutions

=======
Suggestion 1

def numDistinct(s, t):
    m = len(s)
    n = len(t)
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[m][n]

print(numDistinct("rabbbit", "rabbit"))
print(numDistinct("babgbag", "bag"))
print(numDistinct("babgbag", "bagg"))
print(numDistinct("babgbag", "babg"))
print(numDistinct("babgbag", "bbg"))
print(numDistinct("babgbag", "bb"))
print(numDistinct("babgbag", "b"))
print(numDistinct("babgbag", "a"))
print(numDistinct("babgbag", "bbbbb"))
print(numDistinct("babgbag", "bbbb"))
print(numDistinct("babgbag", "bbbbbbbb"))
print(numDistinct("babgbag", "bbbbbbbb

=======
Suggestion 2

def distinctSubsequences(s, t):
    if len(s) < len(t):
        return 0
    elif len(s) == len(t):
        if s == t:
            return 1
        else:
            return 0
    else:
        i = 0
        count = 0
        while i < len(s):
            if s[i] == t[0]:
                count += distinctSubsequences(s[i+1:], t[1:])
            i += 1
        return count

=======
Suggestion 3

def distinctSubsequences(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]
    for j in range(len(s) + 1):
        dp[0][j] = 1

    for i in range(1, len(t) + 1):
        for j in range(1, len(s) + 1):
            if t[i-1] == s[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1]

    return dp[len(t)][len(s)]

=======
Suggestion 4

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]
    for j in range(len(s) + 1):
        dp[0][j] = 1
    for i in range(1, len(t) + 1):
        for j in range(1, len(s) + 1):
            if t[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]
    return dp[-1][-1]

=======
Suggestion 5

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    dp = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
    for i in range(len(s)+1):
        dp[0][i] = 1
    for i in range(1, len(t)+1):
        for j in range(1, len(s)+1):
            if s[j-1] == t[i-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[-1][-1]

=======
Suggestion 6

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    dp = [[0 for j in range(len(s)+1)] for i in range(len(t)+1)]
    for i in range(len(s)+1):
        dp[0][i] = 1
    for i in range(1,len(t)+1):
        for j in range(1,len(s)+1):
            if t[i-1] == s[j-1]:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[-1][-1]

print(numDistinct("rabbbit", "rabbit"))
print(numDistinct("babgbag", "bag"))
print(numDistinct("babgbag", "bag"))
print("The values above should be 3, 5, and 5.")

=======
Suggestion 7

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    if len(s) < len(t):
        return 0
    if len(t) == 0:
        return 1
    dp = [[0 for _ in range(len(t))] for _ in range(len(s))]
    # dp[i][j] stores the number of distinct subsequences of s[:i+1] which equals t[:j+1]
    if s[0] == t[0]:
        dp[0][0] = 1
    for i in range(1, len(s)):
        if s[i] == t[0]:
            dp[i][0] = dp[i-1][0] + 1
        else:
            dp[i][0] = dp[i-1][0]
    for j in range(1, len(t)):
        dp[j-1][j] = 0
        for i in range(j, len(s)):
            if s[i] == t[j]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

=======
Suggestion 8

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    m, n = len(s), len(t)
    dp = [[1] * (n + 1) for _ in range(m + 1)]
    for j in range(1, n + 1):
        dp[0][j] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j]
            if s[i - 1] == t[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]
    return dp[m][n]

=======
Suggestion 9

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
    for i in range(len(s) + 1):
        dp[i][0] = 1
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            dp[i][j] = dp[i - 1][j]
            if s[i - 1] == t[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]
    return dp[-1][-1]

=======
Suggestion 10

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
