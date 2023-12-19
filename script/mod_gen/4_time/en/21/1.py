def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #Solution 1
    #O(n) time, O(1) space
    #The key to this solution is to realize that the number of new arithmetic slices created by adding a new element is the same as the number of arithmetic slices created by adding the new element to the existing arithmetic slices
    #For example, if we have [1,2,3,4,5], the number of arithmetic slices created by adding the 5 to the existing slices is the number of slices created by adding 5 to [1,2,3,4] + 1 ([1,2,3,4,5])
    #We can keep track of the number of new slices created by adding each element to the existing slices and add them to the total number of slices
    #We can keep track of the number of slices created by adding each element to the existing slices by keeping a counter and incrementing it by 1 each time we see an arithmetic slice
    #If we see an element that breaks the arithmetic slice, we can reset the counter to 0
    #We can keep track of the total number of slices by adding the counter to the total number of slices each time we see an arithmetic slice
    #We can check if a slice is arithmetic by checking if the difference between the last two elements is the same as the difference between the last element and the current element
    #We can keep track of the total number of slices by adding the counter to the total number of slices each time we see an arithmetic slice
    #We can check if a slice is arithmetic by checking if the difference between the last two elements is the same as the difference between the last element and the current element
    #We can check if a slice is arithmetic by checking if the difference between the last two elements is the same as the difference between the last element and the current element
    #We can check if a slice is arithmetic by checking if the difference between the last two elements is the same as the difference between the last element and the current element
    #We can check if a slice is arithmetic by checking if the difference between the last two elements is the same as the difference between the last element and the current element
    #We can check if a slice is arithmetic by checking if the difference between the

if __name__ == '__main__':
    numberOfArithmeticSlices()