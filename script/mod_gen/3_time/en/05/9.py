def unique_substrings_in_wraparound_string(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    if n == 0:
        return 0
    count = [0] * 26
    count[ord(s[0]) - ord('a')] = 1
    result = 1
    for i in range(1, n):
        if ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i]) - ord(s[i - 1]) == -25:
            result += 1
        else:
            result = 1
        count[ord(s[i]) - ord('a')] = max(count[ord(s[i]) - ord('a')], result)
    return sum(count)

if __name__ == '__main__':
    unique_substrings_in_wraparound_string()