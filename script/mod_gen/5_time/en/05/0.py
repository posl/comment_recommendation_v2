def unique_substring(s):
    if s == None or len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    count = 0
    for i in range(len(s)):
        count += 1
        for j in range(i+1, len(s)):
            if ord(s[j])-ord(s[j-1]) == 1 or ord(s[j])-ord(s[j-1]) == -25:
                count += 1
            else:
                break
    return count
print(unique_substring("zab"))
print(unique_substring("cac"))
print(unique_substring("a"))
print(unique_substring("zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd"))
print(unique_substring("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijkl
