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
