def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    count = 0
    for i in range(len(nums)-2):
        for j in range(i+2, len(nums)):
            if nums[j] - nums[j-1] == nums[j-1] - nums[j-2]:
                count += 1
            else:
                break
    return count
nums = [1,2,3,4]
print(numberOfArithmeticSlices(nums))
nums = [1]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
print(numberOfArithmeticSlices
