def getMaxRepetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    # get a list of indexes of s1 where s2 starts
    # get a list of indexes of s2 where s2 starts
    # find the longest sequence of s2 indexes where the difference between two indexes is the same
    # find the longest sequence of s1 indexes where the difference between two indexes is the same
    # find the longest sequence of s1 indexes where the difference between two indexes is the same and is in the previous sequence
    # find the longest sequence of s2 indexes where the difference between two indexes is the same and is in the previous sequence
    # find the longest sequence of s1 indexes where the difference between two indexes is the same and is in the previous sequence and the difference between the first and last index is the same as the longest sequence of s2 indexes where the difference between two indexes is the same and is in the previous sequence
    # find the longest sequence of s1 indexes where the difference between two indexes is the same and is in the previous sequence and the difference between the first and last index is the same as the longest sequence of s2 indexes where the difference between two indexes is the same and is in the previous sequence and the difference between the first and last index is the same as the longest sequence of s1 indexes where the difference between two indexes is the same and is in the previous sequence
    # find the longest sequence of s1 indexes where the difference between two indexes is the same and is in the previous sequence and the difference between the first and last index is the same as the longest sequence of s2 indexes where the difference between two indexes is the same and is in the previous sequence and the difference between the first and last index is the same as the longest sequence of s1 indexes where the difference between two indexes is the same and is in the previous sequence and the difference between the first and last index is the same as the longest sequence of s2 indexes where the difference between two indexes is the same and is in the previous sequence
    # find the longest sequence of s1 indexes where the difference between two indexes is the same and is in the previous sequence and the difference between the first and

if __name__ == '__main__':
    s1 = input()
    n1 = int(input())
    s2 = input()
    n2 = int(input())
    a = getMaxRepetitions(s1, n1, s2, n2)
    print(a)