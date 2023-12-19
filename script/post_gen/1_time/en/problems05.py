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

=======
Suggestion 2

def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    s = list(s)
    s = [ord(i)-97 for i in s]
    s = [i-26 if i>25 else i for i in s]
    count = 1
    maxCount = [0]*26
    maxCount[s[0]] = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]+1 or (s[i] == 0 and s[i-1] == 25):
            count += 1
        else:
            count = 1
        maxCount[s[i]] = max(maxCount[s[i]],count)
    return sum(maxCount)

print(findSubstringInWraproundString("zab"))

=======
Suggestion 3

def unique_substrings_in_wraparound_string(s):
    """
    :type p: str
    :type s: str
    :rtype: List[int]
    """
    if len(s) == 0:
        return 0
    count = [0] * 26
    max_len = 1
    count[ord(s[0]) - ord('a')] = 1
    for i in range(1, len(s)):
        if (ord(s[i]) - ord(s[i - 1])) % 26 == 1:
            max_len += 1
        else:
            max_len = 1
        count[ord(s[i]) - ord('a')] = max(count[ord(s[i]) - ord('a')], max_len)
    return sum(count)

print(unique_substrings_in_wraparound_string("zab"))

=======
Suggestion 4

def uniqueSubstringsInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    substrings = set()
    substrings.add(s[0])
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i]) - ord(s[i - 1]) == -25:
            substrings.add(s[i])
            substrings.add(s[i - 1] + s[i])
        else:
            substrings.add(s[i])
    return len(substrings)

print(uniqueSubstringsInWraproundString("zab"))

=======
Suggestion 5

def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if not s:
        return 0
    
    res = 0
    dp = [0] * 26
    dp[ord(s[0]) - ord('a')] = 1
    count = 1
    
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i]) - ord(s[i - 1]) == -25:
            count += 1
        else:
            count = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
    
    for i in range(26):
        res += dp[i]
    
    return res

print(findSubstringInWraproundString("zab"))

=======
Suggestion 6

def findSubstringInWraproundString(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    dp = [0] * 26
    dp[ord(s[0]) - ord('a')] = 1
    count = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i - 1]) - ord(s[i]) == 25:
            count += 1
        else:
            count = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
    return sum(dp)

print(findSubstringInWraproundString("zab"))
print(findSubstringInWraproundString("cac"))
print(findSubstringInWraproundString("a"))
print(findSubstringInWraproundString(""))
print(findSubstringInWraproundString("abc"))
print(findSubstringInWraproundString("zabcdefz"))

=======
Suggestion 7

def uniqueSubstringInWraparoundString(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    res = 0
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

print(uniqueSubstringInWraparoundString("zab"))

=======
Suggestion 8

def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    dp = [0]*26
    dp[ord(s[0]) - ord('a')] = 1
    count = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i]) - ord(s[i-1]) == -25:
            count += 1
        else:
            count = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
    return sum(dp)
    
s1 = "a"
s2 = "cac"
s3 = "zab"
s4 = "zaba"
s5 = "zabca"
s6 = "zabcd"
s7 = "zabcdef"
s8 = "zabcdefg"
s9 = "zabcdefgh"
s10 = "zabcdefghi"
s11 = "zabcdefghij"
s12 = "zabcdefghijk"
s13 = "zabcdefghijkl"
s14 = "zabcdefghijklm"
s15 = "zabcdefghijklmn"
s16 = "zabcdefghijklmno"
s17 = "zabcdefghijklmnop"
s18 = "zabcdefghijklmnopq"
s19 = "zabcdefghijklmnopqr"
s20 = "zabcdefghijklmnopqrs"
s21 = "zabcdefghijklmnopqrst"
s22 = "zabcdefghijklmnopqrstu"
s23 = "zabcdefghijklmnopqrstuv"
s24 = "zabcdefghijklmnopqrstuvw"
s25 = "zabcdefghijklmnopqrstuvwx"
s26 = "zabcdefghijklmnopqrstuvwxy"
s27 = "zabcdefghijklmnopqrstuvwxyz"
s28 = "zabcdefghijklmnopqrstuvwxyzab"
s29 = "zabcdefghijklmnopqrstuvwxyzabc"
s30 = "zabcdefghijklmnopqrstuvwxyzabcd"
s31 = "zabcdefghijklmnopqrstuvwxyzabcde"
s32 = "zabcdefghijklmnopqrstuvwxyzabcdef"
s33 = "zabcdefghijklmnopqrstuvwxyzabcdefg"
s34 = "zabcdefghijklmnopqrstuvwxyzabcdefgh"
s35 = "zabcdefghijklmnopqrstuvwxyzabcdefghi"
s36 = "zabcdefghijklmnopqrstuvwxyzabcdefghij"
s37 = "zabcdefghijklmnopqrstuvwxyzabcdefghijk"
s38 = "zabcdefghijklmnopqrstuvwxyzabcdefghijkl"
s39 = "zabcdefghijklmnopqrstuvwxyzabcdefghijklm"
s40 = "zabcdefghijklmnopqrstuvwxyzabcdefghijklmn"
s41 = "zabcdefghijklmnopqrstuvwxyzabcdefghijklmno"
s42 = "

=======
Suggestion 9

def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    substring = set()
    substring.add(s[0])
    count = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1 or (s[i] == 'a' and s[i-1] == 'z'):
            count += 1
        else:
            substring.add(s[i])
            count = 1
        substring.add(s[i-count+1:i+1])
    return len(substring)

print(findSubstringInWraproundString("cac"))
print(findSubstringInWraproundString("zab"))
print(findSubstringInWraproundString("a"))
print(findSubstringInWraproundString("zabc"))
print(findSubstringInWraproundString("zabcd"))
print(findSubstringInWraproundString("zabcde"))
print(findSubstringInWraproundString("zabcdef"))
print(findSubstringInWraproundString("zabcdefg"))
print(findSubstringInWraproundString("zabcdefgh"))
print(findSubstringInWraproundString("zabcdefghi"))
print(findSubstringInWraproundString("zabcdefghij"))
print(findSubstringInWraproundString("zabcdefghijk"))
print(findSubstringInWraproundString("zabcdefghijkl"))
print(findSubstringInWraproundString("zabcdefghijklm"))
print(findSubstringInWraproundString("zabcdefghijklmn"))
print(findSubstringInWraproundString("zabcdefghijklmno"))
print(findSubstringInWraproundString("zabcdefghijklmnop"))
print(findSubstringInWraproundString("zabcdefghijklmnopq"))
print(findSubstringInWraproundString("zabcdefghijklmnopqr"))
print(findSubstringInWraproundString("zabcdefghijklmnopqrs"))
print(findSubstringInWraproundString("zabcdefghijklmnopqrst"))
print(findSubstringInWraproundString("zabcdefghijklmnopqrstu"))
print(findSubstringInWraproundString("zabcdefghijklmnopqrstuv"))
print(findSubstringInWraproundString("zabcdefghijklmnopqrstuvw"))
print(findSubstringInWraproundString("zabcdefghijklmnopqrstuvwx"))
print(findSubstringInWraproundString("zabcdefghijklmnopqrstuvwxy"))
print(findSubstringInWraproundString("zabcdefghijklmnopqrstuvwxyz"))
print(findSubstringInWraproundString("zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))
print(findSubstringInWraproundString("zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))
print(findSubstringInWraproundString("zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz

=======
Suggestion 10

def uniqueSubstringsInWraparoundString(s):
    """
    :type p: str
    :rtype: List[int]
    """
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    base = "abcdefghijklmnopqrstuvwxyz"
    base = base + base
    substrings = []
    for i in range(len(s)):
        for j in range(len(base)):
            if base[j] == s[i]:
                substrings.append(s[i])
                break
            else:
                continue
    print(substrings)
    return len(set(substrings))

print(uniqueSubstringsInWraparoundString("a"))
print(uniqueSubstringsInWraparoundString("cac"))
print(uniqueSubstringsInWraparoundString("zab"))
print(uniqueSubstringsInWraparoundString("zaba"))
print(uniqueSubstringsInWraparoundString("zabac"))
print(uniqueSubstringsInWraparoundString("zabacd"))
print(uniqueSubstringsInWraparoundString("zabacde"))
print(uniqueSubstringsInWraparoundString("zabacdef"))
print(uniqueSubstringsInWraparoundString("zabacdefg"))
print(uniqueSubstringsInWraparoundString("zabacdefgh"))
print(uniqueSubstringsInWraparoundString("zabacdefghi"))
print(uniqueSubstringsInWraparoundString("zabacdefghij"))
print(uniqueSubstringsInWraparoundString("zabacdefghijk"))
print(uniqueSubstringsInWraparoundString("zabacdefghijkl"))
print(uniqueSubstringsInWraparoundString("zabacdefghijklm"))
print(uniqueSubstringsInWraparoundString("zabacdefghijklmn"))
print(uniqueSubstringsInWraparoundString("zabacdefghijklmno"))
print(uniqueSubstringsInWraparoundString("zabacdefghijklmnop"))
print(uniqueSubstringsInWraparoundString("zabacdefghijklmnopq"))
print(uniqueSubstringsInWraparoundString("zabacdefghijklmnopqr"))
print(uniqueSubstringsInWraparoundString("zabacdefghijklmnopqrs"))
print(uniqueSubstringsInWraparoundString("zabacdefghijklmnopqrst"))
print(uniqueSubstringsInWraparoundString("zabacdefghijklmnopqrstu"))
print(uniqueSubstringsInWraparoundString("zabacdefghijklmnopqrstuv"))
print
