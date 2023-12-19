def uniqueSubstringInWraproundString(s):
    """
    :type s: str
    :rtype: int
    """
    # initialize an array of length 26 to record the max length of substring ends with each character
    # of 'a' to 'z'
    # for example, count[0] is the max length of substring ends with 'a'
    # count[1] is the max length of substring ends with 'b'
    # ...
    # count[25] is the max length of substring ends with 'z'
    count = [0] * 26
    # store the max length of substring
    maxLength = 0
    for i in range(len(s)):
        # if the current character is the same as the previous character or
        # the current character is 'a' and the previous character is 'z',
        # the current character can be appended to the previous substring
        if i > 0 and (ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i - 1]) - ord(s[i]) == 25):
            maxLength += 1
        # otherwise, the current character can only be a new substring
        else:
            maxLength = 1
        # update the max length of substring ends with the current character
        count[ord(s[i]) - ord('a')] = max(count[ord(s[i]) - ord('a')], maxLength)
    # return the sum of the max length of substring ends with each character
    return sum(count)

if __name__ == '__main__':
    uniqueSubstringInWraproundString()