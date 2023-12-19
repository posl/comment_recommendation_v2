def getMaxRepetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    # In the worst case, we need to scan the whole s1 string to find the first character of s2
    # Then we can start to scan s2, and we need to scan n2 times
    # So we need to scan s1 for n1 times
    # So the time complexity is O(n1 * n2)
    # We can use a map to record the index of s1 and s2
    # If we find the same index of s1 and s2, we can use the map to get the number of s2 we can get
    # Then we can use the number to calculate the result
    # The time complexity is O(n1 + n2)
    # The space complexity is O(n2)
    # The key is to find the loop
    # The loop is the substring of s1
    # The loop is the substring of s2
    # The loop is the substring of s1 and s2
    # The loop is the substring of s2 and s1
    # The loop is the substring of s1 and s2 and s1
    # The loop is the substring of s2 and s1 and s2
    # The loop is the substring of s1 and s2 and s1 and s2
    # The loop is the substring of s2 and s1 and s2 and s1
    # The loop is the substring of s1 and s2 and s1 and s2 and s1
    # The loop is the substring of s2 and s1 and s2 and s1 and s2
    # The loop is the substring of s1 and s2 and s1 and s2 and s1 and s2
    # The loop is the substring of s2 and s1 and s2 and s1 and s2 and s1
    # The loop is the substring of s1 and s2 and s1 and s2 and s1 and s2 and s1
    # The loop is the substring of s2 and s1 and s2 and s1 and s2 and

if __name__ == '__main__':
    getMaxRepetitions()