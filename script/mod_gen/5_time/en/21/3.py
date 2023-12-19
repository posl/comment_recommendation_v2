def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #Solution 1
    #numOfSubarrays = 0
    #for i in range(0,len(nums)-2):
    #    for j in range(i+2,len(nums)):
    #        diff = nums[i+1] - nums[i]
    #        if nums[j] - nums[j-1] == diff:
    #            numOfSubarrays += 1
    #        else:
    #            break
    #return numOfSubarrays
    #Solution 2
    numOfSubarrays = 0
    for i in range(0,len(nums)-2):
        diff = nums[i+1] - nums[i]
        for j in range(i+2,len(nums)):
            if nums[j] - nums[j-1] == diff:
                numOfSubarrays += 1
            else:
                break
    return numOfSubarrays
print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1]))
print(numberOfArithmeticSlices([1,2,3,4,5,6]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
print(numberOfArithmeticSlices([1,2,3,4
