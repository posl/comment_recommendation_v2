Synthesizing 10/10 solutions

=======
Suggestion 1

def findSubstringInWraproundString(s: str) -> int:
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1

    d = dict()
    d[s[0]] = 1
    curr = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i]) - ord(s[i-1]) == -25:
            curr += 1
        else:
            curr = 1
        d[s[i]] = max(d.get(s[i], 0), curr)
    return sum(d.values())

print(findSubstringInWraproundString("zab"))
print(findSubstringInWraproundString("cac"))
print(findSubstringInWraproundString("a"))
print(findSubstringInWraproundString("zabaz"))
print(findSubstringInWraproundString("zaba"))

=======
Suggestion 2

def uniqueSubstringsInWraparoundString(s):
    """
    :type p: str
    :rtype: int
    """
    if not s:
        return 0
    if len(s) == 1:
        return 1
    dp = [0] * len(s)
    dp[0] = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1 or (s[i] == 'a' and s[i-1] == 'z'):
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 1
    return sum(dp)

=======
Suggestion 3

def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if len(s) == 0: return 0

    res = 1
    dp = [1] * 26

    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i]) - ord(s[i-1]) == -25:
            res += 1
        else:
            res = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], res)
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
    substr = set()
    i = 0
    while i < len(s):
        j = i + 1
        while j < len(s) and (ord(s[j]) - ord(s[j-1]) == 1 or ord(s[j-1]) - ord(s[j]) == 25):
            j += 1
        for k in range(i, j):
            for l in range(k, j):
                substr.add(s[k:l+1])
        i = j
    return len(substr)

=======
Suggestion 5

def uniqueSubstringsInWraparoundString(s):
    """
    :type p: str
    :rtype: int
    """
    if not s:
        return 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] in alphabet:
                count += 1
            else:
                break
    return count

print(uniqueSubstringsInWraparoundString("zab")) # 6
print(uniqueSubstringsInWraparoundString("cac")) # 2
print(uniqueSubstringsInWraparoundString("a")) # 1
print(uniqueSubstringsInWraparoundString("")) # 0
print(uniqueSubstringsInWraparoundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd")) # 26
print(uniqueSubstringsInWraparoundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcde")) # 26
print(uniqueSubstringsInWraparoundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdef")) # 26
print(uniqueSubstringsInWraparoundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg")) # 26
print(uniqueSubstringsInWraparoundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefgh")) # 26
print(uniqueSubstringsInWraparoundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghi")) # 26
print(uniqueSubstringsInWraparoundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghij")) # 26
print(uniqueSubstringsInWraparoundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijk")) # 26
print(uniqueSubstringsInWraparoundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijkl")) # 26
print(uniqueSubstringsInWraparoundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklm")) # 26
print(uniqueSubstringsInWraparoundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmn")) # 26
print(uniqueSubstringsInWraparoundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmno")) # 26
print(uniqueSubstringsInWraparoundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnop")) # 26
print(uniqueSubstringsInWraparoundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopq")) # 26
print(uniqueSubstringsInWraparoundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqr")) # 26
print(uniqueSubstringsInWraparoundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrs")) # 26
print(uniqueSubstringsInWraparoundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrst")) # 26
print(uniqueSubstringsInWraparoundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstu")) # 26
print(uniqueSubstringsInWraparoundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuv")) # 26
print(uniqueSubstringsIn

=======
Suggestion 6

def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if not s:
        return 0
    dp = [0]*26
    dp[ord(s[0])-ord('a')] = 1
    count = 1
    for i in range(1,len(s)):
        if ord(s[i])-ord(s[i-1])==1 or ord(s[i-1])-ord(s[i])==25:
            count += 1
        else:
            count = 1
        dp[ord(s[i])-ord('a')] = max(dp[ord(s[i])-ord('a')],count)
    return sum(dp)

print(findSubstringInWraproundString("zab"))
print(findSubstringInWraproundString("cac"))
print(findSubstringInWraproundString("a"))
print(findSubstringInWraproundString(""))

=======
Suggestion 7

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
        dp[ord(s[i]) - ord('a')] = max(count, dp[ord(s[i]) - ord('a')])
    return sum(dp)

print(findSubstringInWraproundString("a"))
print(findSubstringInWraproundString("cac"))
print(findSubstringInWraproundString("zab"))

=======
Suggestion 8

def findSubstringInWraproundString(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    if n <= 1:
        return n
    res = [0]*26
    res[ord(s[0])-ord('a')] = 1
    count = 1
    for i in range(1, n):
        if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i]) - ord(s[i-1]) == -25:
            count += 1
        else:
            count = 1
        res[ord(s[i])-ord('a')] = max(res[ord(s[i])-ord('a')], count)
    return sum(res)
    
print(findSubstringInWraproundString("zab"))

=======
Suggestion 9

def findSubstringInWraproundString(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    if len(s) == 2:
        if ord(s[1]) - ord(s[0]) == 1 or ord(s[1]) - ord(s[0]) == -25:
            return 3
        else:
            return 2

    dp = [0] * len(s)
    dp[0] = 1
    if ord(s[1]) - ord(s[0]) == 1 or ord(s[1]) - ord(s[0]) == -25:
        dp[1] = 3
    else:
        dp[1] = 2

    for i in range(2, len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i]) - ord(s[i-1]) == -25:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 1
        if ord(s[i]) - ord(s[i-1]) == 1 and dp[i-1] == 2:
            dp[i] += 1

    return sum(dp)

print(findSubstringInWraproundString("zab"))

=======
Suggestion 10

def unique_substring(s):
    #base = "abcdefghijklmnopqrstuvwxyz"
    #base = base * 2
    #print(base)
    #result = []
    #for i in range(len(s)):
    #    for j in range(i+1, len(s)+1):
    #        if s[i:j] in base:
    #            result.append(s[i:j])
    #print(result)
    #return len(set(result))
    #print(len(s))
    #print(len(set(s)))
    #print(set(s))
    #print(set(s))
    #print(set(s))
    #print(set
