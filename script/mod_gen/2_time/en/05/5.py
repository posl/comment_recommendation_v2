def unique_substrings_in_wraparound_string(s):
    """
    :type s: str
    :rtype: int
    """
    count = [0] * 26
    max_len = 0
    for i in range(len(s)):
        if i > 0 and (ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i - 1]) - ord(s[i]) == 25):
            max_len += 1
        else:
            max_len = 1
        count[ord(s[i]) - ord('a')] = max(count[ord(s[i]) - ord('a')], max_len)
    return sum(count)
    
print(unique_substrings_in_wraparound_string('zab'))
print(unique_substrings_in_wraparound_string('cac'))
print(unique_substrings_in_wraparound_string('a'))
