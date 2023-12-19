def uniqueSubstringInWraparoundString(s):
    """
    :type p: str
    :rtype: int
    """
    if not s:
        return 0
    # Initialize the count of all unique substrings end with letter 'a', 'b', ..., 'z'.
    # Use array instead of dictionary to make it run faster.
    count = [0] * 26
    # Store longest contiguous substring ends at current position.
    maxLengthCur = 0
    for i in range(len(s)):
        # Check if the current character is continuation of s[i - 1]
        if i > 0 and (ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i - 1]) - ord(s[i]) == 25):
            maxLengthCur += 1
        else:
            maxLengthCur = 1
        # Get the index of current character, e.g. 'a' -> 0, 'z' -> 25.
        index = ord(s[i]) - ord('a')
        count[index] = max(count[index], maxLengthCur)
    # Sum to get result
    return sum(count)

if __name__ == '__main__':
    uniqueSubstringInWraparoundString()