def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #The key is to find the difference between two consecutive elements
    #Then use the difference as key and the number of arithmetic sequences as value in a dictionary
    #Initialize the dictionary with the first two elements of the array
    #If the difference between the third element and the second element is the same as the difference between the second element and the first element, then the number of arithmetic sequences is 1
    #If the difference between the third element and the second element is not the same as the difference between the second element and the first element, then the number of arithmetic sequences is 0
    #If the difference between the third element and the second element is the same as the difference between the second element and the first element, then the number of arithmetic sequences is the number of arithmetic sequences of the second element plus 1
    #If the difference between the third element and the second element is not the same as the difference between the second element and the first element, then the number of arithmetic sequences is the number of arithmetic sequences of the second element
    #If the difference between the third element and the second element is the same as the difference between the second element and the first element, then the number of arithmetic sequences is the number of arithmetic sequences of the second element plus 1
    #If the difference between the third element and the second element is not the same as the difference between the second element and the first element, then the number of arithmetic sequences is the number of arithmetic sequences of the second element
    #If the difference between the third element and the second element is the same as the difference between the second element and the first element, then the number of arithmetic sequences is the number of arithmetic sequences of the second element plus 1
    #If the difference between the third element and the second element is not the same as the difference between the second element and the first element, then the number of arithmetic sequences is the number of arithmetic sequences of the second element
    #If the difference between the third element and the second element is the same as the difference between the second element and the first element, then the number of arithmetic sequences is the number of arithmetic sequences of the second element plus 1
    #If the difference between the third element and the second element is not the same as the difference

if __name__ == '__main__':
    numberOfArithmeticSlices()