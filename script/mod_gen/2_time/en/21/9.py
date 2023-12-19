def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    total = 0
    i = 0
    while i < len(nums) - 2:
        if nums[i+1] - nums[i] == nums[i+2] - nums[i+1]:
            count = 3
            j = i + 3
            while j < len(nums) and nums[j] - nums[j-1] == nums[j-1] - nums[j-2]:
                count += 1
                j += 1
            total += (count - 2) * (count - 1) // 2
            i = j - 1
        else:
            i += 1
    return total

if __name__ == '__main__':
    numberOfArithmeticSlices()