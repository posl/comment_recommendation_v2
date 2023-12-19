def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #Solution 1
    #if len(nums) < 3:
    #    return 0
    #count = 0
    #for i in range(0, len(nums)-2):
    #    diff = nums[i+1] - nums[i]
    #    for j in range(i+1, len(nums)-1):
    #        if nums[j+1] - nums[j] == diff:
    #            count += 1
    #        else:
    #            break
    #return count
    
    #Solution 2
    #if len(nums) < 3:
    #    return 0
    #count = 0
    #for i in range(0, len(nums)-2):
    #    diff = nums[i+1] - nums[i]
    #    for j in range(i+1, len(nums)-1):
    #        if nums[j+1] - nums[j] == diff:
    #            count += 1
    #        else:
    #            break
    #return count
    
    #Solution 3
    if len(nums) < 3:
        return 0
    count = 0
    for i in range(0, len(nums)-2):
        diff = nums[i+1] - nums[i]
        for j in range(i+1, len(nums)-1):
            if nums[j+1] - nums[j] == diff:
                count += 1
            else:
                break
    return count
    
print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1]))
print(numberOfArithmeticSlices([1,2,3,4,5,6]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print("The values above should be 3, 0, 10, 25, and 35.")

if __name__ == '__main__':
    numberOfArithmeticSlices()