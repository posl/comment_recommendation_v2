def unique_substrings_in_wraparound_string(s):
    """
    :type p: str
    :type s: str
    :rtype: List[int]
    """
    if len(s) == 0:
        return 0
    count = [0] * 26
    max_len = 1
    count[ord(s[0]) - ord('a')] = 1
    for i in range(1, len(s)):
        if (ord(s[i]) - ord(s[i - 1])) % 26 == 1:
            max_len += 1
        else:
            max_len = 1
        count[ord(s[i]) - ord('a')] = max(count[ord(s[i]) - ord('a')], max_len)
    return sum(count)
print(unique_substrings_in_wraparound_string("zab"))
