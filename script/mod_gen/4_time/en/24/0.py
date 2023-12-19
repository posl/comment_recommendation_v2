def numDistinct(s: str, t: str) -> int:
    if len(s) < len(t):
        return 0
    if s == t:
        return 1
    if len(t) == 0:
        return 1
    if len(s) == 1:
        if s == t:
            return 1
        else:
            return 0
    if s[0] == t[0]:
        return numDistinct(s[1:], t[1:]) + numDistinct(s[1:], t)
    else:
        return numDistinct(s[1:], t)

if __name__ == '__main__':
    numDistinct()