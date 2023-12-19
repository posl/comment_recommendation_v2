def unique_substrings_in_wraparound_string(s):
    """
    :type s: str
    :rtype: int
    """
    res = 0
    count = [0] * 26
    for i in range(len(s)):
        if i > 0 and (ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25):
            res += 1
        else:
            res = 1
        count[ord(s[i]) - ord('a')] = max(count[ord(s[i]) - ord('a')], res)
    return sum(count)

if __name__ == '__main__':
    unique_substrings_in_wraparound_string()