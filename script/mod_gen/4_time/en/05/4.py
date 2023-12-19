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

if __name__ == '__main__':
    uniqueSubstringsInWraparoundString()