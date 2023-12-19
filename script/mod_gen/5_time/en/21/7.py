def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    count = 0
    i = 0
    while i < len(nums) - 2:
        j = i + 1
        diff = nums[j] - nums[i]
        while j < len(nums) - 1:
            if nums[j + 1] - nums[j] == diff:
                count += 1
                j += 1
            else:
                break
        i += 1
    return count

if __name__ == '__main__':
    numberOfArithmeticSlices()