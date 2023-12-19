Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    
    count = [0] * 26
    count[ord(s[0]) - ord('a')] = 1
    maxLen = 1
    
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25:
            maxLen += 1
        else:
            maxLen = 1
        count[ord(s[i]) - ord('a')] = max(count[ord(s[i]) - ord('a')], maxLen)
    
    return sum(count)

=======
Suggestion 3

def findSubstringInWraproundString(s: str) -> int:
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    res = 0
    counter = [0]*26
    counter[ord(s[0])-ord('a')] = 1
    length = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1 or (ord(s[i]) - ord(s[i-1]) == -25 and s[i] == 'a'):
            length += 1
        else:
            length = 1
        counter[ord(s[i])-ord('a')] = max(counter[ord(s[i])-ord('a')], length)
    return sum(counter)

=======
Suggestion 4

def findSubstringInWraproundString(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0

    prev = s[0]
    curr = 1
    count = 0
    for i in range(1, len(s)):
        if ord(s[i]) - ord(prev) == 1 or (s[i] == "a" and prev == "z"):
            curr += 1
        else:
            curr = 1
        count += curr
        prev = s[i]
    return count

print(findSubstringInWraproundString("a"))
print(findSubstringInWraproundString("cac"))
print(findSubstringInWraproundString("zab"))
print(findSubstringInWraproundString("zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd"))

=======
Suggestion 5

def uniqueSubstringsInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    dp = [0] * 26
    dp[ord(s[0]) - ord('a')] = 1
    currentMax = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1 or (ord(s[i]) - ord(s[i-1]) == -25 and s[i] != 'a'):
            currentMax += 1
        else:
            currentMax = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], currentMax)
    return sum(dp)

print(uniqueSubstringsInWraproundString("zab"))
print(uniqueSubstringsInWraproundString("cac"))
print(uniqueSubstringsInWraproundString("a"))
print(uniqueSubstringsInWraproundString("zababc"))
print(uniqueSubstringsInWraproundString("zababca"))
print(uniqueSubstringsInWraproundString("zababcab"))
print(uniqueSubstringsInWraproundString("zababcabc"))
print(uniqueSubstringsInWraproundString("zababcabca"))
print(uniqueSubstringsInWraproundString("zababcabcab"))
print(uniqueSubstringsInWraproundString("zababcabcabc"))
print(uniqueSubstringsInWraproundString("zababcabcabca"))
print(uniqueSubstringsInWraproundString("zababcabcabcab"))
print(uniqueSubstringsInWraproundString("zababcabcabcabc"))
print(uniqueSubstringsInWraproundString("zababcabcabcabca"))
print(uniqueSubstringsInWraproundString("zababcabcabcabcab"))
print(uniqueSubstringsInWraproundString("zababcabcabcabcabc"))
print(uniqueSubstringsInWraproundString("zababcabcabcabcabca"))
print(uniqueSubstringsInWraproundString("zababcabcabcabcabcab"))
print(uniqueSubstringsInWraproundString("zababcabcabcabcabcabc"))
print(uniqueSubstringsInWraproundString("zababcabcabcabcabcabca"))
print(uniqueSubstringsInWraproundString("zababcabcabcabcabcabcab

=======
Suggestion 6

def unique_substrings_in_wraparound_string(s):
    """
    :type p: str
    :type s: str
    :rtype: List[int]
    """
    #https://leetcode.com/problems/unique-substrings-in-wraparound-string/
    #https://leetcode.com/problems/unique-substrings-in-wraparound-string/discuss/95439/Concise-Java-solution-using-DP
    #https://leetcode.com/problems/unique-substrings-in-wraparound-string/discuss/95439/Concise-Java-solution-using-DP/99734
    #https://leetcode.com/problems/unique-substrings-in-wraparound-string/discuss/95439/Concise-Java-solution-using-DP/99734
    #https://leetcode.com/problems/unique-substrings-in-wraparound-string/discuss/95439/Concise-Java-solution-using-DP/99734
    #https://leetcode.com/problems/unique-substrings-in-wraparound-string/discuss/95439/Concise-Java-solution-using-DP/99734
    #https://leetcode.com/problems/unique-substrings-in-wraparound-string/discuss/95439/Concise-Java-solution-using-DP/99734
    #https://leetcode.com/problems/unique-substrings-in-wraparound-string/discuss/95439/Concise-Java-solution-using-DP/99734
    #https://leetcode.com/problems/unique-substrings-in-wraparound-string/discuss/95439/Concise-Java-solution-using-DP/99734
    #https://leetcode.com/problems/unique-substrings-in-wraparound-string/discuss/95439/Concise-Java-solution-using-DP/99734
    #https://leetcode.com/problems/unique-substrings-in-wraparound-string/discuss/95439/Concise-Java-solution-using-DP/99734
    
    #https://leetcode.com/problems/unique-substrings-in-wraparound-string/discuss/95439/Concise-Java-solution-using-DP/99734
    #https://leetcode.com/problems/unique-substrings-in-wraparound-string/discuss/95439/Concise-Java-solution-using-DP/99734
    #https://leetcode.com/problems/unique-substrings-in-wraparound-string/discuss/95439/Concise-Java-solution-using-DP/997

=======
Suggestion 7

def uniqueSubstringInWraparoundString(s):
    """
    :type p: str
    :rtype: int
    """
    # Solution 1:
    # if len(s) <= 1:
    #     return len(s)
    # base = 'abcdefghijklmnopqrstuvwxyz'
    # base += base
    # count = 1
    # for i in range(1, len(s)):
    #     if base.find(s[i-1:i+1]) != -1:
    #         count += 1
    # return count
    # Solution 2:
    if len(s) <= 1:
        return len(s)
    count = [0 for _ in range(26)]
    count[ord(s[0]) - ord('a')] = 1
    maxLength = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i]) - ord(s[i-1]) == -25:
            maxLength += 1
        else:
            maxLength = 1
        count[ord(s[i]) - ord('a')] = max(count[ord(s[i]) - ord('a')], maxLength)
    return sum(count)

print(uniqueSubstringInWraparoundString('zab'))
print(uniqueSubstringInWraparoundString('a'))
print(uniqueSubstringInWraparoundString('cac'))
print(uniqueSubstringInWraparoundString('zabcde'))
print(uniqueSubstringInWraparoundString('abcde'))
print(uniqueSubstringInWraparoundString('zabzabcde'))
print(uniqueSubstringInWraparoundString('zabzabcdeabcde'))
print(uniqueSubstringInWraparoundString('zabzabcdeabcdeabcdeabcde'))
print(uniqueSubstringInWraparoundString('zabzabcdeabcdeabcdeabcdeabcde'))
# Output:
# 6
# 1
# 2
# 5
# 5
# 7
# 10
# 15
# 21

=======
Suggestion 8

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

=======
Suggestion 9

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
    count = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i]) - ord(s[i - 1]) == -25:
            count += 1
        else:
            count = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
    return sum(dp)

print(findSubstringInWraproundString("zab"))
print(findSubstringInWraproundString("cac"))
print(findSubstringInWraproundString("a"))
print(findSubstringInWraproundString("zaba"))
print(findSubstringInWraproundString("zabca"))
print(findSubstringInWraproundString("zabcad"))
print(findSubstringInWraproundString("zabcade"))
print(findSubstringInWraproundString("zabcadef"))
print(findSubstringInWraproundString("zabcadefg"))
print(findSubstringInWraproundString("zabcadefgh"))
print(findSubstringInWraproundString("zabcadefghi"))
print(findSubstringInWraproundString("zabcadefghij"))
print(findSubstringInWraproundString("zabcadefghijk"))
print(findSubstringInWraproundString("zabcadefghijkl"))
print(findSubstringInWraproundString("zabcadefghijklm"))
print(findSubstringInWraproundString("zabcadefghijklmn"))
print(findSubstringInWraproundString("zabcadefghijklmno"))
print(findSubstringInWraproundString("zabcadefghijklmnop"))
print(findSubstringInWraproundString("zabcadefghijklmnopq"))
print(findSubstringInWraproundString("zabcadefghijklmnopqr"))
print(findSubstringInWraproundString("zabcadefghijklmnopqrs"))
print(findSubstringInWraproundString("zabcadefghijklmnopqrst"))
print(findSubstringInWraproundString("zabcadefgh

=======
Suggestion 10

def unique_substrings_in_wraparound_string(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    if n == 0:
        return 0
    count = [0] * 26
    count[ord(s[0]) - ord('a')] = 1
    result = 1
    for i in range(1, n):
        if ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i]) - ord(s[i - 1]) == -25:
            result += 1
        else:
            result = 1
        count[ord(s[i]) - ord('a')] = max(count[ord(s[i]) - ord('a')], result)
    return sum(count)
