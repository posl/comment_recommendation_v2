def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    result = 0
    for i in range(len(nums)):
        for j in range(i+2, len(nums)+1):
            if all(nums[k+1]-nums[k] == nums[i+1]-nums[i] for k in range(i+1, j-1)):
                result += 1
    return result
print(numberOfArithmeticSlices([1,2,3,4]))
