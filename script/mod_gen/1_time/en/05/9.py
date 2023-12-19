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

if __name__ == '__main__':
    uniqueSubstringsInWraparoundString()