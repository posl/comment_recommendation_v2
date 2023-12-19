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

if __name__ == '__main__':
    uniqueSubstringInWraparoundString()