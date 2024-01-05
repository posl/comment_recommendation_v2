def getMaxRepetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    #Find the number of times s2 can be found in s1
    #For example, if s1 = "abcabcabc", s2 = "abc" then we can find 3 instances of s2 in s1
    #We can then find the number of times s2 can be found in s1*n1
    #For example, if s1 = "abcabcabc", s2 = "abc", n1 = 3 then we can find 9 instances of s2 in s1*n1
    #We can then find the number of times s2 can be found in s1*n1*n2
    #For example, if s1 = "abcabcabc", s2 = "abc", n1 = 3, n2 = 2 then we can find 18 instances of s2 in s1*n1*n2
    #We can then find the number of times s2 can be found in s1*n1*n2*n3
    #For example, if s1 = "abcabcabc", s2 = "abc", n1 = 3, n2 = 2, n3 = 1 then we can find 18 instances of s2 in s1*n1*n2*n3
    #We can then find the number of times s2 can be found in s1*n1*n2*n3*n4
    #For example, if s1 = "abcabcabc", s2 = "abc", n1 = 3, n2 = 2, n3 = 1, n4 = 1 then we can find 18 instances of s2 in s1*n1*n2*n3*n4
    #We can then find the number of times s2 can be found in s1*n1*n2*n3*n4*n5
    #For example, if s1 = "abcabcabc", s2 = "abc", n1 = 3, n2 = 2, n3 = 1, n4 = 1, n5 = 1 then we can find 18

if __name__ == '__main__':
    s1 = input()
    n1 = int(input())
    s2 = input()
    n2 = int(input())
    a = getMaxRepetitions(s1, n1, s2, n2)
    print(a)