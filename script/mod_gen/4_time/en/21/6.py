def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    count = 0
    diff = nums[1] - nums[0]
    slice = 1
    for i in range(1, len(nums) - 1):
        if nums[i + 1] - nums[i] == diff:
            slice += 1
        else:
            if slice >= 2:
                count += slice * (slice - 1) // 2
            diff = nums[i + 1] - nums[i]
            slice = 1
    if slice >= 2:
        count += slice * (slice - 1) // 2
    return count

if __name__ == '__main__':
    numberOfArithmeticSlices()