Synthesizing 10/10 solutions

=======
Suggestion 1

def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if not s:
        return 0
    count = 1
    dp = [0]*26
    dp[ord(s[0])-ord('a')] = 1
    for i in range(1,len(s)):
        if ord(s[i])-ord(s[i-1]) == 1 or (s[i] == 'a' and s[i-1] == 'z'):
            count += 1
        else:
            count = 1
        dp[ord(s[i])-ord('a')] = max(dp[ord(s[i])-ord('a')],count)
    return sum(dp)

print(findSubstringInWraproundString('a'))
print(findSubstringInWraproundString('cac'))
print(findSubstringInWraproundString('zab'))
print(findSubstringInWraproundString('zabcdefghijk'))

=======
Suggestion 2

def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if not s:
        return 0
    if len(s) == 1:
        return 1
    dp = [0] * 26
    dp[ord(s[0]) - ord('a')] = 1
    cur_len = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i - 1]) == 1 or (s[i] == 'a' and s[i - 1] == 'z'):
            cur_len += 1
        else:
            cur_len = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], cur_len)
    return sum(dp)

print(findSubstringInWraproundString("zab"))
print(findSubstringInWraproundString("cac"))
print(findSubstringInWraproundString("a"))
print(findSubstringInWraproundString("zaba"))
print(findSubstringInWraproundString("zabaz"))
print(findSubstringInWraproundString("zabazab"))
print(findSubstringInWraproundString("zabazaba"))
print(findSubstringInWraproundString("zabazabaz"))
print(findSubstringInWraproundString("zabazabaza"))
print(findSubstringInWraproundString("zabazabazab"))
print(findSubstringInWraproundString("zabazabazaba"))
print(findSubstringInWraproundString("zabazabazabaz"))
print(findSubstringInWraproundString("zabazabazabaza"))
print(findSubstringInWraproundString("zabazabazabazab"))
print(findSubstringInWraproundString("zabazabazabazaba"))
print(findSubstringInWraproundString("zabazabazabazabaz"))
print(findSubstringInWraproundString("zabazabazabazabaza"))
print(findSubstringInWraproundString("zabazabazabazabazab"))
print(findSubstringInWraproundString("zabazabazabazabazaba"))
print(findSubstringInWraproundString("zabazabazabazabazabaz"))
print(findSubstringInWraproundString("zabazabazabazabazabaza"))

=======
Suggestion 3

def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if len(s) <= 1:
        return len(s)
    dp = [0] * 26
    dp[ord(s[0]) - ord('a')] = 1
    count = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i - 1]) == 1 or (s[i] == 'a' and s[i - 1] == 'z'):
            count += 1
        else:
            count = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
    return sum(dp)

print(findSubstringInWraproundString("zab"))

=======
Suggestion 4

def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if not s:
        return 0
    
    length = len(s)
    dp = [0] * 26
    dp[ord(s[0]) - ord('a')] = 1
    count = 1
    
    for i in range(1, length):
        if ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i]) - ord(s[i - 1]) == -25:
            count += 1
        else:
            count = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
    
    return sum(dp)

print(findSubstringInWraproundString("zab"))

=======
Suggestion 5

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

=======
Suggestion 6

def unique_substrings_in_wraparound_string(s):
    """
    :type s: str
    :rtype: int
    """
    count = [0] * 26
    max_len = 0
    for i in range(len(s)):
        if i > 0 and (ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i - 1]) - ord(s[i]) == 25):
            max_len += 1
        else:
            max_len = 1
        count[ord(s[i]) - ord('a')] = max(count[ord(s[i]) - ord('a')], max_len)
    return sum(count)
    
print(unique_substrings_in_wraparound_string('zab'))
print(unique_substrings_in_wraparound_string('cac'))
print(unique_substrings_in_wraparound_string('a'))

=======
Suggestion 7

def uniqueSubstringInWraparoundString(s):
    """
    :type p: str
    :rtype: int
    """
    if not s:
        return 0

    # Initialize the count of all unique substrings end with letter 'a', 'b', ..., 'z'.
    # Use array instead of dictionary to make it run faster.
    count = [0] * 26

    # Store longest contiguous substring ends at current position.
    maxLengthCur = 0

    for i in range(len(s)):
        # Check if the current character is continuation of s[i - 1]
        if i > 0 and (ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i - 1]) - ord(s[i]) == 25):
            maxLengthCur += 1
        else:
            maxLengthCur = 1

        # Get the index of current character, e.g. 'a' -> 0, 'z' -> 25.
        index = ord(s[i]) - ord('a')
        count[index] = max(count[index], maxLengthCur)

    # Sum to get result
    return sum(count)

=======
Suggestion 8

def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if len(s) == 1:
        return 1
    if len(s) == 0:
        return 0
    base = 'abcdefghijklmnopqrstuvwxyz'
    temp = s[0]
    result = 0
    for i in range(1, len(s)):
        if s[i] in base[base.index(temp[-1])+1:]:
            temp += s[i]
        else:
            temp = s[i]
        result = max(result, len(temp))
    return result

print(findSubstringInWraproundString('a'))
print(findSubstringInWraproundString('cac'))
print(findSubstringInWraproundString('zab'))

=======
Suggestion 9

def findSubstringInWraproundString(s: str) -> int:
    if not s:
        return 0
    dp = [0] * 26
    dp[ord(s[0]) - ord('a')] = 1
    count = 1
    for i in range(1, len(s)):
        if (ord(s[i]) - ord(s[i - 1]) == 1) or (ord(s[i]) - ord(s[i - 1]) == -25):
            count += 1
        else:
            count = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
    return sum(dp)

print(findSubstringInWraproundString("zab"))

=======
Suggestion 10

def unique_substrings_in_wraparound_string(s):
    """
    :type s: str
    :rtype: int
    """
    res = 0
    count = [0] * 26
    for i in range(len(s)):
        if i > 0 and (ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25):
            res += 1
        else:
            res = 1
        count[ord(s[i]) - ord('a')] = max(count[ord(s[i]) - ord('a')], res)
    return sum(count)
