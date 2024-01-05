def getMaxRepetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    #Approach: Brute Force
    #Time Complexity: O(n1 * n2)
    #Space Complexity: O(1)
    reps = 0
    s1_idx = 0
    s2_idx = 0
    while reps < n1:
        if s1[s1_idx] == s2[s2_idx]:
            s2_idx += 1
            if s2_idx == len(s2):
                s2_idx = 0
                reps += 1
        s1_idx += 1
        if s1_idx == len(s1):
            s1_idx = 0
    return reps // n2

if __name__ == '__main__':
    s1 = input()
    n1 = int(input())
    s2 = input()
    n2 = int(input())
    a = getMaxRepetitions(s1, n1, s2, n2)
    print(a)