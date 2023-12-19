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
