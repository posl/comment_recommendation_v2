def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    count = 0
    for i in range(len(nums) - 2):
        diff = nums[i + 1] - nums[i]
        for j in range(i + 2, len(nums)):
            if nums[j] - nums[j - 1] == diff:
                count += 1
            else:
                break
    return count

if __name__ == '__main__':
    numberOfArithmeticSlices()