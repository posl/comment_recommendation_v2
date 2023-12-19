def distinctSubsequences(s, t):
    if len(s) < len(t):
        return 0
    elif len(s) == len(t):
        if s == t:
            return 1
        else:
            return 0
    else:
        i = 0
        count = 0
        while i < len(s):
            if s[i] == t[0]:
                count += distinctSubsequences(s[i+1:], t[1:])
            i += 1
        return count

if __name__ == '__main__':
    distinctSubsequences()