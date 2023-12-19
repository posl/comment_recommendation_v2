Synthesizing 10/10 solutions

=======
Suggestion 1

def numDistinct(s,t):
    dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
    for i in range(len(s)+1):
        dp[i][0] = 1
    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

print(numDistinct("rabbbit","rabbit"))
print(numDistinct("babgbag","bag"))
print(numDistinct("abcd","abcd"))
print(numDistinct("abcd","abc"))
print(numDistinct("abcd","ab"))
print(numDistinct("abcd","a"))
print(numDistinct("abcd",""))
print(numDistinct("","a"))
print(numDistinct("",""))
print(numDistinct("babgbag","babgbag"))
print(numDistinct("babgbag","babgbagb"))
print(numDistinct("babgbag","babgbagbb"))
print(numDistinct("babgbag","babgbagbbb"))
print(numDistinct("babgbag","babgbagbbbb"))
print(numDistinct("babgbag","babgbagbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbbbbbbbbbbbb"))

=======
Suggestion 2

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
            if t[i-1] == s[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[-1][-1]

=======
Suggestion 3

def numDistinct(s: str, t: str) -> int:
    # Time Complexity: O(s*t)
    # Space Complexity: O(s*t)
    n = len(s)
    m = len(t)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][m]

=======
Suggestion 4

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    # dp[i][j] is the number of distinct subsequences of s[:i] which equals t[:j]
    # dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i-1] == t[j-1]
    #          = dp[i-1][j] if s[i-1] != t[j-1]
    # dp[0][0] = 1, dp[i][0] = 1, dp[0][j] = 0 for all i, j
    m, n = len(s), len(t)
    dp = [[1] + [0] * n for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[m][n]

=======
Suggestion 5

def numDistinct(s, t):
    dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    for i in range(len(s)+1):
        dp[i][0] = 1
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

=======
Suggestion 6

def numDistinct(s: str, t: str) -> int:
    dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    for i in range(len(s)+1):
        dp[i][0] = 1
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
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
    #Solution 1
    # if not s:
    #     return 0
    # if not t:
    #     return 1
    # if len(s) < len(t):
    #     return 0
    # if s == t:
    #     return 1
    # if s[0] == t[0]:
    #     return numDistinct(s[1:], t[1:]) + numDistinct(s[1:], t)
    # else:
    #     return numDistinct(s[1:], t)
    
    #Solution 2
    # if not s:
    #     return 0
    # if not t:
    #     return 1
    # if len(s) < len(t):
    #     return 0
    # if s == t:
    #     return 1
    # if s[0] == t[0]:
    #     return numDistinct(s[1:], t[1:]) + numDistinct(s[1:], t)
    # else:
    #     return numDistinct(s[1:], t)
    
    #Solution 3
    # if len(s) < len(t):
    #     return 0
    # if not t:
    #     return 1
    # if not s:
    #     return 0
    # if s == t:
    #     return 1
    # if s[0] == t[0]:
    #     return numDistinct(s[1:], t[1:]) + numDistinct(s[1:], t)
    # else:
    #     return numDistinct(s[1:], t)
    
    #Solution 4
    # if len(s) < len(t):
    #     return 0
    # if not t:
    #     return 1
    # if not s:
    #     return 0
    # if s == t:
    #     return 1
    # if s[0] == t[0]:
    #     return numDistinct(s[1:], t[1:]) + numDistinct(s[1:], t)
    # else:
    #     return numDistinct(s[1:], t)
    
    #Solution 5
    # if len

=======
Suggestion 8

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    #if s == t:
    #    return 1
    #if len(s) < len(t):
    #    return 0
    #if len(t) == 0:
    #    return 1
    #if len(s) == 0:
    #    return 0
    #if s[0] == t[0]:
    #    return numDistinct(s[1:], t[1:]) + numDistinct(s[1:], t)
    #else:
    #    return numDistinct(s[1:], t)
    #dp = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
    #for i in range(len(s)+1):
    #    dp[0][i] = 1
    #for i in range(1, len(t)+1):
    #    for j in range(1, len(s)+1):
    #        if t[i-1] == s[j-1]:
    #            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    #        else:
    #            dp[i][j] = dp[i][j-1]
    #return dp[-1][-1]
    dp = [0 for _ in range(len(t)+1)]
    dp[0] = 1
    for i in range(1, len(s)+1):
        for j in range(len(t), 0, -1):
            if s[i-1] == t[j-1]:
                dp[j] += dp[j-1]
    return dp[-1]

=======
Suggestion 9

def numDistinct(s: str, t: str) -> int:
    if len(s) == 0 or len(t) == 0:
        return 0
    if len(s) < len(t):
        return 0
    if len(s) == len(t):
        if s == t:
            return 1
        else:
            return 0
    dp = [[0 for _ in range(len(s))] for _ in range(len(t))]
    for i in range(len(t)):
        for j in range(len(s)):
            if t[i] == s[j]:
                if i == 0:
                    if j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i][j - 1] + 1
                else:
                    if j == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
            else:
                if j == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j - 1]
    return dp[len(t) - 1][len(s) - 1]

s = "rabbbit"
t = "rabbit"
print(numDistinct(s, t))

s = "babgbag"
t = "bag"
print(numDistinct(s, t))

s = "babgbag"
t = "bag"
print(numDistinct(s, t))

s

=======
Suggestion 10

def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    # dp[i][j] is the number of distinct subsequences of s[:i] which equals t[:j]
    # dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i-1] == t[j-1]
    # dp[i][j] = dp[i-1][j] if s[i-1] != t[j-1]
    # dp[0][j] = 0 for all j
    # dp[i][0] = 1 for all i
    # return dp[-1][-1]
    # dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    # for i in range(len(s)+1):
    #     dp[i][0] = 1
    # for i in range(1, len(s)+1):
    #     for j in range(1, len(t)+1):
    #         if s[i-1] == t[j-1]:
    #             dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    #         else:
    #             dp[i][j] = dp[i-1][j]
    # return dp[-1][-1]
    dp = [0 for _ in range(len(t)+1)]
    dp[0] = 1
    for i in range(1, len(s)+1):
        for j in range(len(t), 0, -1):
            if s[i-1] == t[j-1]:
                dp[j] = dp[j-1] + dp[j]
    return dp[-1]

print(numDistinct("rabbbit", "rabbit"))
print(numDistinct("babgbag", "bag"))
print(numDistinct("babgbag", "bag"))
print(num
