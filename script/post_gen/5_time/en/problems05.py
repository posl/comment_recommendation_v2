Synthesizing 10/10 solutions

=======
Suggestion 1

def unique_substring(s):
    if s == None or len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    count = 0
    for i in range(len(s)):
        count += 1
        for j in range(i+1, len(s)):
            if ord(s[j])-ord(s[j-1]) == 1 or ord(s[j])-ord(s[j-1]) == -25:
                count += 1
            else:
                break
    return count

print(unique_substring("zab"))
print(unique_substring("cac"))
print(unique_substring("a"))
print(unique_substring("zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd"))
print(unique_substring("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijkl

=======
Suggestion 2

def uniqueSubstringsInWraparoundString(s):
    """
    :type p: str
    :rtype: int
    """
    if not s:
        return 0
    count = 0
    length = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i - 1]) == 1 or (s[i] == 'a' and s[i - 1] == 'z'):
            length += 1
        else:
            count += length * (length + 1) // 2
            length = 1
    count += length * (length + 1) // 2
    return count

print(uniqueSubstringsInWraparoundString("zab"))

=======
Suggestion 3

def uniqueSubstringsInWraparoundString(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) <= 1:
        return len(s)
    dp = [0] * 26
    dp[ord(s[0]) - ord('a')] = 1
    count = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i - 1]) == 1 or (ord(s[i]) - ord(s[i - 1]) == -25 and s[i] == 'a'):
            count += 1
        else:
            count = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
    return sum(dp)

s = "zab"
print(uniqueSubstringsInWraparoundString(s))

=======
Suggestion 4

def uniqueSubstringInWraproundString(s):
    """
    :type s: str
    :rtype: int
    """
    # initialize an array of length 26 to record the max length of substring ends with each character
    # of 'a' to 'z'
    # for example, count[0] is the max length of substring ends with 'a'
    # count[1] is the max length of substring ends with 'b'
    # ...
    # count[25] is the max length of substring ends with 'z'
    count = [0] * 26
    # store the max length of substring
    maxLength = 0
    for i in range(len(s)):
        # if the current character is the same as the previous character or
        # the current character is 'a' and the previous character is 'z',
        # the current character can be appended to the previous substring
        if i > 0 and (ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i - 1]) - ord(s[i]) == 25):
            maxLength += 1
        # otherwise, the current character can only be a new substring
        else:
            maxLength = 1
        # update the max length of substring ends with the current character
        count[ord(s[i]) - ord('a')] = max(count[ord(s[i]) - ord('a')], maxLength)
    # return the sum of the max length of substring ends with each character
    return sum(count)

=======
Suggestion 5

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

=======
Suggestion 6

def unique_substrings_in_wraparound_string(s):
    if not s:
        return 0
    if len(s) == 1:
        return 1
    result = 0
    curr = 0
    count = [0] * 26
    for i in range(len(s)):
        curr = ord(s[i]) - ord('a')
        if i > 0 and ord(s[i - 1]) != (curr - 1) % 26 + ord('a'):
            count[curr] = 0
        count[curr] = max(count[curr], 1)
        result = max(result, count[curr])
    return result

print(unique_substrings_in_wraparound_string("zab"))
print(unique_substrings_in_wraparound_string("cac"))
print(unique_substrings_in_wraparound_string("a"))
print(unique_substrings_in_wraparound_string("zabzabc"))
print(unique_substrings_in_wraparound_string("zabzabzab"))
print(unique_substrings_in_wraparound_string("zabzabzaba"))
print(unique_substrings_in_wraparound_string("zabzabzabaz"))
print(unique_substrings_in_wraparound_string("zabzabzabaza"))
print(unique_substrings_in_wraparound_string("zabzabzabazab"))
print(unique_substrings_in_wraparound_string("zabzabzabazaba"))
print(unique_substrings_in_wraparound_string("zabzabzabazabaz"))
print(unique_substrings_in_wraparound_string("zabzabzabazabaza"))
print(unique_substrings_in_wraparound_string("zabzabzabazabazab"))
print(unique_substrings_in_wraparound_string("zabzabzabazabazaba"))
print(unique_substrings_in_wraparound_string("zabzabzabazabazabaz"))
print(unique_substrings_in_wraparound_string("zabzabzabazabazabaza"))
print(unique_substrings_in_wraparound_string("zabzabzabazabazabazab"))
print(unique_substrings_in_wraparound_string("zabzabzabazabazabazaba"))
print(unique_substrings_in_wraparound_string("zabzabzabazabazabazabaz"))
print(unique_substrings_in_wraparound_string("zabzabzabazabazabazabaza"))
print(unique_sub

=======
Suggestion 7

def uniqueSubstringsInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if not s:
        return 0
    s = list(s)
    count = 0
    s[0] = ord(s[0]) - ord('a')
    for i in range(1,len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1 or (s[i] == 'a' and s[i-1] == 'z'):
            s[i] = s[i-1] + 1
        else:
            s[i] = ord(s[i]) - ord('a')
    temp = [0]*26
    for i in range(len(s)):
        if temp[s[i]] == 0:
            temp[s[i]] = 1
            count += 1
        for j in range(i+1,len(s)):
            if s[j] - s[j-1] == 1 or (s[j] == 0 and s[j-1] == 25):
                if temp[s[j]] == 0:
                    temp[s[j]] = 1
                    count += 1
            else:
                break
    return count

print(uniqueSubstringsInWraproundString("zaba"))
print(uniqueSubstringsInWraproundString("zab"))
print(uniqueSubstringsInWraproundString("cac"))
print(uniqueSubstringsInWraproundString("a"))
print(uniqueSubstringsInWraproundString("z"))

=======
Suggestion 8

def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    d = {}
    i = 0
    while i < len(s):
        j = i + 1
        while j < len(s) and (ord(s[j]) - ord(s[j - 1]) == 1 or ord(s[j]) - ord(s[j - 1]) == -25):
            j += 1
        for k in range(i, j):
            if s[k] not in d:
                d[s[k]] = j - k
            else:
                d[s[k]] = max(d[s[k]], j - k)
        i = j
    return sum(d.values())

print(findSubstringInWraproundString("zab"))

=======
Suggestion 9

def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    dp = [0] * 26
    dp[ord(s[0]) - ord('a')] = 1
    count = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25:
            count += 1
        else:
            count = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
    return sum(dp)

print(findSubstringInWraproundString("zab"))
print(findSubstringInWraproundString("cac"))
print(findSubstringInWraproundString("a"))
print(findSubstringInWraproundString("ab"))
print(findSubstringInWraproundString("abc"))
print(findSubstringInWraproundString("zabcd"))

=======
Suggestion 10

def findSubstringInWraproundString(s: str) -> int:
    if len(s) == 1:
        return 1
    count = 0
    for i in range(len(s)):
        j = i + 1
        while j < len(s) and (ord(s[j]) - ord(s[j - 1]) == 1 or ord(s[j - 1]) - ord(s[j]) == 25):
            j += 1
        count += (j - i) * (j - i + 1) // 2
        i = j - 1
    return count

print(findSubstringInWraproundString("zab"))
