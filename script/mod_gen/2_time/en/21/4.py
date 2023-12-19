def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    diff = nums[1] - nums[0]
    count = 0
    res = 0
    for i in range(2, len(nums)):
        if nums[i] - nums[i-1] == diff:
            count += 1
            res += count
        else:
            diff = nums[i] - nums[i-1]
            count = 0
    return res

if __name__ == '__main__':
    numberOfArithmeticSlices()