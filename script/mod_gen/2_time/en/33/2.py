def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            diff = nums[j] - nums[i]
            for k in range(j+1, len(nums)):
                if nums[k] - nums[j] == diff:
                    count += 1
                elif nums[k] - nums[j] > diff:
                    break
    return count
nums = [2,4,6,8,10]
print(numberOfArithmeticSlices(nums))
nums = [7,7,7,7,7]
print(numberOfArithmeticSlices(nums))
