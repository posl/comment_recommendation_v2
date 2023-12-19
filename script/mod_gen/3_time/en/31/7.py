def getMaxRepetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    # We need to find the maximum number of times we can
    # repeat s2, such that we can get s1. We can repeat
    # s2 at most n2 * n1 times. If we have a string s of
    # length n, and we repeat it k times, then the length
    # of the resulting string is n * k. We can use this
    # fact to find the maximum number of times we can
    # repeat s2.
    # We can use a greedy approach to find the number of
    # times we can repeat s2. We can keep a pointer to
    # the current character we are looking for in s2.
    # If we find the current character, we move the
    # pointer to the next character. If we reach the
    # end of s2, we have found one repetition. If we
    # reach the end of s1, we have found one repetition
    # of s2 in s1. If we reach the end of s1 and we have
    # not found a repetition of s2, we cannot find a
    # repetition of s2 in s1.
    # We keep track of the number of times we have found
    # a repetition of s2 in s1. We keep track of the
    # number of times we have found s2 in s1. We keep
    # track of the number of times we have found the
    # current character in s2.
    # We can use a dictionary to keep track of the
    # number of times we have found the current
    # character in s2.
    # We can use a list to keep track of the number
    # of times we have found a repetition of s2 in
    # s1.
    # We can use a list to keep track of the number
    # of times we have found s2 in s1.
    # We can use a list to keep track of the current
    # character in s2.
    # We can use a list to keep track of

if __name__ == '__main__':
    getMaxRepetitions()