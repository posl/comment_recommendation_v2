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

if __name__ == '__main__':
    findSubstringInWraproundString()