def getMaxRepetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    # Solution 1
    # Time Complexity: O(n1 * n2 * s1)
    # Space Complexity: O(n1 * n2 * s1)
    #s1 = s1 * n1
    #s2 = s2 * n2
    #i = 0
    #j = 0
    #count = 0
    #while j < len(s2):
    #    if s1[i] == s2[j]:
    #        if j == len(s2) - 1:
    #            count += 1
    #        i += 1
    #        j += 1
    #    else:
    #        i += 1
    #    if i == len(s1):
    #        i = 0
    #return count // n2
    # Solution 2
    # Time Complexity: O(n1 + n2 + s1)
    # Space Complexity: O(n1 + n2 + s1)
    s1 = s1 * n1
    s2 = s2 * n2
    i = 0
    j = 0
    count = 0
    visited = {}
    while i < len(s1):
        if s1[i] == s2[j]:
            if j == len(s2) - 1:
                count += 1
                if j not in visited:
                    visited[j] = [i, count]
                else:
                    prev_i, prev_count = visited[j]
                    diff_i = i - prev_i
                    diff_count = count - prev_count
                    if diff_i == 0:
                        return diff_count // n2
                    else:
                        n = (len(s1) - i) // diff_i
                        i += n * diff_i
                        count += n * diff_count
            i += 1
            j += 1
        else:
            i += 1
        if i == len(s1):
            i = 0
    return count // n2
print(getMaxRepetitions("aaa",
