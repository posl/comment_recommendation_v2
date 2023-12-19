def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    for i in range(len(nums)-2):
        if nums[i+1] - nums[i] == nums[i+2] - nums[i+1]:
            count += 1
            j = 3
            while i+j < len(nums) and nums[i+j] - nums[i+j-1] == nums[i+1] - nums[i]:
                count += 1
                j += 1
    return count

if __name__ == '__main__':
    numberOfArithmeticSlices()