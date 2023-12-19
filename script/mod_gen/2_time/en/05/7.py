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
