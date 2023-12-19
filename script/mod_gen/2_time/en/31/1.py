def getMaxRepetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    # if s1 is empty or n1 is 0, return 0
    if not s1 or not n1:
        return 0
    # if s2 is empty or n2 is 0, return n1
    if not s2 or not n2:
        return n1
    # initialize the current index of s2, the number of repetitions
    # of s1 and s2, and the next index of s1
    curr_s2_index = 0
    s1_repetitions = 0
    s2_repetitions = 0
    next_s1_index = 0
    # while we haven't reached the end of s1
    while next_s1_index < len(s1):
        # if the current character of s1 is the same as the current
        # character of s2, move to the next character of s2
        if s1[next_s1_index] == s2[curr_s2_index]:
            curr_s2_index += 1
            # if we have reached the end of s2, we have found a repetition
            # of s2 in s1, so reset the index of s2 and increment the number
            # of repetitions of s2
            if curr_s2_index == len(s2):
                curr_s2_index = 0
                s2_repetitions += 1
        # move to the next index of s1
        next_s1_index += 1
        # if we have reached the end of s1, increment the number of
        # repetitions of s1 and reset the index of s1
        if next_s1_index == len(s1):
            next_s1_index = 0
            s1_repetitions += 1
    # return the number of repetitions of s2 in s1 divided by n2
    return s2_repetitions // n2

if __name__ == '__main__':
    getMaxRepetitions()